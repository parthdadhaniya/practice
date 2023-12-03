"""
Q33. Ask a number from user.
Print “Fizz” if the number is divisible by 3.
Print “Buzz” if the number is divisible by 5.
Print “FizzBuzz” if the number is divisible by 3 and 5.
"""

number = int(input("Enter a number : "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
