# Q61. Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.

total = 0

for i in range(20, 50 + 1):
    if i % 4 == 0:
        total += i
print(total)
