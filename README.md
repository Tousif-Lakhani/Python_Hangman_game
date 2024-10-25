# Hangman Game
Welcome to the Hangman Game! This classic word-guessing game challenges players to identify a hidden word, letter by letter, before running out of attempts. Perfect for practicing vocabulary, spelling, and a bit of deduction, this Hangman implementation in Python allows for a fun and interactive experience directly from your terminal.

# Overview
This Hangman game is written in Python, with a straightforward approach to gameplay. Players attempt to guess the letters in a hidden word, with each incorrect guess resulting in a step closer to losing the game. You have a limited number of guesses, so choose carefully! Words are randomly selected from a text file, keeping gameplay fresh and unpredictable.

# How to Play
1 - The program selects a random word from a pre-defined list of words.

2 - Players guess letters one at a time.

3 - Correct guesses reveal the letter(s) in the word, while incorrect guesses reduce the number of attempts.

4 - The game ends when:

  - The player guesses all letters correctly (Win)
    
  - The player runs out of attempts (Lose)
    
5 - Players are prompted to play again after each game.

# Features
- **Random Word Selection**: Words are drawn from a custom list, ensuring a new word every round.
- **Error Handling**: The game manages common input errors, ensuring a smooth experience.
- **Replayability**: The user can replay the game without needing to restart the program.
- **ASCII Art Stages**: Players see the progression of "hangman" visuals with each incorrect guess, adding to the game’s charm.

# Setup
1 - Clone the Repository:
```
git clone https://github.com/Tousif-Lakhani/hangman-game.git
cd hangman-game
```

2 - Create a Word List:

- Prepare a file named **words.txt** with a list of words (one word per line) that the game will randomly select from.
- Update the path in the get_word function if necessary.

3 - Run the Game:
- Launch the game by running the following command in your terminal:
bash
```
python hangman.py
```

# Game Design
The game functions are split into two main components:

- get_word(): Retrieves a random word from the words.txt file.
- start_game(): Manages the game loop, which handles user input, tracks attempts, displays the word, and checks for win/loss conditions.

Additional error handling in start_game() ensures:
- Single-letter inputs
- Validation of previously guessed letters
- Tracking of guessed letters to prevent duplicates

# Usage
To start the game:

1 - Ensure you’re in the correct directory.

2 - Run python hangman.py.

3 - Follow the prompts to guess letters and see the game progress in your terminal.

Each time you guess a letter, the game will:
- Display the current state of the word with correct guesses filled in
- Show a "hangman" image to indicate how many incorrect guesses remain
- Notify you of any incorrect guesses or repeated letters

#
Enjoy the game, and thank you for cheking out this project!


