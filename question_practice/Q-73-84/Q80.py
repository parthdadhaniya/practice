# Q80. Print the following pattern. (Do on your own)

"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
