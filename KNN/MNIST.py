from tensorflow.examples.tutorials.mnist import input_data
from scipy.spatial import distance




def get_distance(a,b):
	return distance.euclidean(a,b)



def predict(distances):
	count_dict = {}
	distances = sorted(distances)
	distances = distances[:3]
	for distance in distances:
		if distance[1] in count_dict:
			count_dict[distance[1]] += 1
		else:
			count_dict[distance[1]] = 1

	max_count = 0
	predicted_label = ""

	for label in count_dict:
		if count_dict[label] > max_count:
			max_count = count_dict[label]
			predicted_label = label

	return predicted_label

def KNN(idx, k):
	correct_predictions = 0.0
	total_predictions = 0.0

	mnist = input_data.read_data_sets("MNIST_data/")

	training_images = mnist.train.images
	training_lables = mnist.train.labels
	test_images = mnist.test.images
	test_lables = mnist.test.labels


	# for i in range(0,100):
	# 	distances = []
	# 	test_image = test_images[i]
	# 	for j in range(0, 50000):
	# 		distance = get_distance(test_image, training_images[j])
	# 		distances.append((distance, training_lables[j]))
		
	# 	label = predict(distances)
	# 	if(test_lables[i] == label):
	# 		correct_predictions += 1
	# 	total_predictions += 1

	distances_labels = []
	distances_indexes = []
	test_image = test_images[idx]
	for j in range(0, 50000):
		distance = get_distance(test_image, training_images[j])
		distances_labels.append((distance, training_lables[j]))
		distances_indexes.append((distance, j))

	distances_labels = sorted(distances_labels)
	distances_indexes = sorted(distances_indexes)

	distances_labels = distances_labels[1 : (1 + k)]
	distances_indexes = distances_indexes[1 : (1 + k)]

	print("Five nearest indexs: ")
	for distance in distances_indexes:
		print(distance[1])

	print("Labels of indexes: ")	
	for distance in distances_labels:
		print(distance[1])	

	# prediction_accuracy = (correct_predictions / total_predictions) * 100
	# print("Total prediction: " + str(total_predictions))
	# print("Correct prediction: " + str(correct_predictions))
	# print("Prediction accuracy: " + str(prediction_accuracy))

KNN(0,5)