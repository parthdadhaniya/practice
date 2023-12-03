# Q47. Calculate how many numbers are divisible by 7 from 1 to 100.

count = 0
number = 1
while number <= 100:
    if number % 7 == 0:
        count += 1
    number = number + 1

print(count)
