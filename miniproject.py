def main():
    print("Welcome to Humber Bank Terminal!")
    attempts = 3
    pin = "7692"  
    balance = 1000.00  # Starting balance

    # 3 attempts to verify PIN
    while attempts > 0:
        entered_pin = input("Please enter your 4-digit PIN: ")
        if entered_pin == pin:
            print("PIN correct.")
            mainMenu(balance)
            return
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempts remaining.")

    print("Too many incorrect attempts. Exiting the program.")


def mainMenu(balance):
    while True:
        print("\nMain Menu:")
        print("1. Check Balance")
        print("2. Withdraw Funds")
        print("3. Deposit Funds")
        print("4. Exit")

        option = input("Please select an option: ")
        if option == '1':
            checkBalance(balance)
        elif option == '2':
            balance = withdraw(balance)
        elif option == '3':
            balance = deposit(balance)
        elif option == '4':
            print("Thank you for using Humber Bank. Have a great day!")
            break
        else:
            print("Invalid option. Please try again.")
        
        # Check if user wants to perform another action
        another_action = input("Would you like to perform another action? (y/n): ")
        if not another_action.lower() == 'y':
            print("Thank you for using Humber Bank. Have a great day!")
            break


def checkBalance(balance):
    print(f"Your current balance is: ${balance:.2f}")


def withdraw(balance):
    print("Withdrawal Options:")
    print("1. $20")
    print("2. $40")
    print("3. $60")
    print("4. $80")
    print("5. $100")
    print("6. Custom Amount")

    choice = input("Please select an option: ")
    withdrawalAmount = 0

    if choice == '1':
        withdrawalAmount = 20.00
    elif choice == '2':
        withdrawalAmount = 40.00
    elif choice == '3':
        withdrawalAmount = 60.00
    elif choice == '4':
        withdrawalAmount = 80.00
    elif choice == '5':
        withdrawalAmount = 100.00
    elif choice == '6':
        try:
            withdrawalAmount = float(input("Enter custom withdrawal amount: $"))
        except ValueError:
            print("Invalid amount entered. Please try again.")
            return balance
    else:
        print("Invalid option. Please try again.")
        return balance

    if withdrawalAmount <= 0:
        print("Withdrawal amount must be greater than zero.")
    elif withdrawalAmount > balance:
        print("Insufficient funds. Transaction cancelled.")
    else:
        balance -= withdrawalAmount
        print(f"Withdrawal successful. New balance: ${balance:.2f}")
    
    return balance


def deposit(balance):
    try:
        depositAmount = float(input("Enter deposit amount: $"))
        if depositAmount <= 0:
            print("Deposit amount must be greater than zero.")
            return balance
        balance += depositAmount
        print(f"Deposit successful. New balance: ${balance:.2f}")
    except ValueError:
        print("Invalid amount entered. Please try again.")
    return balance


main()
