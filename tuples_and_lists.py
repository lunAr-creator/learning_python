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
