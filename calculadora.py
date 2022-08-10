def calculate():
	operation=input('''Please type in the math operation you would like to complete:
	+ for addition
	- for subtraction 
	* for multiplication
	/ for division
	''')

	number_1 = int(input('Enter your first number: ')) 
	number_2 = int(input('Enter your second number: '))

	if operation== '+':
		# Sum
		print (f'{number_1} + {number_2} = {number_1+number_2}')
	elif operation== '-':
		# Subtraction
		print (f'{number_1} - {number_2} = {number_1-number_2}')
	elif operation== '*':
		#Multiplication 
		print (f'{number_1} * {number_2} = {number_1*number_2}')
	elif operation== '/':
		# Division
		print (f'{number_1} / {number_2} = {number_1/number_2}')
	else:
		print('wrong operation, run again!')
	again()
def again():
	x=input('Again? (Y/N)')
	if x.upper()=='Y':
		calculate()
	else:
		print('Ok, então!')
calculate()