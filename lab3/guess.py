'''generates a random number in the range of 1 through 20, and asks the user to guess what the number is
If the user guesses the number, the application should congratulate the user and generate a new random number so the game can start over. If the user enters 0, they can exit out of the game.'''
import random

def main():
	#creates variable repeat. determines whether the game will repeat or not depending on if repeat = 0
	repeat = 21
	print("starting the guessing game!")
	while repeat != 0:
		#Generates random number from 1 to 20
		number = random.randint(1, 20)
		#for testing
		#print("for testing, the answer is:", number)
		#runs the guessing game function. if the guessing game function does not return 0, will generate a new number and repeat. 
		repeat = playGuessingGame(number)

def playGuessingGame(number):
	#creates variable guess
	guess = 25
	#will continue to loop as long as user does not enter 0 or the correct answer
	while guess != 0 and guess != number:
		#asks the user to guess the number
		guess = int(input("enter a number between 1 and 20, or 0 to quit: "))
		#if user input is greater than the answer
		if guess > number:
			print("too high, try again.")
		#if user input is less than the answer but not zero
		elif guess < number and guess > 0:
			print("too low, try again.")
		#if user input is the answer, congratulates them.
		elif guess == number:
			print("congratulations! you guessed the right number!")
			print("playing the game again.")
			print("a new number has been generated.")
		#if user input = 0, displays exit game message.
		elif guess == 0:
			print("now exiting the game. thanks for playing!")
	#returns the user input when it is either 0 or the correct answer.
	return guess

main()