#test program

rFile = open("US_Constitution.txt", "r")

text = rFile.read()
wordList = text.split()

for word in range(len(wordList)):
	wordList[word] = wordList[word].strip(".")


print(wordList)