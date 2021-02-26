'''
A program sometimes may have to make choices. These choices can execute different code depending on certain condition.
'''

# Here i am going to print bigger or smaller depending on the number the user inputs:

x = 4
var = int(input('Number: '))
if var < x:
	print(f'The number {var} is smaller than the number {x}')
elif var == x:
	print(f'The number {var} is equal to the number {x}')
else:
	print(f'The number {var} is bigger than the number {x}')

#Here is a login system that asks for a password. If the password does not equal the set password, you are not allowed access. 

password = 'hello1234'
password_input = str(input('Password: '))
if password_input == password:
	print('Correct Password!')
else:
	print('Incorrect Password!')


#This program will ask you a maths question. If it is correct it will return Correct answer, if not Incorrect answer. 

a = 4
b = 6
question = int(input(f'What is {a} + {b}? '))
if question == a+b:
	print('Correct Answer!')
elif question != a+b:
	print(f'Incorrect Answer! The answer was {a+b}')


'''
Expected output:

Number: 5
The number 5 is bigger than the number 4
Password: hello1234
Correct Password!
What is 4 + 6? 10
Correct Answer!
'''