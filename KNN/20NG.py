from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import euclidean_distances


def predict(distances):
	count_dict = {}
	distances = sorted(distances)
	distances = distances[:10]
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
	print("Fecthing data..................................")
	newsgroups_train = fetch_20newsgroups(subset='train')
	newsgroups_test = fetch_20newsgroups(subset='test')
	newsgroups_data = newsgroups_train.data + newsgroups_test.data

	print("Data fetched successfully")
	print("Turning data into Tf-IDF format................")
	vectorizer = TfidfVectorizer()
	vectors = vectorizer.fit_transform(newsgroups_data)
	
	print("Successfully created bag of words.")
	
	# for i in range(11314, 18846):    #test documents
	# 	test_label = newsgroups_test.target_names[newsgroups_test.target[i-11314]]
	# 	ecu_distances = euclidean_distances(vectors[i], vectors)
	# 	distances = []
	# 	for j in range(0,11314):      #train indexes
	# 		label = newsgroups_train.target_names[newsgroups_train.target[j]]
	# 		distance = ecu_distances[0][j]
	# 		distances.append((distance, label))
	# 	label = predict(distances)
		
	# 	if (test_label == label):
	# 		correct_predictions += 1
	# 	total_predictions += 1
	
	ecu_distances = euclidean_distances(vectors[11314+idx], vectors)
	test_label = newsgroups_test.target_names[newsgroups_test.target[idx]]
	print("Test label: " + test_label)
	print("Five nearest neighbours: ")
	distances_indexs = []
	distances_label = []

	for j in range(0,11314):
		label = newsgroups_train.target_names[newsgroups_train.target[j]]
		distance = ecu_distances[0][j]
		distances_indexs.append((distance, j))
		distances_label.append((distance,label))
	
	distances_indexs = sorted(distances_indexs)
	distances_label = sorted(distances_label)


	for i in range(1, (1 + k)):
		print(distances_indexs[i][1])

	print("Label of nearest neighbours:")
	for i in range(1, (1 + k)):
		print(distances_label[i][1])

	# label = predict(distances)

	# print("Total predictions: " + str(total_predictions))
	# print("Correct predictions: " + str(correct_predictions))
	# print("Accuracy: " + str((total_predictions/correct_predictions) * 100))

KNN(990, 5)
