# Q101. Make your own list. Print how many positive and negative numbers are here. (Do on your own)

my_list = [51, 85, 1748, 52, 44, 100, 200]

positive = 0

negative = 0

for i in my_list:
    if i % 2 == 0:
        positive += 1
    else:
        negative += 1
print(positive)
print(negative)
