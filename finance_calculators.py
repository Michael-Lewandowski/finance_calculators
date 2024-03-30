
'finance_calculators.py'

"""
1. Import the math module.
2. Ask user to choose type of financial calculator 'investment' or 'bond'.
3. Take the user's choice as input.
4. For investment calculator:
 - Prompt for the amount of money being invested, the interest rate, the number of years for the investment, and the interest type (simple or compound).
 - Calculate the total amount after the investment period based on the interest type.
5. For bond calculator:
 - Prompt for the present value of the house, the interest rate, and the number of months to repay the bond.
 - Calculate the monthly repayment amount.
6. Display the calculated result to the user.
"""

# Importing the math library for calculations
import math

# Presenting the options to the user
print("Choose a calculator:")
print("1. Investment")
print("2. Bond")
user_choice = input("Enter your choice (investment or bond): ").lower()

# Handling the user's choice
if user_choice == "investment":
        
    # Investment calculations                    
    P = float(input("Enter the amount of money you are depositing: "))
    r = float(input("Enter the interest rate (as a percentage): ")) / 100
    t = float(input("Enter the number of years for the investment: "))
    interest_type = input("Choose the type of interest (simple or compound): ").lower()

    # Calculating the return based on the type of interest
    if interest_type == "simple":
            A = P * (1 + r * t)
    elif interest_type == "compound":
            A = P * math.pow((1 + r), t)
    else:
        print("Invalid interest type entered.")

    # Displaying the result
    print(f"The total amount after {t} years is: {A}")

elif user_choice == "bond":
        
    # Bond repayment calculations
    P = float(input("Enter the present value of the house: "))
    r = float(input("Enter the annual interest rate: ")) / (100 * 12)
    n = float(input("Enter the number of months to repay the bond: "))

    # Calculating the monthly repayment
    repayment = (r * P) / (1 - (1 + r)**(-n))

    # Displaying the result
    print(f"The monthly repayment on the bond is: {repayment}")

else:
    print("Invalid choice entered. Please enter either 'investment' or 'bond'.")
    