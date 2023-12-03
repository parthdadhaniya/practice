"""
Q31. Write a program to calculate bill. 
Ask the final amount from the user.
You have to give discount and print the final bill after discount.
50000 above - 30% discount40000 - 49999 - 25% discount30000 - 39999 - 20% discount10000 - 29999 - 10% discount1 - 9999 - No discount 
Print the discount and the final amount to be paid.
"""

final_amount = int(input("Enter your final amount : "))

if final_amount >= 50000:
    print("You have get 30'%' discount")
    final_discount = (final_amount * 30) / 100
    print("Your discount amount is ", final_discount)
    print("Your final bill is : ", final_amount - final_discount)
elif final_amount >= 40000 and final_amount <= 49999:
    print("You have get 25'%' discount")
    final_discount = (final_amount * 25) / 100
    print("You discount amount is ", final_discount)
    print("Your final bill is : ", final_amount - final_discount)
elif final_amount >= 30000 and final_amount <= 39999:
    print("You have get 20'%' discount")
    final_discount = (final_amount * 20) / 100
    print("You discount amount is ", final_discount)
    print("Your final bill is : ", final_amount - final_discount)
elif final_amount >= 10000 and final_amount <= 29999:
    print("You have get 20'%' discount")
    final_discount = (final_amount * 10) / 100
    print("You discount amount is ", final_discount)
    print("Your final bill is : ", final_amount - final_discount)
else:
    print("Sorry no discount")
    print("Your final bill is : ", final_amount)
