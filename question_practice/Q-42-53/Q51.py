"""
Q51. Ask a number from user. Print the multiplication table of that number.ExampleEnter a number = 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
.....
8 x 10 = 80

"""

number = int(input("Enter a number : "))

i = 1

while i <= 10:
    count = number * i
    print(f"{number} x {i} = {count}")
    i += 1
