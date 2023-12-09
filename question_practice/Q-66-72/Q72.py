# Q72. Ask N from user. N means number of lines. Then print the following pattern. (Do on your own)

"""
6 6 6 6 6
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""

number = int(input("Enter a number : "))

for i in range(number, 0, -1):
    for j in range(number, 1, -1):
        print(i, end=" ")
    print()
