# Q56. Ask start number and end number from user. Print all the numbers from start to end using while loop.

start_number = int(input("Enter a start number : "))
end_number = int(input("Enter a end number : "))

for i in range(start_number, end_number + 1):
    print(i)
