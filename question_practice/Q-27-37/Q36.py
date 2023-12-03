# Q36. Take three numbers as input from User and print which one is greater or are they equal.


num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))
num3 = int(input("Enter num3 : "))

if num1 > num2 and num1 > num3:
    print("Num1 is greater")
elif num2 > num1 and num2 > num3:
    print("Num2 is greater")
elif num3 > num1 and num3 > num1:
    print("Num3 is greater")
else:
    print("Equal")
