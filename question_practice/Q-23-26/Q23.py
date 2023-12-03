# Q23. Write a Python program that takes an integer input and prints whether it's positive, negative. (Consider 0 as positive)


number = int(input("Enter number : "))

if number % 2 == 0:
    print("POSITIVE")
else:
    print("NEGATIVE")
