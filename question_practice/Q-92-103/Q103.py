# Q103. Make your own list. Print the smallest number present in that list. (Do on your own)

my_list = [51, 85, 1748, 52, 44, 100, 200]

smallest_number = my_list[0]

for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] < smallest_number:
        smallest_number = my_list[i]
print(smallest_number)
