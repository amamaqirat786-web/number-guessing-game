# 🎯 Number Guessing Game

A challenging console-based number guessing game built with Python. Test your guessing skills across three difficulty levels with 5 levels each!

## 📋 Project Description

This is an interactive Python game where players guess random numbers within specified ranges. The game features:

- **3 Difficulty Categories**: Easy, Intermediate, and Hard
- **5 Levels per Difficulty**: Progressive range increases
- **5-Chance Limit**: Each level allows exactly 5 attempts to guess the correct number
- **Dynamic Scoring System**: Points based on difficulty, level, and accuracy
- **Input Validation**: Safe handling of invalid inputs
- **Retry System**: Failed levels can be retried with a new random number

## ✨ Features

- 🎮 Interactive console-based gameplay
- 📊 Real-time score tracking
- 🔄 Level retry system after failure
- ⚠️ Input validation (no invalid guesses count against your chances)
- 🎯 Progressive difficulty scaling
- 🏆 Level completion feedback and achievement messages
- 💾 Session-based score tracking

## 🎯 Difficulty Levels

### Easy
- **Level 1**: Guess a number between 1–10
- **Level 2**: Guess a number between 1–20
- **Level 3**: Guess a number between 1–30
- **Level 4**: Guess a number between 1–50
- **Level 5**: Guess a number between 1–100

### Intermediate
- **Level 1**: Guess a number between 1–100
- **Level 2**: Guess a number between 1–250
- **Level 3**: Guess a number between 1–500
- **Level 4**: Guess a number between 1–750
- **Level 5**: Guess a number between 1–1,000

### Hard
- **Level 1**: Guess a number between 1–1,000
- **Level 2**: Guess a number between 1–5,000
- **Level 3**: Guess a number between 1–10,000
- **Level 4**: Guess a number between 1–50,000
- **Level 5**: Guess a number between 1–100,000

## 🎲 Five-Chance Rule

Each level gives you **exactly 5 chances** to guess the correct number.

### Example Gameplay:
```
Guess the number between 1 and 100

Chance 1/5: 50
Too low!

Chance 2/5: 75
Too high!

Chance 3/5: 65
Too low!

Chance 4/5: 70
Too high!

Chance 5/5: 68
🎉 Correct!
```

### Failed Level Example:
```
❌ YOU LOST!

You used all 5 chances.
The correct number was: 68
Points earned: 0
```

**Important**: Invalid input does NOT count as one of your 5 chances!

## 📈 Scoring System

Points are calculated based on:

1. **Base Score**: `Level × 100`
2. **Bonus Score**: `(6 - Chances Used) × 50`
3. **Difficulty Multiplier**:
   - Easy: ×1
   - Intermediate: ×2
   - Hard: ×3

**Total Points** = (Base Score + Bonus Score) × Difficulty Multiplier

### Score Example:
```
🎉 CORRECT!

Number: 68
Chances used: 3/5
Points earned: 300
Total Score: 750
```

## 🚀 How to Install Python

### Windows
1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.x (latest version)
3. Run the installer and **check "Add Python to PATH"**
4. Click "Install Now"

### macOS
1. Visit [python.org](https://www.python.org/downloads/)
2. Download Python 3.x for macOS
3. Run the installer and follow the prompts

### Linux
```bash
sudo apt-get update
sudo apt-get install python3
```

## 🎮 How to Run the Game

### 1. Clone the Repository
```bash
git clone https://github.com/amamaqirat786-web/number-guessing-game.git
cd number-guessing-game
```

### 2. Run the Game
```bash
python main.py
```

or on some systems:
```bash
python3 main.py
```

## 📖 How to Play

### Main Menu
```
========================================
       🎯 NUMBER GUESSING GAME
========================================

1. Easy
2. Intermediate
3. Hard
4. View Score
5. Exit

Choose an option:
```

### Level Selection
Select a difficulty, then choose a level (1–5) or return to the main menu.

### During Gameplay
1. You'll see the range you need to guess within
2. Enter your guess
3. The game tells you if it's too high, too low, or correct
4. You have **5 chances** to guess correctly
5. Invalid input doesn't consume a chance

### After Winning a Level
- ✅ Points are awarded
- ➡️ You unlock the next level
- 🏆 After Level 5, you see a completion message

### After Losing a Level
- ❌ You see the correct number
- You can choose to:
  - **Retry Level**: Play with a new random number
  - **Return to Difficulty Menu**: Pick a different level
  - **Main Menu**: Return to the main menu

## 📝 Example Gameplay

### Level Completion
```
🎯 Easy - Level 1

Guess the number between 1 and 10

Chance 1/5: 5
Too high!

Chance 2/5: 3
Too low!

Chance 3/5: 4
🎉 Correct!

Number: 4
Chances used: 3/5
Points earned: 350
Total Score: 350

🎉 LEVEL 1 COMPLETED!

You guessed the number in 3 chances.

➡️  Level 2 unlocked!
```

### Difficulty Completion
```
🏆 CONGRATULATIONS!

You completed all 5 levels of Easy!

Total Score: 1,750
```

## 🔧 Code Structure

The project is organized with the following key functions:

- `main_menu()` - Main game loop
- `display_main_menu()` - Shows main menu options
- `play_difficulty()` - Handles a difficulty category
- `play_level()` - Core game logic for a single level
- `calculate_score()` - Computes points earned
- `show_score()` - Displays current total score
- `get_valid_menu_choice()` - Validates menu input
- `get_valid_guess()` - Validates number input
- `level_failed_menu()` - Shows retry options
- `clear_screen()` - Clears console display

## 🛠️ Technologies Used

- **Language**: Python 3
- **Libraries**: `random`, `os` (standard library only)
- **No external dependencies required**

## 📚 Future Improvements

- [ ] Save/load game progress to a file
- [ ] Leaderboard system with player names
- [ ] Difficulty streak tracker
- [ ] Time-based challenges (guess within X seconds)
- [ ] Statistics dashboard (average guesses, win rate, etc.)
- [ ] GUI version using tkinter
- [ ] Multiplayer mode
- [ ] Different game modes (higher/lower, number matching, etc.)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎯 Tips for Playing

1. **Use Binary Search**: For large ranges, guess the midpoint to eliminate half the numbers
2. **Listen to Feedback**: Pay attention to "too high" and "too low" hints
3. **Easy First**: Master Easy levels before moving to harder difficulties
4. **Maximize Points**: Try to win with fewer chances for higher scores
5. **Learn Patterns**: Each difficulty has its own number range pattern

## 🐛 Troubleshooting

### "python: command not found"
- Make sure Python is installed and added to your PATH
- Try `python3 main.py` instead

### Input doesn't seem to work
- Make sure you press Enter after typing your guess
- The game only accepts numbers, not letters

### Score not updating
- Score is tracked during your current session only
- Restarting the game resets the score (see future improvements for persistence)

## 🙌 Contributing

Feel free to fork this project and submit pull requests with improvements!

## 📧 Support

If you encounter any issues, please open an issue on GitHub.

---

**Enjoy the game and happy guessing! 🎯**
