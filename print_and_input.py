# Learning Python 1 - print and input

'''
The builtin print function allows us to print a string, or any other object (the object will be converted into a string)
to a shell, commandline or any other application that allows python to do that. 
'''

# An example of using a print function:
print('Hello World!')

#We can also print variables by referencing them without quotes in the print function:
var = 'Hello World!'
print(var)

# We can aslo add variables AND a string into a print function like so (they must be separated by an equals sign or a plus sign - + or =):
var = 'Hello'
print(var,'World!')

#We can also print var twice without having to write print again by just adding a '*2' (which will print it 2 times - this can be any number)
var = 'Hello World!'
print(var*2)

#String formatting - we can use string formatting which means that we dont have to add a '+' or ',' when separating variables from other strings or objects:
var = 'Hello World!'
print(f'My message is {var}')

'''
The builtin input function lets you ask the user for input. You can also call this function and wait for the user to pree the key
in the description.  
'''

#Here is an example using input to say a greeting after recieving the users name:
var = input('What is your name?: ')
print('Hello',var)

# or using string formatting:

var = input('What is your name?: ')
print(f'Hello {var}')

'''
Next time we will use our newly learnt built in funtions (print and input) with if, elif and else statments! :D
'''
