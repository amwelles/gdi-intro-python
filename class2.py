# parenthesis around predicates are NOT standard (weird)
# prescendence determines which order things are evaluated
# elif = elseif
# no switch/case statement -- could use dictionary

twenty_one = raw_input('are you over 21? (y/n) ')

if twenty_one == 'y':
	print 'you may have a beer!'
	how_many = raw_input('how many beers would you like? ')
	how_many = int(how_many)
	if how_many > 10:
		print 'you got alcohol poisoning. :('
	elif how_many > 3:
		print 'oops, you\'re drunk!'
	elif how_many > 1:
		print 'you got a little tipsy.'
	else:
		print 'so I guess you\'re the designated driver.'
else:
	print 'you may not have a beer.'
	print 'but here, have a glass of juice!'