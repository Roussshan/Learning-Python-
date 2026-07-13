#input values
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))

#Calculate the compound_intrest
compound_intrest = principal*((1+rate/100)**time)-principal

#Output the result
print("The compound Interest is:",compound_intrest)