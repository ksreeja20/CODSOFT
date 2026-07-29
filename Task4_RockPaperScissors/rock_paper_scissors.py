import random

user_score = 0
computer_score = 0
draws = 0

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("\n===== ROCK PAPER SCISSORS =====")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("\nFinal Score")
        print("You      :", user_score)
        print("Computer :", computer_score)
        print("Draws    :", draws)
        print("\nThank you for playing!")
        break

    if choice not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1-4.")
        continue

    user_choice = choices[int(choice) - 1]
    computer_choice = random.choice(choices)

    print("\nYou chose      :", user_choice)
    print("Computer chose :", computer_choice)

    if user_choice == computer_choice:
        print("🤝 It's a Draw!")
        draws += 1

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        print("🎉 You Win!")
        user_score += 1

    else:
        print("😔 Computer Wins!")
        computer_score += 1

    print("\n===== SCOREBOARD =====")
    print("You      :", user_score)
    print("Computer :", computer_score)
    print("Draws    :", draws)