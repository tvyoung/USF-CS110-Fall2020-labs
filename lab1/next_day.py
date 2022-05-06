#gives the date of the next day based on a date provided by the user (year, month, day)

#asks user to input a year, month, and day
year = int(input("input a year: "))
month = int(input("input a month [1-12]: "))
day = int(input("input a day [1-31]: "))

#checks if the given date is valid or not
valid = True

#checks whether it is a leap year
leap_year = False
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0: #if the year is evenly divible by 100 and 400, this is a leap year
			leap_year = True
		else: #if the year is evenly divisble by 100 but not 400, this is not a leap year
			leap_year = False
	else: #if the year is evenly divisble by 4 but not by 100, this is a leap year
		leap_year = True
else: #if the year is not evenly divible by 4, is not a leap year
	leap_year = False


#creates month_length variable
month_length = 0

if month == 1: #january
	month_length = 31
elif month == 2: #february
	if leap_year:
		month_length = 29
	else:
		month_length = 28
elif month == 3: #march
	month_length = 31
elif month == 4: #april
	month_length = 30
elif month == 5: #may
	month_length = 31
elif month == 6: #june
	month_length = 30
elif month == 7: #july
	month_length = 31
elif month == 8: #august
	month_length = 31
elif month == 9: #september
	month_length = 30
elif month == 10: #october
	month_length = 31
elif month == 11: #november
	month_length = 30
elif month == 12: #december
	month_length = 31
else: 
	valid = False
	print("that is not a valid month.")	


#if the day is equal to or greater than the 1st and is less than the last day of the month, adds 1 day
if day >= 1 and day < month_length:
	day += 1
#if the day given is equal to the last day of the month, adds 1 month and resets the day to the 1st
elif day == month_length: 
	day = 1
	month += 1
	#if it is the last day of december, next day will be january 1st and adds 1 year
	if month == 13:
		month = 1
		year += 1
#if the day given does not exist in the given month, doesn't return a date
else:
	valid = False
	print("that is not a valid day of the given month.")


#if the year, month, and day are all valid, will give the next date. otherwise will not given an answer.
if valid:
	if leap_year: #notes if the given year is a leap year
		print("it is a leap year!")
	print("the next date is:", year, month, day)
else:
	print("the given date is not valid.")