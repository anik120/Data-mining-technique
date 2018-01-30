from tensorflow.examples.tutorials.mnist import input_data
from scipy.spatial import distance
import scipy


def get_distance(a,b):
	return distance.euclidean(a,b)
	#scipy.spatial.distance.cosine(a,b)



def main():
	mnist = input_data.read_data_sets("MNIST_data/")

	training_images = mnist.train.images[:500]
	training_lables = mnist.train.labels[:500]
	test_images = mnist.test.images[:500]
	test_lables = mnist.test.labels[:500]


	file = open("similarity_matrix.txt", 'w')

	for i in range(0, len(training_images)):
		for j in range(0, len(training_images)):
			file.write(str(get_distance(training_images[i], training_images[j])) + " ")
		file.write("\n")

	file.close()

main()