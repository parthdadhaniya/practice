# Q102. Make your own list. Print the largest number present in that list.

my_list = [51, 85, 1748, 52, 44, 100, 200]

largest_number = my_list[0]

for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] > largest_number:
        largest_number = my_list[i]
print(largest_number)
