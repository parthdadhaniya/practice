# Q28. Write a program to check if number is divisible by 2 and 3 but not 8.

number = int(input("Enter a number : "))

if number % 2 == 0 and number % 3 == 0 and number % 8 != 0:
    print("Number divisible by 2 and 3 but not 8")
else:
    print("No")
