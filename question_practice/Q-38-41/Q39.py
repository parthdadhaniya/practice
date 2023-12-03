# Q39. Write a program that checks if a given year is a leap year. Leap years are divisible by 4, but not by 100 unless they are also divisible by 400.


year = int(input("Enter a year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year is a leap year")
        else:
            print("Year is a not a leap year")
    else:
        print("Year is a leap year")
else:
    print("Year is a not leap year")
