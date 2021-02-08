#!/usr/bin/env Python3

"""

continuation of ex1

how to start?
        - add loop to verify age of user
        - if is younger than fifty display different message than in ex1
        - if is elder than fifty display age of user
        - change some variables from int to str
        - correct year variable to birth_year
        - make other corrections in your code
"""


from datetime import datetime

name = input("What is your name?: ")
birth_year = int(input("What year you were born?: "))
hundred = (birth_year + 100)

print("Hi " + name + ". \nYou will be 100 years old in " + str(hundred) + " year.")

today = str(datetime.today())
time_now = (today[11:16])

current_year = int(today[:4])
fifty = (50 - (current_year - birth_year))

if (current_year - birth_year) > 50:
    print("You are " + str(current_year - birth_year) + " years old")
    # older than 50
elif (current_year - birth_year) < 50:
    print("You will turn 50th birthday in " + str(fifty) + " year(s) from now.")
    # younger than 50
elif (current_year - birth_year) == 50:
    print("Wow, you are 50! You are so lucky. Beautiful age.")
    
    
print("Today we have beautiful day and clock shows: " + time_now)
