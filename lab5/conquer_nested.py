#prints out the sum of each row of a 3x3 grid represented in a nested list using a nested for loop by item only
#use a nested for loop by item and use both target variables 

import random

def main(): 
	#creates 3x3 nested list example used for the program
	nestedList1 = [[4, 9, 2],
				  [3, 5, 7], 
				  [8, 1, 6]]

	#creates second 3x3 nested list example used for the program
	nestedList2 = [[1, 3, 8],
				   [2, 4, 6], 
				   [7, 9, 0]]

	#fills in each index of the 3x3 nested list with random numbers ranging from 0 to 10
	'''for rows in range(len(nestedList)):
		for columns in range(len(nestedList[rows])):
			nestedList[rows][columns] = random.randint(0,10)'''

	printList(nestedList1)
	findSum(nestedList1)

	printList(nestedList2)
	findSum(nestedList2)

#prints out the given 3x3 nested list
def printList(list):
	print("for the 3x3 grid represented by:")
	print(list[0])
	print(list[1])
	print(list[2])

#finds the sum of each sub-list in the given 3x3 nested list
#returns the total sum of each sub-list
def findSum(list):
	#creates rowNumber variable to tally each row
	rowNumber = 0
	#creates total variable to store the sum of each sub-list
	total = 0

	#finds the sum of each sub-list in nestedList by ITEM
	for rows in list:
		for columns in rows:
			 total += columns
		print("row", rowNumber, "total is:", total)
		total = 0
		rowNumber += 1

main()