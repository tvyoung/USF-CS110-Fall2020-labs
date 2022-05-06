#creates the variable choice for user input
choice = 0

#creates variables to store the total number of action figures the user collects
totalWonderwoman = 0
totalThor = 0
totalBatwoman = 0
totalSuperman = 0

#continues to ask the user to pick action figures until they choose to input 5 and exit
while choice != 5:
	#displays the menu and asks the user for input
	print("Welcome to the CS 110 Action FigureShop!")
	print("Which action figure would you like to collect?")
	print("1. Wonderwoman")
	print("2. Thor")
	print("3. Batwoman")
	print("4. Superman") 
	print("5. Exit")
	choice = int(input("Please enter your choice (1-5): "))

	#input validation to check if user input is in the range 1-4. will continue to ask for input from user until one is valid.
	#redisplays the menu and then asks again for input
	while choice < 1 or (choice > 4 and choice !=5):
		print("ERROR: the choice input is invalid.")
		print("Welcome to the CS 110 Action FigureShop!")
		print("Which action figure would you like to collect?")
		print("1. Wonderwoman")
		print("2. Thor")
		print("3. Batwoman")
		print("4. Superman") 
		print("5. Exit")
		choice = int(input("Please enter your choice (1-5): "))

	#asks the user for how many Wonderwomen they want to collect
	if choice == 1:
		amountWonderwoman = int(input("how many Wonderwoman figures would you like to collect? "))
		totalWonderwoman += amountWonderwoman
	#asks the user for how many Thor figures they want to collect
	elif choice == 2:
		amountThor = int(input("how many Thor figures would you like to collect? "))
		totalThor += amountThor
	#asks the user for how many Batwoman figures they want to collect
	elif choice == 3:
		amountBatwoman = int(input("how many Batwoman figures would you like to collect? "))
		totalBatwoman += amountBatwoman
	#asks the user for how many Superman figures they want to collect
	elif choice == 4:
		amountSuperman = int(input("how many Superman figures would you like to collect? "))
		totalSuperman += amountSuperman


print("your total number of collected action figures:")
print("Wonderwoman:", totalWonderwoman)
print("Thor:", totalThor)
print("Batwoman:", totalBatwoman)
print("Superman:", totalSuperman)