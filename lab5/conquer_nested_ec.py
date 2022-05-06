#same as conquer_nested.py finding the sum of rows, but also with finding the sum of columns
#prints out the sum of each row and sum of each column of a 3x3 grid represented in a nested list using a nested for loop by item only

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
	findRowTotals(nestedList1)
	findColumnTotals(nestedList1)

	printList(nestedList2)
	findRowTotals(nestedList2)
	findColumnTotals(nestedList2)

#prints out the given 3x3 nested list
def printList(list):
	print("for the 3x3 grid represented by:")
	print(list[0])
	print(list[1])
	print(list[2])

#finds the sum of each sub-list in the given 3x3 nested list
#returns the total sum of each sub-list
def findRowTotals(list):
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

def findColumnTotals(list):
	#creates columnNumber variable to tally each column
	columnNumber = 0
	#creates total variables for the sum of each column
	total0 = 0
	total1 = 0
	total2 = 0

	#finds the sum of each column in nestedList by ITEM
	for rows in list:
		for columns in rows:
			if columnNumber == 0:
				total0 += columns
			elif columnNumber == 1:
				total1 += columns
			elif columnNumber == 2:
				total2 += columns
			columnNumber += 1
		columnNumber = 0

	#i have no idea how to put the print statements in the nested for loop 
	print("column 0 total is:", total0)
	print("column 1 total is:", total1)
	print("column 2 total is:", total2)
	

main()