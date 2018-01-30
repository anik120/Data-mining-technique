from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
import sklearn.metrics.pairwise
import scipy.sparse
import numpy as np

def main():
	print("Fecthing data..................................")
	newsgroups_train = fetch_20newsgroups(subset='train')
	
	
	print("Data fetched successfully")
	print("Turning data into Tf-IDF format................")
	vectorizer = TfidfVectorizer()
	print("Successfully created bag of words.")
	print("Computing Similarity matrix between documents..")
	vectors = vectorizer.fit_transform(newsgroups_train.data)
	sim_mat = sklearn.metrics.pairwise.euclidean_distances(vectors)
	print("Distane matrix: ")
	print(sim_mat)
	euclidean_distances_output = open("Eucledian Distances.txt", "wb")
	np.save(euclidean_distances_output, sim_mat)

main()