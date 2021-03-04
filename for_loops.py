'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). 
This is less like the for keyword in other programming languages, and works more like an iterator method as found in 
other object-orientated programming languages.
'''

#This for loop will print 'hello world' 20 times!

for i in range(20):
	print('Hello World!')

'''
A simple exercise: all numbers from 1 - hundred divisible by 3 are going to be replaced with 'Fizz'
All numbers divisible by 5 are going to be replaced with 'buzz'
All numbers divisible by both 3 and 5 are going to be replaced with 'FizzBuzz'
The rest of the numbers are going to stay the same
I will do this using a for loop.
'''

for i in range(1,101):
	if i % 5 == 0 and i % 3 == 0:
		print('Fizzbuzz')
	elif i % 5 == 0:
		print('buzz')
	elif i % 3 == 0:
		print('Fizz')
	else:
		print(i)

# For loops also a more pythonic way of doing things. For instance this while loop:

word = 'thud'
offset = 0
while offset < len(word):
	print(word[offset])
	offset += 1

# or we can do the same thing using a for loop but in a more pythonic way compared to a while loop:

for letter in word:
	print(letter)

# cancelling with break. (if letter == u break)

for letter in word:
	if letter == 'u':
		break
	print(letter)

'''
Inserting a continue in a for loop jumps to the next iteration of the loop, as it does for a while loop
'''

# Check break Use with else

'''
Similar to while, for has an optional else that checks whether for completed normally. If break was not
called, the else statement is run. This is useful when you want to verify that the previous loop ran to 
completion instead of being stopped early with a break. 
'''

# Example:

for letter in word:
	if letter == 'x':
		print('An x was found')
		break
	print(letter)
else:
	print('No x was found')

# The range function

'''
The range() function return as stream of numbers with in a specified range (eg. range(1,100))
'''

# Example:

for x in range(0,3):
	print(x)

# We can use range to print a list of numbers aswell

print(list( range(0,3) ))


# Other uses of range

# Will count down from 2

for x in range(2, -1, -1):
	print(x)

# Even numbers from 0 to 10 (the last number in the range function is the number that the list goes up by)

print(list(range(0, 11, 2)))

# Excercises:

# 11 lines of code - works but not efficient

guess_me = 7
num = 1
while True:
	if num < guess_me:
		print('Too low!')
	elif num == guess_me:
		print('Found it!')
		break
	elif num > guess_me:
		print('Oops!')
		break
	num += 1

# 8 lines of code - works and is effecient and more pythonic than using a while loop

guess_me = 5
for number in range(10):
	if number < guess_me:
		print('Too low!')
	elif number == guess_me:
		print('Found it!')
		break
	elif number > guess_me:
		print('Oops!')
		break

