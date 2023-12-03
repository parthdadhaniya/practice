"""
Q35. Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""

salary = int(input("Enter your salary : "))

if salary > 50000:
    increment = 20
elif salary > 20000 and salary <= 50000:
    increment = 15
elif salary > 10000 and salary <= 20000:
    increment = 10
else:
    increment = 5

incremented_salary = (salary * increment) / 100

print("Your updated salary is : ", salary + incremented_salary)
