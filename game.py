import random

def play_level(stage, level, max_number):
    """
    Play a single level of the game.
    
    Args:
        stage (str): Current stage ("Easy" or "Hard")
        level (int): Current level (1-5)
        max_number (int): Maximum number for random generation
    
    Returns:
        bool: True if level passed, False if game over
    """
    secret_number = random.randint(1, max_number)
    attempts = 4
    
    print(f"\n{'='*50}")
    print(f"Stage: {stage} | Level: {level} | Attempts: {attempts}")
    print(f"Guess a number between 1 and {max_number}")
    print(f"{'='*50}\n")
    
    while attempts > 0:
        try:
            guess = int(input(f"Turn {5 - attempts}: Enter your guess: "))
            
            if guess < 1 or guess > max_number:
                print(f"Please enter a number between 1 and {max_number}.\n")
                continue
            
            if guess == secret_number:
                print("\n✓ Correct! You passed the level.\n")
                return True
            elif guess > secret_number:
                print("The number is smaller.")
            else:
                print("The number is bigger.")
            
            attempts -= 1
            if attempts > 0:
                print(f"Attempts remaining: {attempts}\n")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue
    
    print(f"\n✗ Game Over! Try Again.")
    print(f"The secret number was: {secret_number}\n")
    return False

def play_stage(stage, num_levels, max_number):
    """
    Play all levels in a stage.
    
    Args:
        stage (str): Stage name ("Easy" or "Hard")
        num_levels (int): Number of levels (5)
        max_number (int): Maximum number for random generation
    
    Returns:
        bool: True if all levels completed, False if user wants to quit
    """
    completed_levels = 0
    
    for level in range(1, num_levels + 1):
        while True:
            passed = play_level(stage, level, max_number)
            
            if passed:
                completed_levels += 1
                break
            else:
                retry = input("Do you want to retry this level? (yes/no): ").strip().lower()
                if retry != 'yes':
                    quit_game = input("Do you want to quit the game? (yes/no): ").strip().lower()
                    if quit_game == 'yes':
                        return False
    
    return True

def main():
    """Main game function."""
    print("\n" + "="*50)
    print("   WELCOME TO NUMBER GUESSING GAME")
    print("="*50)
    print("\nGame Rules:")
    print("- Guess the secret number within 4 attempts")
    print("- Easy Stage: Numbers 1-50")
    print("- Hard Stage: Numbers 1-100")
    print("- Complete Easy Stage to unlock Hard Stage\n")
    
    while True:
        # Easy Stage
        print("\n" + "="*50)
        print("STARTING EASY STAGE")
        print("="*50)
        easy_passed = play_stage("Easy", 5, 50)
        
        if not easy_passed:
            print("\nThanks for playing! Goodbye!\n")
            break
        
        print("\n" + "🎉 "*15)
        print("Congratulations! You completed the Easy Stage!")
        print("Unlocking Hard Stage...\n")
        
        # Hard Stage
        print("="*50)
        print("STARTING HARD STAGE")
        print("="*50)
        hard_passed = play_stage("Hard", 5, 100)
        
        if not hard_passed:
            print("\nThanks for playing! Goodbye!\n")
            break
        
        print("\n" + "🎉 "*15)
        print("Congratulations! You completed the entire game!")
        print("🎉 "*15 + "\n")
        
        # Restart option
        restart = input("Do you want to play again? (yes/no): ").strip().lower()
        if restart != 'yes':
            print("\nThanks for playing! Goodbye!\n")
            break

if __name__ == "__main__":
    main()
