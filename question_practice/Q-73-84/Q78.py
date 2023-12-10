# Q78. Print the following pattern. (Do on your own)

"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
