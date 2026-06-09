# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python that uses strings, loops, conditionals, and user input. The player should guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Set Up the Word Puzzle

#### Description
Create the hidden word and the data needed to track the player’s guesses during the game.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Show the current progress using an underscore format such as `_ _ _ _`
- Keep track of incorrect guesses remaining

### 🛠️ Build the Game Loop

#### Description
Handle player input, update the puzzle state, and finish the game when the player wins or loses.

#### Requirements
Completed program should:

- Accept letter guesses from the player
- Reveal correct letters in the hidden word
- Decrease the number of attempts after incorrect guesses
- End the game when the word is guessed or attempts are exhausted
- Display clear win and lose messages
