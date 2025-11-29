def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    import random
    return [random.choice(symbols) for symbol in range(3)]
   
def print_rows(row):
    print("****************")
    print(" | ".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0
    

def main():
    balance = 100
    print("******************************")
    print("Welcome to the Slot Machine!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("******************************")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)

        if bet > balance:
            print("You cannot bet more than your current balance!")
            continue

        if bet <= 0:
            print("Bet amount must be greater than zero!")
            continue
        
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_rows(row)

        
        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
        else:
            print("Sorry, you didn't win this time.")

        balance += payout

    print("\nYou have no money left. Game over!")

    
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
