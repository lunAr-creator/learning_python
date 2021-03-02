'''
Loops are used repeat a certain action multiple times. Python gives us two options for this: while and for
'''

#This loop will print the numbers 1-5 because every time the loop is run (until count = 5) 1 is added to count

count = 1
while count <= 5:
	print(count)
	count += 1

#Cancelling a loop using break

while True:
	stuff = input('String to capitalize [type e to exit]: ')
	if stuff == 'e':
		break
	print(stuff.capitalize())

#Sometimes, you dont want to break out of a loop but want to skip ahead to the next iteration. We can do this using the 'continue' keyword. 

while True:
	stuff = input('Integer [type e to exit]: ')
	if stuff == 'e': # quit
		break
	num = int(stuff)
	if num % 2 == 0: # an even number
		continue
	print(f'{num} squared is {num*num}')

'''
If the while loop enden normally (no break), control passes to an optional else. You use this when youve coded
a while loop to check for something, and breaking as soons as its found. 
'''

numbers = [1, 3, 5]
position = 0
while position < len(numbers):
	number = numbers[position]
	if number % 2 == 0:
		print(f'Found even number {number}')
	position +=1
else:
	print('No even numbers found')

'''
Expected Output:

1
2
3
4
5
String to capitalize [type e to exit]: w
W
String to capitalize [type e to exit]: e
Integer [type e to exit]: 5
5 squared is 25
Integer [type e to exit]: e
Found even number 6
'''

'''
Next file will be about for loops
'''