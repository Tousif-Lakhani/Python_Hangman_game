import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

def get_word():
    # Path to the text file
    with open('C:\\Users\Lenovo\Desktop\VS Pracrtice\projects\words.txt', 'r') as f:
        # Reads each word after splitting
        words1 = f.read().splitlines()
    # Returns any random word    
    return random.choice(words1)

def start_game():

# Randomly choose a word from the list
    chosen_word = get_word()
    word_display = ['_' for _ in chosen_word]
    
    attempts = 6 # Number of allowed attempts
    guessed_letters = [] # List to store guessed letters

    print("Welcome to Hangman!")

    while attempts > 0 and '_' in word_display:
        print("\n" + ' '.join(word_display))
        guess = input("Guess a letter: ").lower()
        

        if len(guess) != 1:
            print("You should input a single letter")
        
        elif guess in guessed_letters:
            print("You've already guessed this letter")

        elif not guess.isalpha():
            print("Please enter a single letter")
        
        elif guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    if word_display[index] == guess:
                        print("You've already guessed this letter")
                    else:
                        word_display[index] = guess # reveal letter

        else:
            print("That letter doesn't appear in the word.")
            print(stages[attempts-1])
            attempts -= 1
            guessed_letters.append(guess)
            print(f'{attempts} attempts remaining')

    # Game conclusion
    if '_'not in word_display:
        print("You guessed the word!")
        print(' '.join(word_display))
        print("You survived!")

    else:
        print(f"You ran out of attempts. The word was: {chosen_word}")
        print("You lost!")
        guessed_letters = []

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'no' and play_again.lower() != 'yes':
        print("Please enter a valid input")
        play_again = input("Do you want to play again? (yes/no): ")

    elif play_again.lower() == 'yes':
        print("\n")
        start_game()
    elif play_again.lower() == 'no':
        print(" ")
        print("Thank you for playing Hangman. Have a nice day :) !!!")
    elif play_again.lower() == 'yes':
        print("\n")
        start_game()
    

start_game()