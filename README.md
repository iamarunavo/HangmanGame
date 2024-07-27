# HangmanGame
Hangman Game
Welcome to the Hangman game! This classic word guessing game challenges players to guess a hidden word by suggesting letters or the entire word within a limited number of tries.

How It Works
Game Setup:

The game selects a random word from a predefined list.
The player has a maximum of 6 tries to guess the word.
Players can guess one letter or the entire word per turn.
Gameplay:

The word is represented as underscores (_) initially.
Players input their guesses.
Correct guesses reveal letters in their positions.
Incorrect guesses reduce the number of remaining tries.
The game ends when the player either correctly guesses the word or runs out of tries.
Game Display:

The game displays a hangman graphic showing the current state of the drawing based on remaining tries.
It also shows the current progress of the guessed word.
Files
hangman.py: Contains the main game logic, including word selection, gameplay, and display functions.
words.py: Contains the list of words used in the game.
