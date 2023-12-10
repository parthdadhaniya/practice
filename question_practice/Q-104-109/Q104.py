"""
Q104. Write a program that prompts the user to specify the length of a list and then requests numbers to populate that list. Display the final list as the output.
"""

lenth = int(input("Enter a lenth : "))

my_list = []

for i in range(lenth):
    number = int(input("Enter a number : "))
    my_list.append(number)
print(my_list)
