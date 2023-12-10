# Q95. Make your own list. Print all the elements present at even index position.

my_list = [51, "Anirudh", 85, 91.66, 52, 44, 100, 200]

for i in range(len(my_list)):
    if i % 2 == 0:
        print(my_list[i])
