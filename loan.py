# Get the loan details
money_owed = float(input("How much money do you owe, in pounds?\n")) # £6000
apr = float(input("What is the annual percentage?\n")) # 3.5%
payment = float(input("What will be your monthly payment?\n")) # £1,000
months = int(input("How many months do you want to see the results for?\n")) # 12

# Divide apr by 100 to make it a percent, then divide by 12 to make it monthly
monthly_rate = apr/100/12
for i in range(months):
    # Add in intrest
    intrest_paid = money_owed * monthly_rate
    money_owed = money_owed + intrest_paid
    
    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid of the loan in", i+1, "months")
        break

    # Make payment
    money_owed = money_owed - payment

    # Print the results after this month
    print("Paid", payment, "of which", intrest_paid, "was intrest", end=' ')
    print("Now I owe", money_owed)