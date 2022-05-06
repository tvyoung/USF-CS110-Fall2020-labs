#reads the contents of the given two files into two separate lists
#strip the elements of each list of the newline.
#user should be able to enter a boy’s name, a girl’s name, or both, and the application will display messages indicating whether the names were among the most popular.

infile1 = open("BoyNames.txt", "r")
infile2 = open("GirlNames.txt", "r")

boyNames = infile1.readlines()
girlNames = infile2.readlines()

infile1.close()
infile2.close()

#strip \n from each element in boyNames list
index = 0
while index < len(boyNames):
	boyNames[index] = boyNames[index].rstrip("\n")
	index += 1

#strip \n from each element in girlNames list
index = 0
while index < len(girlNames):
	girlNames[index] = girlNames[index].rstrip("\n")
	index += 1

#case sensitive
#asks user to input a boy's name, a girl's name, or both
searchBoy = input("enter a boy's name, or N if you do not wish to enter a boy's name: ")
searchGirl = input("enter a girl's name, or N if you do not wish to enter a girl's name: ")

if searchBoy == "N":
	print("you chose not to enter a boy's name.")
elif searchBoy in boyNames:
	print(searchBoy, "is one of the most popular boy's names.")
else:
	print(searchBoy, "is not one of the most popular boy's names.")

if searchGirl == "N":
	print("you chose not to enter a girl's name.")
elif searchGirl in girlNames:
	print(searchGirl, "is one of the most popular girl's names.")
else:
	print(searchGirl, "is not one of the most popular girl's names.")