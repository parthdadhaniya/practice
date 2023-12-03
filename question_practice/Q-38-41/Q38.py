"""
Q38. Write a program that takes three numbers as input and determines the largest one using nested if-else statements. 
Make sure all 3 numbers entered by user are dierent.
"""

num1 = int(input("Enter a num1 :"))
num2 = int(input("Enter a num2 :"))
num3 = int(input("Enter a num3 :"))

if num1 >= num2:
    if num1 >= num3:
        print("Number 1 is greater")
    else:
        print("Number 3 is greater")
else:
    if num2 >= num3:
        print("Number 2 is greater")
    else:
        print("Number 3 is greater")
