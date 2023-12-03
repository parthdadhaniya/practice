"""
Q34. A student will not be allowed to sit in exam if his/her attendance is less than 75%. 
a. Take following input from useri. Number of classes held ii. 
Number of classes attended. 
b. Print percentage of class attended 
c. Print Is student is allowed to sit in exam or not.
"""

number_of_classes_held = int(input("Enter a number of classess held : "))
number_of_classess_attend = int(input("Enter a number of classess attend : "))

percentage = (number_of_classes_held * number_of_classess_attend) / 100

print("percentage: ", percentage)

if percentage >= 75:
    print("You can sit the exam")
else:
    print("You can not sit the exam")
