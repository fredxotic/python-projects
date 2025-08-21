# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100

total_amount = 0
print("-----Do you want to Deposit or withdraw?----")

while True:
    user_input = input("D(Deposit) OR W(Withdraw): ")
    if user_input == "D":
        deposit = int(input('D: '))
        total_amount += deposit
    elif user_input == "W":
        withdrawal = int(input('W: '))
        total_amount -= withdrawal
    else:
        break

print(f"\nTotal amount: {total_amount}")
