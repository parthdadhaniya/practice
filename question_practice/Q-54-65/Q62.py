# Q62. Calculate how many numbers are divisible by 6 and 7 between 1 to 200.

count = 0

for i in range(1, 200 + 1):
    if i % 6 == 0 and i % 7 == 0:
        count += 1
print(count)
