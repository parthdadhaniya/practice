# Q30. Write a program to check if the last digit of a number is divisible by 5 or not.

number = int(input("Enter a number : "))

last_digit = number % 10

if last_digit % 5 == 0:
    print("Yes it is divisible by 5")
else:
    print("Not divisible 5")
