# Hangman Game

This Python project is a console-based implementation of the classic Hangman game. The game selects a random word from a predefined list, and the player attempts to guess the word one letter at a time with a limited number of incorrect attempts allowed.

## Project Overview

The Hangman game provides a fun, interactive way to test and improve vocabulary and pattern recognition skills. This version is implemented entirely in Python and includes features such as random word selection, tracking of guessed letters, input validation, and a summary of attempts left.

### Features

- **Random Word Selection**: Each game uses a randomly chosen word from a predefined list, ensuring a new challenge each time.
- **Limited Attempts**: Players are limited to six incorrect guesses before the game ends, adding an element of challenge.
- **Progress Display**: Shows correctly guessed letters in the word and displays underscores for letters not yet guessed, helping players track progress.
- **Guessed Letters Tracking**: Keeps a record of all guessed letters to prevent duplicate guesses.
- **Endgame Messages**: Displays a congratulatory message if the word is successfully guessed or reveals the word if the player runs out of attempts.

## Project Structure

The main components of the Hangman game include:

- **`words`**: A list of possible words for the game, from which one is randomly selected.
- **`attempts`**: A counter to track the player’s remaining incorrect guesses.
- **`guessed_word`**: A list that reveals the player’s progress, showing correctly guessed letters.
- **`guessed_letters`**: A set that records all letters guessed, helping prevent duplicate guesses.

This structure allows the game to provide real-time feedback and maintain a smooth, interactive experience.

## Requirements

- Python 3.x


---

This Hangman game project is a great way to practice Python programming skills and create an interactive experience for players.
