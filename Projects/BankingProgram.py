def show_balance():
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter amount to deposit: $"))

    if amount < 0:
        print("Please Enter Correct Amount!")
        return 0
    else:
        return amount


def withdraw():
    amount = float(input("Enter amount to withdraw: $"))

    if amount < 0:
        print("Please Enter Correct Amount!")
        return 0
    elif amount > balance:
        print("Insufficient funds!")
        return 0
    else:
        return amount

balance = 0
is_running = True   

while is_running:
    print("Welcome to the Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposit()
    elif choice == '3':
        balance -= withdraw()
    elif choice == '4':
        is_running = False
        print("Thank you for using the Banking Program. Goodbye!")
    else:
        print("Invalid option. Please try again.")