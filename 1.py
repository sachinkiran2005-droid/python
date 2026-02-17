import random

print("🎲 Welcome to Dice Rolling Game!")
print("First to reach 5 points wins!")
print("----------------------------------")

user_score = 0
computer_score = 0

while user_score < 5 and computer_score < 5:
    input("\nPress Enter to roll the dice...")

    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("🎲 You rolled:", user_roll)
    print("💻 Computer rolled:", computer_roll)

    if user_roll > computer_roll:
        print("🎉 You win this round!")
        user_score += 1
    elif user_roll < computer_roll:
        print("💻 Computer wins this round!")
        computer_score += 1
    else:
        print("🤝 It's a tie!")

    print("Score → You:", user_score, "| Computer:", computer_score)

# Final Result
print("\n🏁 Final Result")
if user_score > computer_score:
    print("🏆 Congratulations! You won the game!")
else:
    print("💻 Computer wins the game!")

print("Thanks for playing!")