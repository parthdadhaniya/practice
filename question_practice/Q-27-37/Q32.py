# Q32. Ask 4 numbers from user. Make sure all the numbers entered by user are dierent. Print which number is the smallest.

number_1 = int(input("Enter a number_1 : "))
number_2 = int(input("Enter a number_2 : "))
number_3 = int(input("Enter a number_3 : "))
number_4 = int(input("Enter a number_4 : "))

if number_1 < number_2 and number_1 < number_3 and number_1 < number_4:
    print("Number 1 is smallest")
elif number_2 < number_1 and number_2 < number_3 and number_2 < number_4:
    print("Number 2 is samllest")
elif number_3 < number_1 and number_3 < number_2 and number_3 < number_4:
    print("Number 3 is samllest")
else:
    print("Number 4 is samllest")
