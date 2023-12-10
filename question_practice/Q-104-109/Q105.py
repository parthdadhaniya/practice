"""
Q105. Create a list and prompt the user for an 'old number' followed by a 'new number.
' If the 'old number' exists in the list, replace it with the 'new number' provided by the user.
"""

my_list = [5, 10, 15, 20, 15]

old_number = int(input("Enter a old number : "))

new_number = int(input("Enter a new number : "))

for i in my_list:
    if i == old_number:
        temp = my_list.index(i)
        my_list[temp] = new_number
print(my_list)
