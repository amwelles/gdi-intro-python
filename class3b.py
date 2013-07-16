from helpers import generate_cleaned_lines

def is_word_in_file(word, filename):
    result = 'that word was not found'
    for line in generate_cleaned_lines(filename):
        # line will be a string of each line of the file in order
        # Your code goes here. Do something with the word and line variables
        if word in line:
        	result = 'that word was found!'
        	break
    print result

input_word = raw_input("Enter a word to search for: ")
answer = is_word_in_file(input_word, 'pride.txt')
# Display the answer in some meaningful way