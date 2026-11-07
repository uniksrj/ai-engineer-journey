import random

# Display game rules
print("Welcome to Rock-Paper-Scissors!\n")
print("Winning Rules:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

Choices = ["Rock", "Paper", "Scissor"]

while True:
    print("Choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    try:
        choice = int(input("Enter your choice :"))
    except ValueError:
        print("Please enter a valide number. \n")

    while choice < 1 or choice > 3:
        choice = int(input("Please enter a valid choice (1-3): "))

    userChoice = Choices[choice-1]

    print("\nUser choice is:", userChoice)
    print("Now it's Computer's Turn...")

    compNumber = random.randint(1,3)
    compChoice = Choices[compNumber - 1]

    print("Computer choice is:", compChoice)
    print(userChoice, "vs", compChoice)

    if choice == compNumber:
        print("It's a tie!")
    elif (choice == 1 and compNumber == 2) or (choice == 2 and compNumber == 3) or (choice == 3 and compNumber == 1):
        print("User wins!")
    else:
        print("Computer wins!")

    playAgain = input("Do you want to play again? (y/n): ")
    if playAgain.lower() != 'y':
        print("Thanks for playing!")
        break


print("\nThanks for playing!")