#!/usr/bin/env python3

# Import the random module to generate random numbers
import random

# Define function named greeting
def greeting():
  # Ask user for their name and store it in the variable 'name'
  name = input("Hello!, What's your name?")
  
  # Generate random integer between 1 and 100 (inclusive) and store it in 'number'
  number = random.randint(1,101)
  
  # Print greeting message that includes user's name and their random number
  print("hello " + name + ", your random number is " + str(number))
  
# Call the greeting function to execute it
greeting()
