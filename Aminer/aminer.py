
#import matplotlib.pyplot as plt


def main():
	authors = set()
	publication_venus = set()
	number_of_pulications = 0
	number_of_citations = 0

	file = open("AP_train.txt", 'r')
	
	for line in file:	
		line_parts = line.split()
		
		if line != "\n":

			if line_parts[0] == "#@":
				authors = add_authors(line_parts, authors)

			# if line_parts[0] == "#c":
			# 	publication_venus.add(line_parts[1])

			if line_parts[0] == "#index":
				number_of_pulications += 1

			if line_parts[0] == "#%":
				number_of_citations += 1

	print("Number of unique authors: " + str(len(authors)))
	# print("Number of publication venus: " + str(len(publication_venus)))
	# print("Number of publications: " + str(number_of_pulications))
	# print("Number of citations: " + str(number_of_citations))


def add_authors(line_parts, authors):
	if len(line_parts) > 1:
				book_authors = line_parts[1].split(";")
				for author in book_authors:
					authors.add(author)
	return authors


def author_publications():
	author_publication_list = {}

	#file = open("testfile.txt", 'r')
	file = open("AP_train.txt", 'r')
	for line in file:
		line_parts = line.split()
		if line != "\n" and line_parts[0] == "#*":
			paper = line.replace('#', '').replace('*', '').strip()

		if line != "\n" and line_parts[0] == "#@" and len(line_parts) > 1:
			line = line.replace('#', '').replace('@', '').strip()
			authors = line.split(";")

			for author in authors:
				if author in author_publication_list:
					author_publication_list[author].append(paper)
				else:
					author_publication_list[author] = []
					author_publication_list[author].append(paper)

	author_publication_histogram(author_publication_list)
	
	


def author_publication_histogram(author_publication_list):
	bins = []
	point = 0
	total = 0
	while point <= 250:
		bins.append(point)
		point += 10

	number_of_pulications = []
	for author in author_publication_list.keys():
		total += len(author_publication_list[author])
		number_of_pulications.append(len(author_publication_list[author])) 

	plt.hist(number_of_pulications, bins, histtype = 'bar' )
	plt.show()

	print("Mean number of publications", end = ':')
	print(str(total/len(author_publication_list.keys())))



def number_of_publication_per_venu():
	#file = open("testfile.txt", 'r')
	file = open("AP_train.txt", 'r')
	venu_list = {}

	for line in file:
		line_parts = line.split()
		if(line != "\n" and line_parts[0] == "#c"):
			line = line.replace('#', '').replace('c', '', 1).strip()
			venu = line
			if venu in venu_list:
				venu_list[venu] = venu_list[venu] + 1
			else:
				venu_list[venu] = 1

	venu_with_largest_no_of_publication = ''
	largest_number_of_publication = 0

	for venu in venu_list:
		number_of_pulications = venu_list[venu]
		if number_of_pulications > largest_number_of_publication:
			largest_number_of_publication = number_of_pulications
			venu_with_largest_no_of_publication = venu

	print("Venu with largest number of pulications: ", end = " ")
	print(venu_with_largest_no_of_publication)
	print("Number of publications in above venu: ", end = " ") 
	print(str(venu_list[venu_with_largest_no_of_publication]))

def number_of_references_and_citations():
	#file = open("testfile.txt", 'r')
	file = open("AP_train.txt", 'r')
	reference_dict = {}
	citation_dict = {}
	index = ""
	for line in file:
		line_parts = line.split()
		if line != "\n" and line_parts[0] == "#index":
			index = line_parts[1]
			reference_dict[index] = 0
		if line != "\n" and line_parts[0] == "#%":
			reference_dict[index] = reference_dict[index] + 1
			if line_parts[1] in citation_dict:
				citation_dict[line_parts[1]] = citation_dict[line_parts[1]] + 1
			else:
				citation_dict[line_parts[1]] = 1

	pub_with_largest_ref = ""
	largest_ref = 0
	for paper_index in reference_list.keys():
		if reference_list[paper_index] > largest_ref:
			largest_ref = reference_list[paper_index]
			pub_with_largest_ref = paper_index

	pub_with_largest_cit = ""
	largest_cit = 0
	for paper_index in citation_list:
		if citation_list[paper_index] > largest_cit:
			largest_cit = citation_list[paper_index]
			pub_with_largest_cit = paper_index

	print("Publication with largest number of references: " + pub_with_largest_ref)
	print("Publication with largest number of citations: " + pub_with_largest_cit)


def calculate_impact_factor():
	path = "AP_train.txt"
	venu_citation_count_dict = {}
	file = open(path, 'r')
	index_venu_dict = create_index_venu_dict(path)
	for line in file:
		line_parts = line.split()
		if line != "\n" and line_parts[0] == "#%":
			index = line_parts[1]
			if index in index_venu_dict:
				venu = index_venu_dict[index]
				if venu in venu_citation_count_dict:
					venu_citation_count_dict[venu] = venu_citation_count_dict[venu] + 1
				else:
					venu_citation_count_dict[venu] = 1

	max_citation_count = 0
	highest_impact_factor_venu = ""
	for venu in venu_citation_count_dict.keys():
		if venu_citation_count_dict[venu] > max_citation_count:
			max_citation_count = venu_citation_count_dict[venu]
			highest_impact_factor_venu = venu
	

	print("Venu with highest impact factor: " + highest_impact_factor_venu)
	
def create_index_venu_dict(path):
	file = open(path, 'r')
	index_venu_dict = {}
	for line in file:
		line_parts = line.split()
			
		if line != "\n":
			if line_parts[0] == "#index":
				index = line_parts[1]
			if line_parts[0] == "#c":
				index_venu_dict[index] = line.replace('#', '').replace('c', '', 1).strip() 

	return index_venu_dict


# def yearwise_pub_list():
# 	file = open("AP_train.txt", 'r')

# 	year_pub_dict = {}
# 	for line in file:
# 		line_parts = line.split()
# 		if line != "\n":
# 			if line_parts[0] == "#*":
# 				paper_title = line_parts[1]
# 			if line_parts[0] == "#t":
# 				year = line_parts[1]
# 				if year in year_pub_dict:
# 					year_pub_dict[year].append(paper_title)
# 				else:
# 					year_pub_dict[year] = [paper_title]

# 	for year in year_pub_dict.keys():
# 		print(year + ": " + str(len(year_pub_dict[year])))

#number_of_publication_per_venu()
#number_of_references_and_citations()
#calculate_impact_factor()
#yearwise_pub_list()
main()