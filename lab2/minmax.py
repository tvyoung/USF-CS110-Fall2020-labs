#program takes input from the user until the user enters a -1. When the user enters a -1, display the minimum value and the maximum value entered by the user up to that point

#asks user for a number
number = int(input("please enter a number or enter -1 to end: "))

#creates minimum and maximum variables, sets them both to the user's input
minimum = number
maximum = number

#continues askins for numbers as long as user does not input -1
while number != -1:
	#if the user's new input value is smaller than the minimum, the new input value will become the minimum 
	if number < minimum: 
		minimum = number
	#if the user's new input value is larger than the maximum, the new input value will become the maximum
	elif number > maximum:
		maximum = number
	#asks the user to input another number
	number = int(input("please enter a number or enter -1 to end: "))

#prints the minimum and maximum numbers
print("the minimum value:", minimum)
print("the maximum value:", maximum)



#draft version 1
'''number1 = int(input("please enter a number: "))
minimum = number1
maximum = number1
number2 = number1
while number2 != -1 and number1 != -1:
	if number2 < minimum: 
		minimum = number2
	elif number2 > maximum:
		maximum = number2
	number2 = int(input("please enter a number: "))

print("the minimum value:", minimum)
print("the maximum value:", maximum)'''