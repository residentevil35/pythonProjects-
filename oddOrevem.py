"""
Name: Rachel Coughanour

File: oddOreven.py

Description: Program to ask the user for a number and
then determine if it is odd or even.
"""

num = int(input("Please enter a number: "))

if num % 2 == 0:
    print ("the number is an even number")
elif num % 2 == 1:
    print ( "the number is an odd number")
