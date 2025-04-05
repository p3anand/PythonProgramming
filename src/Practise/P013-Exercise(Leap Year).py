'''
Program to determine a given year is a leap year
Leap year is divisible by 4, but not by 100 unless it is also divisible by 400
Use if-else loop

Sample:
Year=2024
Output=Leap Year
'''

year = int(input("Enter year:\n"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a Leap year")
        else:
            print(f"{year} is a not a Leap year")
    else:
        print(f"{year} is a Leap year")
else:
    print(f"{year} is a not a Leap year")

#Concept for leap year
# Each year that is a multiple of 4, except for years
# - evenly divisible by 100 but not by 400
# One line condition
# if((year % 4==0 and year % 100! = 0)) or year % 400 == 0):