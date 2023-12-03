# Q24. Write a program that takes a character as input and prints whether it's a vowel or a consonant. (Multiple OR will be used)

character = str(input("Enter a character : "))

if character not in ["a", "e", "i", "o", "u"]:
    print("Consonant")
else:
    print("Vowel")
