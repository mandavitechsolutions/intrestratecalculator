def calculate_interest(account_balance):
    # Define the interest rate slabs and corresponding interest rates
    slab_interest_rates = [
        (100000, 0.0425),  # 4.25% interest rate for balances up to ₹100000
        (1000000, 0.055),  # 5.5% interest rate for balances up to ₹1000000
        (2500000, 0.060),  # 6% interest rate for balances up to ₹2500000
        (20000000, 0.075),  # 7.5% interest rate for balances up to ₹20000000
        (30000000, 0.07)   # 7% interest rate for balances above ₹30000000
    ]

    total_interest = 0

    for slab_balance, slab_rate in slab_interest_rates:
        if account_balance <= 0:
            break
        elif account_balance <= slab_balance:
            total_interest += account_balance * slab_rate
            break
        else:
            total_interest += slab_balance * slab_rate
            account_balance -= slab_balance

    return total_interest

# Input the account balance
account_balance = float(input("Enter your account balance: ₹"))

# Calculate and display the interest
interest = calculate_interest(account_balance)
print(f"Your interest earned is: ₹{interest:.2f}")
