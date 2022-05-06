#initializes (hardcodes, no user input required) the list of numbers that you come up with (10 or so should do) and the number n
#displays the original list and the number n. then displays the list of numbers smaller than n by calling smaller_than_n_list() and displaying the returned results.
def main():
	listA = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
	print("list A is the following:", listA)
	n = 10
	print("the value of variable n is the following:", n)
	listB = smaller_than_n_list(listA, n)
	print("the numbers in list A that are smaller than n are the following:", listB)


#accepts two arguments: an input_list, and a number n
#returns a list of all of the numbers in the input_list that are less than the number n
def smaller_than_n_list(input_list, n):
	new_list = []
	for index in input_list:
		if index < n:
			new_list.append(index)
	return new_list

main()