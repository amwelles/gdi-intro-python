# print 'I am a Python program'

# input_value = raw_input('enter a radius: ')
# radius = float(input_value)
# area = 3.14159 * radius ** 2 # ** means 'to the power of'
# print 'the area of a circle with a radius of '+ input_value +' is:'
# print area

# how do I turn something into a string?
# str(42)

birth_year = raw_input('what year were you born? ')
year = int(birth_year)
age = 2013 - year
minAge = str(age - 1)
age = str(age)
print 'you are either '+ minAge +' or '+ age +' years old'