from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
	i = 0
	lines_found = []
	for line in generate_cleaned_lines(filename):
		i += 1
		# line will be a string of each line of the file in order
		# Your code goes here. Do something with the word and line variables
		if word in line:
			lines_found.append(i)
			# result = 'that word was found on line {0}'.format(i)

	if len(lines_found) > 0:
		print 'your word was found on these lines:'
		print lines_found
		print 'total number of lines that word was found on: {0}'.format(len(lines_found))
		
	else:
		print 'your word was not found :('

# this code ensures that imports don't make this stuff below run
if __name__ == '__main__':
	input_word = raw_input("Enter a word to search for: ")
	answer = is_word_in_file(input_word, 'pride.txt')