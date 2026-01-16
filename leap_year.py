#!/usr/bin/env python3

#Check if input is an integer
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#Determine a leap year
user_input = input("Enter a year: ")

while user_input != 'end':
    if is_int(user_input):
        if (int(user_input) % 4 == 0 and int(user_input) % 100 != 0) or (int(user_input) % 400 == 0):
            print(f"{user_input} a leap year!")
        else:
            print(f"{user_input} not a leap year!")
        user_input = input("Enter a year (or 'end' to quit): ")
    else:
        user_input = 'end'
