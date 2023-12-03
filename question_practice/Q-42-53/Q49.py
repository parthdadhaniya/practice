# Q49. Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.


count = 0

number = 20

while number <= 50:
    if number % 4 == 0:
        count += 1
    number = number + 1
print(count)
