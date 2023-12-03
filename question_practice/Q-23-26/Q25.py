# Q25. Write a program that takes two numbers as input and checks if the first number is divisible by the second.

number_1 = int(input("Enter a number 1 : "))
number_2 = int(input("Enter a number 2 : "))

if number_1 % number_2 == 0:
    print("Number is devisible ny number 2")
else:
    print("Number not divisible by number 2")
