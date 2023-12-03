"""
Q52. Calculate factorial of a number entered by user.Example:Enter a number = 5
Factorial of a number means product of all the numbers from 1 to that number.
5 factorial =  5 x 4 x 3 x 2 x 1Output = 120
"""

number = int(input("Enter a number : "))
product = 1
i = 1

while i <= number:
    product *= i
    i += 1
print(product)
