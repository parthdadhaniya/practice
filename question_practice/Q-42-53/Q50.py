# Q50. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.

count = 0

number = 1

while number <= 200:
    if number % 6 == 0 and number % 7 == 0:
        count += 1
    number = number + 1
print(count)
