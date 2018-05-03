from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

def get_distance(a,b):
	return distance.euclidean(a,b)


def make_clusters(vectors, centroids, k):
	number_of_docs = vectors.shape[0]
	cluster_assignment = []
	for i in range(0, number_of_docs - 1):
		distances = []
		for j in range(0, k):
			distance = euclidean_distances(vectors[i], centroids[j])
			distance = distance[0][0]
			distances.append((distance, j))

		distances = sorted(distances)
		cluster_number = distances[0][1]
		cluster_assignment.append((cluster_number, i))

	clusters = [[] for i in range(0, k)]

	for assignment in cluster_assignment:
		cluster = assignment[0]
		doc_index = assignment[1]
		clusters[cluster].append(doc_index)

	return clusters

def recalculate_centroids(vectors, centroids, clusters):
	for i in range (0, len(clusters)):
		centroid = vectors[clusters[i][0]]
		for j in range(1, len(clusters[i])):
			centroid += vectors[clusters[i][j]]
		centroid = centroid / len(clusters[i])
		centroids[i] = centroid
	return centroids

def remake_cluster(clusters, centroids, vectors):
	change_occured = False

	for i in range(0, len(clusters)):
		cluster = clusters[i]
		print("Cluster " + str(i))
		number_of_docs_reclustered = 0
		for doc_index in cluster:
			distances_to_each_centroid = {}
			for j in range(0 , len(centroids)):
				distance = euclidean_distances(vectors[doc_index], centroids[j])
				distances_to_each_centroid[j] = distance

			min_distance = distances_to_each_centroid[0]
			min_distance_index = 0
			for cluster_no in distances_to_each_centroid.keys():
				if distances_to_each_centroid[cluster_no] < min_distance:
					min_distance = distances_to_each_centroid[cluster_no]
					min_distance_index = cluster_no
			if min_distance_index != i:
				clusters[i].remove(doc_index)
				clusters[min_distance_index].append(doc_index)
				change_occured = True
				number_of_docs_reclustered += 1
		print("Number of docs reclustered: " + str(number_of_docs_reclustered))

	return clusters, change_occured

def KMeans(k):

	print("Fecthing data..................................")
	newsgroups_train = fetch_20newsgroups(subset='train')
	newsgroups_test = fetch_20newsgroups(subset='test')
	newsgroups_data = newsgroups_test.data

	print("Data fetched successfully")
	print("Turning data into Tf-IDF format................")
	vectorizer = TfidfVectorizer()
	vectors = vectorizer.fit_transform(newsgroups_data)
	
	number_of_docs = vectors.shape[0]


	centroid_indexs = np.linspace(0, number_of_docs-1, k)
	centroid_indexs = list(map(int, centroid_indexs))
	
	centroids = []
	for i in range(0, len(centroid_indexs)):
		centroids.append(vectors[centroid_indexs[i]])
	# step 1
	clusters = make_clusters(vectors, centroids, k)
	
	iteration = 0
	while(iteration <= 20):
		centroids = recalculate_centroids(vectors, centroids, clusters)
		clusters, change_occured = remake_cluster(clusters, centroids, vectors)
		if change_occured == False:
			break
		iteration += 1
	

	for i in range(0, len(clusters)):
		print("Cluster " + str(i))
		for index in clusters[i]:
			print(index, end = " ")
		print()

KMeans(10)