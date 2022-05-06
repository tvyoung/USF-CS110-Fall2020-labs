#only searches for girls’ names and loops until the user types ‘exit’

infile = open("GirlNames.txt", "r")
girlNames = infile.readlines()
infile.close()

index = 0
while index < len(girlNames):
	girlNames[index] = girlNames[index].rstrip("\n")
	index += 1


searchGirl = input("enter a girl's name, or 'exit' if you do not wish to enter a girl's name: ")
searchHistory = []

while searchGirl != "exit":
	if searchGirl in girlNames:
		print(searchGirl, "is one of the most popular girl's names.")
	else:
		print(searchGirl, "is not one of the most popular girl's names.")
	searchHistory.append(searchGirl)
	searchGirl = input("enter another girl's name, or 'exit' if you do not wish to enter a girl's name: ")

#creates a list of all the names that the user searched for (regardless of whether they were popular or not) and writes that list to a separate .txt file called NamesSearched.txt.
outfile = open("NamesSearched.txt", "w")
for index in searchHistory:
	outfile.write(index + "\n")

outfile.close()


