# Q83. Print the following pattern. (Do on your own)

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""

counter = 1

for i in range(1, 6):
    for j in range(i - 1):
        print(" ", end=" ")
    for k in range(i):
        print(counter, end=" ")
        counter += 1
    print()
