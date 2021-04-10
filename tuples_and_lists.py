'''
Python has two other sequence structures: tuples and lists. These contain zero or more elemtns. Unlike
strings, the elements can be of different types. In fact, each element can be any Python object. This lets you create structures
as deep and complex as you like. Tuples are IMMUTABLE and lists are MUTABLE.
'''

#=================================TUPLES=======================================#

# Syntax of a tuple

empty_tuple = () # An example of an empty tuple
hello = ('Hello', ) # Encolse a string in a paranthesis and it will become a tuple
hello2 = 'hi', 'hey', 'hello' # A tuple with one or more elements

# Tuples let you assign multiple variables at once. (this is sometimes called tuple unpacking)

var = ('hi', 'hey', 'hello')
a, b, c = var

# You can use tuples to exchange values in one statment without using a temporary variable:

password = 'hello123'
word = 'keyboard'
password, word = word, password

# Create tuples with tuple()

example_list = ['hi', 'hey', 'hello']
tuple(example_list)

# Iterate with for an in

words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(words)

# Modify a tuple?? YOU CANT!!! THEY ARE IMMUTABLE!!!!

#=================================LISTS=======================================#

'''
Lists are good for keeping track of things by their order, espeially when the order and contents
might change. Unlike string, lists are mutable. You can change a list in place, add new elements 
and delete or replace existing elements. The same value can occur more than once in a list. 
'''

# Create lists with [] (A list's contents are sperated by commas and surrounded by square brackets)

example_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursdar', 'Saturday', 'Sunday']
leap_years = [2000, 2004, 2008]

# Create or convert with list() (you can make a list with the list function)

another_empty_list = list()

# The list function can convert other iterable data types into a list aswell (eg a tuple)

a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)

# CREATE A LIST FROM A STRING WITH SPLIT

day = '1/1/2021'
print(day.split('/'))

# GET AN ITEM FROM A LIST BY OFFSET

# As with strings, you can extract a single value from a list by specifying its offset.

nums = ['1', '2', '3']
for i in range(len(nums)):
	print(nums[i])

print(nums[1]) # will return 2

# GET ITEMS WITH SLICE

# You can extract a subsequence of a list by using slice (a slice of a list is also a list)

nums = ['1', '2', '3', '4']
print(nums[0:3])

# As with strings, slices can step by values other than one. The next example starts and the beginning and goes right by 2:

print(nums[::2])

# Here we go left by 2

print(nums[::-2])

# and finally, a trick to REVERSE A LIST

print(nums[::-1])

# Although, none of these slices changed the nums list itself, because we didnt assign them to nums. To reverse a list in place, we can use list.reverse()

nums.reverse()

# ADD AN ITEM TO THE END OF A LIST WITH APPEND

print(nums)
nums.append(5)
print(nums)