# Q108. Generate a list of at least 10 numbers. Then, create two separate lists called 'odd' and 'even.' Put all the odd numbers from the original list into the 'odd' list, and all the even numbers into the 'even' list.


my_list = [3, 8, 12, 17, 22, 30, 35, 41, 48, 50]

even_number = []

odd_number = []

for i in my_list:
    if i % 2 == 0:
        even_number.append(i)
    else:
        odd_number.append(i)
print(even_number)
print(odd_number)
