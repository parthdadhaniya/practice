# Q14. Write a Python program to calculate the compound interest for a given principal, rate of interest, and time period. Ask everything from the user.


given_principal = int(input("Enter principal : "))
rate_of_interest = float(input("Enter rate of interest : "))
time_duration = int(input("Enter time duration : "))

compound_intrest = (given_principal * rate_of_interest) / 100
total_payble = given_principal + compound_intrest
print("compound_intrest: ", compound_intrest)
print("total_payble: ", total_payble)
