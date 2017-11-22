import sys
import random
import os

age = 22

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