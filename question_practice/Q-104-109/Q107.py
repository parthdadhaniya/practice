"""
Q107. Ask the user for a number. Then, from a list of numbers, remove all the numbers that can be divided by the number the user entered. (Do on your own).
"""

my_list = [11, 21, 30, 50, 60]

number = int(input("Enter a number : "))

for i in my_list:
    if i % number == 0:
        my_list.remove(i)
print(my_list)
