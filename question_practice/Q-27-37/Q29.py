"""
Q29. Write a program to print the last digit of a number. (NOT A IF ELSE QUESTION)
Example 1
Input: 45321 Output: 1
Example 2
Input: 459094 Output: 4
"""

number = int(input("Enter a number : "))

last_number = number % 10

print("last_number: ", last_number)
