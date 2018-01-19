import sys

def create_arff():
	if len(sys.argv) == 1:
		print("Usage: kosarak.py [___.dat]")
		exit()

	output_file = open("kosarak.arff", "w")
	input_file = open(sys.argv[1], "r")

	numbers = []
	for line in input_file:
		numbers_in_line = line.split()
		numbers.extend(numbers_in_line)
		
	numbers = map(int, numbers)

	max_number = max(numbers)

	output_file.write("@RELATION clicks\n")

	for number in range(1, max_number + 1):
		line = "@ATTRIBUTE i" + str(number) + " {0, 1}\n"
		output_file.write(line)
	
	input_file = open(sys.argv[1], "r")

	output_file.write("@DATA\n")
	for line in input_file:
		numbers = line.split()
		numbers = list(set(map(int, numbers)))
		numbers.sort()
		output_line = "{"
		for number in numbers:
			output_line += str(number-1) + " 1, "
		output_line = output_line[:-2]
		output_line += "}\n"
		output_file.write(output_line)
	


	output_file.close()



create_arff()