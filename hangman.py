# Import necessary libraries
import openai  # Library to interact with OpenAI's API
import os  # Library for working with operating system features like environment variables
from dotenv import load_dotenv  # Library to load environment variables from a .env file
from stages import stages  # Import the stages (visuals) for the Hangman game

# Load environment variables from a .env file (if it exists)
# Todo 1: Load environment variables to access the API key

# Set your OpenAI API key
# Todo 2: Set up your OpenAI API key from environment variables

# Todo 3: Use OpenAI API to get a Dutch word for the game
# - Create a request to the ChatGPT API to get a random Dutch word
# - Store the response in a variable

# Todo 4: Extract the word from the API response and make it lowercase

# Todo 5: Create the Function to run the Hangman game


# Todo 5: Initialize game variables
    # - Set the count of wrong guesses to 0
    # - Create a list of letters left to guess from the word
    # - Create a display board to show guessed letters and underscores for missing ones
    # - Set a flag to track whether the player has won

    # Todo 6: Print a welcome message and the initial state of the board

    # Todo 7: Main game loop
    # - Continue looping while the player has guesses left
    # - Ask the user to guess a letter
    # - Check if the guessed letter is in the list of letters left to guess
    # - If the guess is correct, update the board with the guessed letter
    # - If the guess is incorrect, increment the wrong guess count
    # - Print the current state of the board and hangman
    # - Check if the game is won (no more underscores on the board)

# Todo 8: Get user input for a guess

# Todo 9: Check if the guess is correct
# - Find the indices of the guessed letter in the word
# - Update the board and letters left if the guess is correct
# - Update the wrong guess count if the guess is incorrect

# Todo 10: Print the current state of the board and hangman stages

# Todo 11: Check if the player has won (no underscores left on the board)

# Todo 12: End the game with a loss message if the player hasn't won

# Todo 13: Call the hangman function with the word to start the game

