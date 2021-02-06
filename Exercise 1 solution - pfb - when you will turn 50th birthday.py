#!/usr/bin/env Python3

"""

simple script to ask user about name and year of birth
as result you will tell user:
        - when will turn 100 years,
        - how many years left to be 50 years old
        - what time is now

how to start?
        - first you need 2 variables name and year and convert them for user input
        - next you need to convert year of birth and do a simple math ex
        - display 1st info to the user when will turn 100 y old
        - next you need a date, current year, you need to convert date to see only year in YYYY format and
          only hour in HH:MM format
        - next calculate how many years is left to be 50 y old
        - display info to the user
        - display current time
"""


from datetime import datetime

name = input("What is your name?: ")
year = int(input("What year you were born?: "))
hundred = str(year + 100)

print("Hi " + name + ". \nYou will be 100 years old in " + hundred + " year.")

today = str(datetime.today())
# single line comment
# print(today)
time_now = (today[11:16])
#print(time_now)

current_year = int(today[:4])
fifty = str(50 - (current_year - year))

print("You will turn 50th birthday in " + fifty + " year(s) from now.")
print("Today we have beautiful day and clock shows: " + time_now)
