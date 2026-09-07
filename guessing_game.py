import random

# Global variables
total_score = 0
current_difficulty = ""
current_level = 0

# Difficulty configurations
DIFFICULTIES = {
    "Easy": {
        "levels": [
            {"level": 1, "range": (1, 10)},
            {"level": 2, "range": (1, 20)},
            {"level": 3, "range": (1, 30)},
            {"level": 4, "range": (1, 50)},
            {"level": 5, "range": (1, 100)}
        ],
        "multiplier": 1
    },
    "Intermediate": {
        "levels": [
            {"level": 1, "range": (1, 100)},
            {"level": 2, "range": (1, 250)},
            {"level": 3, "range": (1, 500)},
            {"level": 4, "range": (1, 750)},
            {"level": 5, "range": (1, 1000)}
        ],
        "multiplier": 2
    },
    "Hard": {
        "levels": [
            {"level": 1, "range": (1, 1000)},
            {"level": 2, "range": (1, 5000)},
            {"level": 3, "range": (1, 10000)},
            {"level": 4, "range": (1, 50000)},
            {"level": 5, "range": (1, 100000)}
        ],
        "multiplier": 3
    }
}

MAX_CHANCES = 5


def clear_screen():
    """Clear the console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def display_main_menu():
    """Display the main menu."""
    clear_screen()
    print("="*40)
    print("     ���� NUMBER GUESSING GAME")
    print("="*40)
    print()
    print("1. Easy")
    print("2. Intermediate")
    print("3. Hard")
    print("4. View Score")
    print("5. Exit")
    print()


def get_valid_menu_choice(max_option):
    """Get a valid menu choice from the user."""
    while True:
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= max_option:
                return choice
            else:
                print(f"⚠️  Please enter a number between 1 and {max_option}.")
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number.")


def display_difficulty_menu(difficulty):
    """Display the level menu for a difficulty."""
    clear_screen()
    print("="*40)
    print(f"          {difficulty.upper()} LEVELS")
    print("="*40)
    print()
    levels = DIFFICULTIES[difficulty]["levels"]
    for level_info in levels:
        level_num = level_info["level"]
        range_min, range_max = level_info["range"]
        print(f"{level_num}. Level {level_num}  ({range_min}–{range_max})")
    print(f"{len(levels) + 1}. Back to Main Menu")
    print()


def get_valid_guess(min_val, max_val):
    """Get a valid guess from the user within the specified range."""
    while True:
        try:
            guess = int(input(f"Enter your guess ({min_val}–{max_val}): "))
            if min_val <= guess <= max_val:
                return guess
            else:
                print(f"⚠️  The number must be between {min_val} and {max_val}.")
        except ValueError:
            print("⚠️  Invalid input! Please enter a valid number.")


def calculate_score(level, chances_used, multiplier):
    """Calculate points earned for completing a level."""
    # Base score: 100 points per level
    base_score = level * 100
    
    # Bonus for using fewer chances: (6 - chances_used) * 50
    bonus_score = (MAX_CHANCES - chances_used + 1) * 50
    
    # Apply difficulty multiplier
    total_points = (base_score + bonus_score) * multiplier
    
    return total_points


def play_level(difficulty, level_info):
    """Play a single level."""
    global total_score
    
    level_num = level_info["level"]
    range_min, range_max = level_info["range"]
    secret_number = random.randint(range_min, range_max)
    
    print()
    print(f"Guess the number between {range_min} and {range_max}")
    print()
    
    chances_used = 0
    
    while chances_used < MAX_CHANCES:
        chances_used += 1
        guess = get_valid_guess(range_min, range_max)
        
        if guess == secret_number:
            print()
            print("🎉 CORRECT!")
            print()
            multiplier = DIFFICULTIES[difficulty]["multiplier"]
            points = calculate_score(level_num, chances_used, multiplier)
            total_score += points
            print(f"Number: {secret_number}")
            print(f"Chances used: {chances_used}/{MAX_CHANCES}")
            print(f"Points earned: {points}")
            print(f"Total Score: {total_score}")
            print()
            return True
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
        
        if chances_used < MAX_CHANCES:
            print(f"Chance {chances_used + 1}/{MAX_CHANCES}: ", end="")
        print()
    
    # Player lost
    print()
    print("❌ YOU LOST!")
    print()
    print(f"You used all {MAX_CHANCES} chances.")
    print(f"The correct number was: {secret_number}")
    print("Points earned: 0")
    print(f"Total Score: {total_score}")
    print()
    return False


def level_failed_menu():
    """Display options after failing a level."""
    while True:
        print("1. Retry Level")
        print("2. Return to Difficulty Menu")
        print("3. Main Menu")
        print()
        choice = get_valid_menu_choice(3)
        return choice


def play_difficulty(difficulty):
    """Play all levels in a difficulty."""
    global current_level
    
    levels = DIFFICULTIES[difficulty]["levels"]
    current_level = 0
    
    while current_level < len(levels):
        display_difficulty_menu(difficulty)
        choice = get_valid_menu_choice(len(levels) + 1)
        
        if choice == len(levels) + 1:
            # Back to main menu
            return
        
        level_info = levels[choice - 1]
        current_level = choice - 1
        
        clear_screen()
        print()
        print(f"🎯 {difficulty} - Level {level_info['level']}")
        print()
        
        while True:
            success = play_level(difficulty, level_info)
            
            if success:
                if level_info["level"] == len(levels):
                    # Completed all levels
                    clear_screen()
                    print()
                    print("="*40)
                    print("🏆 CONGRATULATIONS!")
                    print("="*40)
                    print()
                    print(f"You completed all {len(levels)} levels of {difficulty}!")
                    print()
                    print(f"Total Score: {total_score}")
                    print()
                    input("Press Enter to return to Main Menu...")
                    return
                else:
                    # Level completed, move to next
                    clear_screen()
                    print()
                    print(f"🎉 LEVEL {level_info['level']} COMPLETED!")
                    print()
                    print(f"You guessed the number in {current_level + 1} chances.")
                    print()
                    print(f"➡️  Level {level_info['level'] + 1} unlocked!")
                    print()
                    input("Press Enter to continue...")
                    break
            else:
                # Level failed
                choice = level_failed_menu()
                
                if choice == 1:
                    # Retry level
                    clear_screen()
                    print()
                    print(f"🎯 {difficulty} - Level {level_info['level']}")
                    print()
                elif choice == 2:
                    # Return to difficulty menu
                    break
                elif choice == 3:
                    # Return to main menu
                    return


def show_score():
    """Display the current total score."""
    clear_screen()
    print()
    print("="*40)
    print("       YOUR SCORE")
    print("="*40)
    print()
    print(f"Total Score: {total_score}")
    print()
    input("Press Enter to return to Main Menu...")


def main_menu():
    """Main game loop."""
    global current_difficulty
    
    while True:
        display_main_menu()
        choice = get_valid_menu_choice(5)
        
        if choice == 1:
            current_difficulty = "Easy"
            play_difficulty("Easy")
        elif choice == 2:
            current_difficulty = "Intermediate"
            play_difficulty("Intermediate")
        elif choice == 3:
            current_difficulty = "Hard"
            play_difficulty("Hard")
        elif choice == 4:
            show_score()
        elif choice == 5:
            clear_screen()
            print()
            print("Thanks for playing! 👋")
            print()
            break


if __name__ == "__main__":
    main_menu()
