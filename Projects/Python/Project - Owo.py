import random
import time
print("""
░█████╗░░██╗░░░░░░░██╗░█████╗░
██╔══██╗░██║░░██╗░░██║██╔══██╗
██║░░██║░╚██╗████╗██╔╝██║░░██║
██║░░██║░░████╔═████║░██║░░██║
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░
""")


def owof() :
    # Starting cash
    cash = 100
    owo = ["HEADS", "TAILS"]

    print(f"💰 OWO GIVES YOU INITIAL CASH : ₹{cash}")

    remain = True
    while remain:
        # User input
        user_input = input("\nENTER H (HEAD), T (TAIL), CC (Check Cash): ").upper()

        if user_input == "CC":
            print(f"💰 CURRENT CASH: ₹{cash}")
            continue

        if user_input == "H":
            user = "HEADS"
        elif user_input == "T":
            user = "TAILS"
        else:
            print("❌ INVALID INPUT")
            continue

        # Get bet
        try:
            bet = int(input("💸 Enter your bet amount: "))
        except ValueError:
            print("❌ Invalid number!")
            continue

        if bet > cash:
            print("❌ Not enough cash!")
            continue
        elif bet <= 0:
            print("❌ Bet must be positive!")
            continue

        # Toss the coin
        print("🌀 OWO IS FLIPPING THE COIN...")
        time.sleep(2)
        owoc = random.choice(owo)
        print(f"🎲 Coin Result: {owoc}")

        # Check result
        if user == owoc:
            win_amount = bet * 2
            cash += bet
            print(f"🎉 YOU WON ₹{win_amount}!")
        else:
            cash -= bet
            print(f"😢 YOU LOST ₹{bet}!")

        # Game over
        if cash <= 0:
            print("💸 You're out of cash! Game Over.")
            break

        again = input("🔁 PLAY AGAIN? (Y/N): ").upper()
        if again == "Y":
            continue
        elif again == "N":
            print("🙏 THANKS FOR PLAYING OWO COIN TOSS!")
            break
        else:
            print("❌ INVALID INPUT, ending game.")
            break
owof()