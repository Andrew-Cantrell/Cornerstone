import sys
import random
import os

# Basic demographics survey with tailored responses. Load into editor and press the run key to initiate survey questions and responses



age = int(input("Enter your age: "))
stateofresidence = type(input("Enter your state of residence i.e. GA, NY, CA: "))
militarystatus = type(input("Did you serve in the military? Y/N: "))
gender = type(input("Please enter your gender. M/F/O: "))

if age >= 21:
    print('You are old enough to drive a car and a commercial vehicle')
elif age >= 16:
    print ('You are old enough to drive a car')
else : print('You are not old enough to drive')

if ((age >=0)and (age<=17)):
    print("You are a minor")
elif(age >=18) and (age<=20):
    print ( 'You are in in the legal majority but you are not old enough to drink')
else : print ( 'Have a drink on me')

if age >= 45:
    print("You're in Generation X")
else : print ("You're not in Generation X")

if militarystatus is "Y":
    print('USA! USA! USA!')
else : print ('You did not serve in the Armed Forces')

if stateofresidence is "GA":
    print ("Georgia's on my mind")

if gender is "m":
    print('Thank you for taking the time to complete this survey, sir.')
elif gender is "f":
    print("Thank you for taking the time to complete this survey, ma'am.")
else : print ("Thank you for taking the time to complete this survey.")
