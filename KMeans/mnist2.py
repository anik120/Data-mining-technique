from tensorflow.examples.tutorials.mnist import input_data
from scipy.spatial import distance
import numpy as np
from datetime import datetime


def get_distance(a,b):
	return distance.euclidean(a,b)



def make_clusters(training_images, centroids, k):
	number_of_images = training_images.shape[0]
	clusters = {}

	for i in range(0, number_of_images - 1):
		distances = []
		for j in range(0, k):
			distance = get_distance(training_images[i], centroids[j])
			distances.append((distance, j))

		distances = sorted(distances)
		cluster_number = distances[0][1]
		if cluster_number in clusters:
			clusters[cluster_number].append(i)
		else:
			clusters[cluster_number] = [i]
		centroids[cluster_number] = recalculate_centroid(training_images, clusters[cluster_number]) 

	return clusters


def recalculate_centroid(training_images, points):
	image_list = []
	for image_index in points:
		image_list.append(training_images[image_index])
	np_array = np.array(image_list)
	centroid = np_array.mean(axis = 0)

	return centroid

def remake_cluster(clusters, centroids, training_images):
	cluster_disturbed = False
	number_of_images = training_images.shape[0]

	for cluster_number in clusters.keys():
		number_of_points_reclusterd = 0
		print("Cluster number: " + str(cluster_number))
		print("Number of points reclusterd:", end = " ")
		cluster = clusters[cluster_number]
		for image_index in cluster:
			distances = []
			for j in range(0, len(centroids)):
				distance = get_distance(training_images[image_index], centroids[j])
				distances.append((distance, j))
			distances = sorted(distances)
			cluster_image_index_closest_to = distances[0][1]
			if cluster_image_index_closest_to != cluster_number:
				clusters[cluster_number].remove(image_index)
				centroids[cluster_number] = recalculate_centroid(training_images, clusters[cluster_number])
				clusters[cluster_image_index_closest_to].append(image_index)
				centroids[cluster_image_index_closest_to] = recalculate_centroid(training_images, clusters[cluster_image_index_closest_to])
				cluster_disturbed = True
				number_of_points_reclusterd += 1
		print(str(number_of_points_reclusterd))

	return clusters, cluster_disturbed

def KMeans(k):

	mnist = input_data.read_data_sets("MNIST_data/")

	training_images = mnist.train.images
	training_labels = mnist.train.labels
	
	number_of_images = training_images.shape[0]

	startTime = datetime.now()
	centroid_indexs = np.linspace(0, number_of_images-1, k)
	centroid_indexs = list(map(int, centroid_indexs))
	# centroid_indexs = [7,4,13,1,2,27,18,0,5,8]
	
	centroids = []
	for i in range(0, len(centroid_indexs)):
		centroids.append(training_images[centroid_indexs[i]])
	# step 1
	clusters = make_clusters(training_images, centroids, k)

	iteration = 0
	while(iteration <= 20):
		clusters, change_occured = remake_cluster(clusters, centroids, training_images)
		if change_occured == False:
			break
		iteration += 1
	
	for i in clusters.keys():
		print("Cluster " + str(i))
		for image_index in clusters[i]:
			print(training_labels[image_index], end = " ")
		print()

	print(datetime.now() - startTime)
	
KMeans(10)

