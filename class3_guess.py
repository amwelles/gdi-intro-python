# importing thing to make random number
from random import randint

# this is the answer
answer = randint(1, 10)

def reply(guess):
	my_guess = int(guess)
	if my_guess == answer:
		return 'you were right! the answer is '+ str(answer) +'.\n' + \
		'you get a gold star!'
	elif my_guess > answer:
		return 'oops, too high!'
	elif my_guess < answer:
		return 'oops, too low!'
	else:
		return 'error. :('

print 'type "quit" at any time to quit.'

while True:
	# this is the guess
	user_guess = raw_input('guess a number between 1 and 10 (inclusive): ')
	if user_guess == 'quit':
		break
	else:
		response = reply(user_guess)
		print response
