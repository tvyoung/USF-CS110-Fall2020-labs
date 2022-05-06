#calculates the interest rate for a loan based on the individual's information

INTEREST_RATE = 3.5

#asks user for age, marital status, credit score
age = int(input("what is your age? "))
marital_status = input("are you married? type 'y' or 'n' ")
credit_score = int(input("what is your credit score? "))

#if user is under 25 years of age, adds 1.5 to interest rate
if age < 25:
	INTEREST_RATE += 1.5
#if user is equal to or over 50 years of age, subtracts 0.5 from interest rate
elif age >= 50:
	INTEREST_RATE -= 0.5

print("interest rate after age calculation: ", format(INTEREST_RATE, '.2f'), '%', sep='')

#if user is married, decreases their interest rate by 0.75
if marital_status == 'y':
	INTEREST_RATE -= 0.75

print("interest rate after marital status calculation: ", format(INTEREST_RATE, '.2f'), '%', sep='')

#if user's credit score is less than 550, adds 2.5 to their interest rate
if credit_score < 550:
	INTEREST_RATE += 2.5
#if user's credit score is equal to or greater than 550 and less than 650, adds 1.5 to their interest rate
elif credit_score >= 550 and credit_score < 650:
	INTEREST_RATE += 1.5
#if user's credit score is equal to or greater than 650, reduces their interest rate by 0.5
elif credit_score >= 650:
	INTEREST_RATE -= 0.5

#displays final interest rate
print("the final interest rate is ", format(INTEREST_RATE, '.2f'), '%', sep='')