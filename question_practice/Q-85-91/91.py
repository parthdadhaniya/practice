# Q91. Print the following pattern. (Do on your own)

"""
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""

for i in range(5, 0, -1):
    for j in range(5, i, -1):
        print(" ", end=" ")
    for k in range((i * 2) - 1):
        print("*", end=" ")
    print()
for i in range(1, 6):
    for j in range(i, 5):
        print(" ", end=" ")
    for k in range((i * 2) - 1):
        print("*", end=" ")
    print()
