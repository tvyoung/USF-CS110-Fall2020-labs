#reads in US_Constitution.txt and displays a list of all the unique words found in the file
#i.e it displays every word in the file once
#if there is a duplicate of the same word, the duplicate cannot be displayed
#only need to use 1 list (to work with the file) and 1 set

infile = open("US_Constitution.txt", "r")

#for testing
#infile = open("fic_test.txt", "r")

#reads file as one giant string
text = infile.read()

#creates the list wordList by splitting text string into a list of words
wordList = text.split()

#strip all the words of commas, newlines, semicolons etc and convert all words into lower case.
#hint: you can use strip() multiple times e.g. astring.strip(something).strip(something) etc.
#for each word (index) in len(wordList) (length of list)
for word in range(len(wordList)):
	#strip of commas, semicolons, colons, and periods
	#(replace each given with nothing)
	wordList[word] = wordList[word].strip(",")
	wordList[word] = wordList[word].strip(";")
	wordList[word] = wordList[word].strip(":")
	wordList[word] = wordList[word].strip(".")

	#strip of quotation marks, en dashes, and parentheses
	#(replace each given with nothing)
	wordList[word] = wordList[word].strip('"')
	wordList[word] = wordList[word].strip("—")
	wordList[word] = wordList[word].strip("(")
	wordList[word] = wordList[word].strip(")")

	#strip newlines from the end of each line, lowercase all alphabetic characters
	wordList[word] = wordList[word].rstrip("\n")
	wordList[word] = wordList[word].lower()

#pass wordList to wordSet
wordSet = set(wordList)

#for testing
#print(wordList)
#print(wordSet)

#print each unique word out on a newline (with no duplicates). the words do not need to be ordered.
for word in wordSet:
	print(word)

#close infile
infile.close()