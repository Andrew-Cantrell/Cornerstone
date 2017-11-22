import sys
import random
import os

# Basic demographics survey with tailored responses

age = 25
militarystatus = 'n'


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

if militarystatus == 'y':
    print('USA! USA! USA!')
else : print ('You did not serve in the Armed Forces')

if stateofresidence == 'GA':
    print ("Georgia's on my mind")

if gender == 'm':
    print('Thank you for taking the time to complete this survey, sir.')
elif gender == 'f':
    print("Thank you for taking the time to complete this survey, ma'am.")
else : print ("Thank you for taking the time to complete this survey.")