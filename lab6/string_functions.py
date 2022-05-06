#defines several functions. each function re-implements python's built-in string methods

def main():
	#testing 1. my_compare
	print("testing 1. my_compare")
	nameA = "squash"
	nameB = "moonie"
	nameC = "ace"
	nameD = "aly"
	#nameA > nameB (nameA is alphatically more than nameB)
	#nameC < nameD (nameC is alphabetically less than nameD)
	result = my_compare(nameA, nameB)
	result2 = my_compare(nameC, nameD)
	print("result of comparison 1, between", nameA, "and", nameB, "is:", result)
	print("result of comparison 2, between", nameC, "and", nameD, "is:", result2)

	#testing 2. is_char_in
	print("\ntesting 2. is_char_in")
	textRV = "red velvet"
	characterA = "a"
	characterE = "e"
	result = is_char_in(textRV, characterA)
	result2 = is_char_in(textRV, characterE)
	print(characterA, " is in ", textRV, ": ", result, sep='')
	print(characterE, " is in ", textRV, ": ", result2, sep='')

	#testing 3. is_char_not_in
	print("\ntesting 3. is_char_not_in")
	result = is_char_not_in(textRV, characterA)
	result2 = is_char_not_in(textRV, characterE)
	print(characterA, " is not in ", textRV, ": ", result, sep='')
	print(characterE, " is not in ", textRV, ": ", result2, sep='')

	#testing 4. my_count
	print("\ntesting 4. my_count")
	textMMM = "mamamoo"
	characterM = "m"
	characterZ = "z"
	result = my_count(textMMM, characterM)
	result2 = my_count(textMMM, characterZ)
	print("number of times ", characterM, " is in ", textMMM, ": ", result, sep='')
	print("number of times ", characterZ, " is in ", textMMM, ": ", result2, sep='')

	#testing 5. my_endswith
	print("\ntesting 5. my_endswith")
	characterO = "o"
	characterQ = "q"
	result = my_endswith(textMMM, characterO)
	result2 = my_endswith(textMMM, characterQ)
	print(textMMM, " ends with ", characterO, ": ", result, sep='')
	print(textMMM, " ends with ", characterQ, ": ", result2, sep='')

	#testing 6. my_find
	print("\ntesting 6. my_find")
	textW = "wendy"
	characterN = "n"
	result = my_find(textW, characterN)
	print("the index of", characterN, "in", textW, "is", result)

	#testing 7. my_replace
	print("\ntesting 7. my_replace")
	text = "no regrets"
	result = my_replace(text, characterE, characterA)
	print("replace every", characterE, "in", text, "with", characterA)
	print("result:", result)

	#testing 8. my_upper
	print("\ntesting 8. my_upper")
	result = my_upper(textMMM)
	print("return", textMMM, "in all uppercase")
	print("result:", result)

	#testing 9. my_lower
	print("\ntesting 9. my_lower")
	textRV = "RED VELVET"
	result = my_lower(textRV)
	print("return", textRV, "in all lowercase")
	print("result:", result)

	#testing extra credit 10. my_title
	print("\ntesting extra credit 10. my_title")
	text = "i liKE REd veLVet and mAmAMoo"
	result = my_title(text)
	print("return", text, "properly capitalized")
	print("result:", result)


#takes two strings as parameters (str1, str2)
#returns a -1 if str1 is alphabetically less than str2
#returns a 0 if str1 is alphabetically equal to str2
#returns a 1 if str1 is alphabetically greater than str2
def my_compare(str1, str2): 
	if str1 < str2:
		return -1
	elif str1 == str2:
		return 0
	elif str1 > str2:
		return 1

#takes a string and a character as parameters
#returns True if the character is in the string or False if it is not
def is_char_in(string, char): 
	if char in string:
		return True
	else:
		return False

#takes a string and a character as parameters
#returns True if the character is NOT in the string or False if it is
def is_char_not_in(string, char): 
	if char not in string:
		return True
	else:
		return False

#takes a string and a character as parameters
#returns an integer count for each occurrence of the character
#ex: if the function takes in 'abracadabra' and  'a', the function should return 5
def my_count(string, char): 
	count = 0
	for letter in string:
		if letter == char:
			count += 1
	return count

#takes a string and a character as parameters
#returns True if the character is the last character in the string or False if it is not #ex: if function takes in 'quartz' and 'z', the function should return True. if function takes in 'quartz' and 'q', the function should return False
def my_endswith(string, char): 
	if string[-1] == char:
		return True
	else: 
		return False

#takes a string and a character as parameters
#returns the first index from the left where the character is found
#if it does not find the character, return -1
#ex: if the function takes in ‘programming’ and ‘g’, it should return 3
#do not use str.find() for this
def my_find(string, char): 
	index = 0
	for letter in string:
		if letter == char:
			return index
		else:
			index += 1
	return index

#takes a string and two characters (char1 and char2) as parameters
#returns a string with all occurrences of char1 replaced by char2
#ex: if the string is ‘bamboozle’ and char1 is ‘b’ and char2 is ‘t’ then your function should return ‘tamtoozle’
def my_replace(string, char1, char2): 
	text = ""
	for letter in string:
		if letter == char1:
			text += char2
		else:
			text += letter
	return text



#takes a string as a parameter
#returns it as a string in all uppercase
#ex: 'victory' would be 'VICTORY'
#hint: use the ord(c) function to get the ASCII / Unicode code-point. for example, ord('a') returns the integer 97. 
#use chr(i) function to convert an integer back to a character. for example, chr(97) returns the string 'a'. 
#you cannot use the built-in string function str.upper() for this
#you do not have to test for mixed upper and lower case characters, such as ‘Victory’
#index of "a" = 97, index of "A" = 65. difference of 32
#unicode index of spaces = 32
def my_upper(string): 
	uppercase = 0
	text = ""
	for letter in string:
		#lowercase unicode index ranges from 97 ("a") to 122 ("z")
		#uppercase variable = subtracts 32 from lowercase unicode in order to get uppercase
		if ord(letter) >= 97 and ord(letter) <= 122:
			uppercase = ord(letter) - 32
			text += chr(uppercase)
		else:
			text += letter
	return text	

#takes a string as a parameter
#returns it as a string in all lowercase
#hint: similar to the previous item, use ord() and chr().
#do not use str.lower() for this
#you do not have to test for mixed upper and lower case characters, such as ‘Victory’
#index of "a" = 97, index of "A" = 65. difference of 32
#unicode index of spaces = 32
def my_lower(string):
	lowercase = 0
	text = ""
	for letter in string:
		#uppercase unicode index ranges from 65 ("A") to 90 ("Z")
		#lowercase variable = add 32 to uppercase unicode in order to get lowercase
		if ord(letter) >= 65 and ord(letter) <= 90:
			lowercase = ord(letter) + 32
			text += chr(lowercase)
		else:
			text += letter
	return text

#takes a string
#returns a string with the first character capitalized for every word
#ex: if the input to the function is "I like Python a lot", the function should return the string "I Like Python A Lot"
#test this for examples like “I like PYthon a lOt”
#why did i spend this much effort for five points ._.
def my_title(string):

	indexCharacter = 0
	characterUnicode = 0
	wordList = []
	word = ""
	
	#splits the given string at every space into a list of words
	#for each character in the given string
	for character in string:
		#if the character in the string is not a space
		if ord(character) != 32: #unicode index of spaces = 32
			#adds the character to word variable
			word += character
			#if the character is the last in the string
			if indexCharacter == (len(string)-1):
				#adds word variable to wordList
				wordList.append(word)
		#if the character in the string is a space
		elif ord(character) == 32:
			#adds word variable to wordList
			wordList.append(word)
			#clear word
			word = ""
		#adds 1 to indexCharacter
		indexCharacter += 1

	indexLetter = 0
	indexList = 0
	uppercase = 0
	lowercase = 0
	completeWord = ""
	finalText = ""

	#for each word in the list
	for word in wordList:
		#for each letter in the word
		for letter in word:

			#if the letter is the first in the word and it is lowercase
			if indexLetter == 0 and (ord(letter) >= 97 and ord(letter) <= 122):
				#capitalize it
				uppercase = ord(letter) - 32
				#add to completeWord
				completeWord += chr(uppercase)
				#clear uppercase afterwards
				uppercase = 0
				indexLetter += 1

			#if the letter is the first in the word and it is uppercase
			elif indexLetter == 0 and (ord(letter) >= 65 and ord(letter) <= 90):
				#leave as is; add to completeWord
				completeWord += letter
				indexLetter += 1

			#if the letter is uppercase
			elif ord(letter) >= 65 and ord(letter) <= 90:
				#make it lowercase
				lowercase = ord(letter) + 32
				#add lowercase to completeWord
				completeWord += chr(lowercase)
				#clear lowercase afterwards
				lowercase = 0
				indexLetter += 1

			#otherwise add the letter to completeWord
			else:
				completeWord += letter
				indexLetter += 1

		finalText += completeWord

		#if the word in wordList is not the last in the list, add a space to finalText
		#this means there will be a space after every word except for the last word
		if indexList != (len(wordList)-1):
			finalText += " "

		#plus 1 to index for wordList
		indexList += 1
		#clears completeWord and indexLetter
		completeWord = ""
		indexLetter = 0

	return finalText


main()