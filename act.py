import random

def fold_unfold_game():
    choices = {0: "Fold", 1: "Unfold"}
    
    print("Welcome to the Fold or Unfold Game!")
    
    while True:
        player_choice = input("Enter your choice (Fold/Unfold or 'quit' to exit): ").capitalize()
        
        if player_choice == 'Quit':
            print("Thanks for playing! Goodbye!")
            break
        
        if player_choice not in choices.values():
            print("Invalid choice! Please choose 'Fold' or 'Unfold'.")
            continue
        
        computer_choice = choices[random.randint(0, 1)]
        print(f"Computer chose: {computer_choice}")
        
        if player_choice == computer_choice:
            result = "Draw"
        elif (player_choice == "Fold" and computer_choice == "Unfold") or \
             (player_choice == "Unfold" and computer_choice == "Fold"):
            result = "Win" if player_choice == "Fold" else "Lose"
        
        print(f"You {result}!")
        print()

# Run the game
fold_unfold_game()
