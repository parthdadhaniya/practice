# Q53. Ask to numbers x and y from the user. If x<y then print all the numbers from x to y, but if y<x then print all the numbers from y to x.


x = int(input("Enter a number : "))
y = int(input("Enter a number : "))

start = x if x < y else y
end = y if x < y else x

i = start

while i <= end:
    print(i)
    i += 1
