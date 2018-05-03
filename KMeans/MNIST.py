from tensorflow.examples.tutorials.mnist import input_data
from scipy.spatial import distance
import numpy as np
from datetime import datetime

def get_distance(a,b):
	return distance.euclidean(a,b)


def make_clusters(training_images, training_labels, centroids, k):
	number_of_images = training_images.shape[0]
	clusters = [[] for i in range(0, k)]

	for i in range(0, number_of_images - 1):
		distances = []
		for j in range(0, k):
			distance = get_distance(training_images[i], centroids[j])
			distances.append((distance, j))

		distances = sorted(distances)
		cluster_number = distances[0][1]
		clusters[cluster_number].append(i)


	return clusters

def recalculate_centroids(training_images, centroids, clusters):
	for i in range (0, len(clusters)):
		image_list = []
		for image_index in clusters[i]:
			image_list.append(training_images[image_index])
		np_array = np.array(image_list)
		centroids[i] = np_array.mean(axis = 0)

	return centroids

def remake_cluster(clusters, centroids, training_images):
	change_occured = False

	for i in range(0, len(clusters)):
		cluster = clusters[i]
		print("Cluster " + str(i))
		number_of_images_reclustered = 0
		for image_index in cluster:
			distances_to_each_centroid = {}
			for j in range(0 , len(centroids)):
				distance = get_distance(training_images[image_index], centroids[j])
				distances_to_each_centroid[j] = distance

			min_distance = distances_to_each_centroid[0]
			min_distance_index = 0
			for cluster_no in distances_to_each_centroid.keys():
				if distances_to_each_centroid[cluster_no] < min_distance:
					min_distance = distances_to_each_centroid[cluster_no]
					min_distance_index = cluster_no
			if min_distance_index != i:
				clusters[i].remove(image_index)
				clusters[min_distance_index].append(image_index)
				change_occured = True
				number_of_images_reclustered += 1
		print("Number of images reclustered: " + str(number_of_images_reclustered))

	return clusters, change_occured

def KMeans(k):

	mnist = input_data.read_data_sets("MNIST_data/")

	training_images = mnist.train.images
	training_labels = mnist.train.labels
	
	number_of_images = training_images.shape[0]

	startTime = datetime.now()
	# centroid_indexs = np.linspace(0, number_of_images-1, k)
	# centroid_indexs = list(map(int, centroid_indexs))
	centroid_indexs = [7,4,13,1,2,27,18,0,5,8]
	
	centroids = []
	for i in range(0, len(centroid_indexs)):
		centroids.append(training_images[centroid_indexs[i]])
	# step 1
	clusters = make_clusters(training_images, training_labels, centroids, k)

	iteration = 0
	while(iteration <= 20):
		centroids = recalculate_centroids(training_images, centroids, clusters)
		clusters, change_occured = remake_cluster(clusters, centroids, training_images)
		if change_occured == False:
			break
		iteration += 1
	
	for i in range(0, len(clusters)):
		print("Cluster " + str(i))
		for image_index in clusters[i]:
			print(training_labels[image_index], end = " ")
		print()

	print(datetime.now() - startTime)
	
KMeans(10)