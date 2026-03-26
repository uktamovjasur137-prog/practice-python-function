def deposit(balance, amount):
    if amount > 0:
        balance += amount

    return balance

def withdraw(balance, amount):
    if amount > 0 and amount <= balance:
        balance -= amount

    return balance

def check_balance(balance):
    print(f"sizning hisobingiz: {balance}")

def main():
    balance = 500

    amount = float(input("Amount "))
    op = input("Amal: ")

    if op == "deposit":
        balance = deposit(balance, amount)
    
    elif op == "withdraw":
        balance = withdraw(balance, amount)

    else:
        print("amal notogri")

        check_balance

main()