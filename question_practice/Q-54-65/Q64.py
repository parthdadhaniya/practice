"""
Q64. Calculate factorial of a number entered by user.Example:Enter a number = 5
Factorial of a number means product of all the numbers from 1 to that number.
5 factorial =  5 x 4 x 3 x 2 x 1O utput = 120
"""

number = int(input("Enter a number : "))
product = 1

for i in range(1, number + 1):
    product = product * i
print(product)
