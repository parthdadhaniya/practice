"""
Q26. A student will not be allowed to sit in exam if his/her attendance is less than 75%. Take following input from user
Number of classes held
Number of classes attended.1. Print percentage of class attended2. Print Is student is allowed to sit in exam or not.
"""

number_of_class_held = int(input("Enter a number of class held : "))
number_of_class_attend = int(input("Enter a number of class attend : "))

percentage = (number_of_class_held * number_of_class_attend) / 100
print("percentage: ", percentage)

if percentage >= 75:
    print("You Can sit the exam")
else:
    print("You can not sit the exam")
