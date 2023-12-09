"""
Q63. Ask a number from user. Print the multiplication table of that number.ExampleEnter a number = 88 x 1 = 88 x 2 = 168 x 3 = 24
"""

number = int(input("Enter a number : "))
# count = 0

for i in range(1, 10 + 1):
    count = number * i
    print(f"{number} x {i} = {count}")
