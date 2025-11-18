#Computer Seminar - Strings
# Excercise 1.
1. print(pizza[0]) - H
2. print(pizza[:5])- Hawai
3. print(pizza[0:2]) - Ha
4. print(" pizza[6]" ) - pizza[6]
5. print(pizza) - Hawaiian
6. print(pizza[6]) - a
7. print(pizza[2:4]) - wa
8. print(pizza[3:])- aiian
9. print(pizza[-1]) - n
10. print(pizza[:-1]) - Hawaiia

# Exercise 2: String Indexing and Slicing

# Ask user for their full name
full_name = input("Enter your full name: ")

# a. The whole name
print("Whole name:", full_name)

# b. The first character
print("First character:", full_name[0])

# c. The first 5 characters
print("First 5 characters:", full_name[:5])

# d. The fourth, fifth, and sixth characters
# Indexing starts from 0, so 4th is index 3, 5th is index 4, 6th is index 5
print("Fourth, fifth and sixth characters:", full_name[3], full_name[4], full_name[5])

# Exercise 3: Length of a string - len()

# Ask user for a username of exactly 6 characters
username = input("Enter a username (6 characters): ")

# Check the length and display the result
if len(username) == 6:
    print("You entered six characters.")
else:
    print("You did NOT enter six characters.")

# Exercise 4: Apply string methods lower(), upper(), and capitalize()

str_value = 'cosc001W'

# Apply and print the results line by line
print(str_value.lower())
print(str_value.upper())
print(str_value.capitalize())

###Exercise 5 - One common task is to remove white space (spaces, tabs, or newlines) from the
###beginning and end of a string using the strip method. Run the following to check the output.
line = ' more white space '
print(line)
print(line.strip())
print(line)

### Guess the Word Game - part 1

# Store the secret word
secret = 'water'

# Number of turns allowed
turns = 6

# String to keep track of all guesses
guesses = ''

# Introduction
print("Welcome to 'Guess the Word' game!")
print(f"You have {turns} turns to guess the word.")
print("The word has", len(secret), "letters.")
print("_ " * len(secret))  # Display underscores for each letter

while turns > 0:
    # Current state of guessed word
    display_word = ''
    for letter in secret:
        if letter in guesses:
            display_word += letter + ' '
        else:
            display_word += "_ "
    print("\nCurrent word:", display_word.strip())

    # Get user guess
    guess = input("Guess a letter: ").lower()

    # Check for single letter input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Add guess to guesses
    if guess not in guesses:
        guesses += guess
    else:
        print("You already guessed that letter.")
        continue

    # Check guess
    if guess in secret:
        print("Good guess!")
    else:
        turns -= 1
        print("Wrong guess.")
        print(f"You have {turns} turns left.")

    # Check if word is completely guessed
    found = True
    for letter in secret:
        if letter not in guesses:
            found = False
            break
    if found:
        print(f"\nCongratulations! You guessed the word: {secret}")
        break

# If out of turns
if not found:
    print(f"\nGame Over! The word was: {secret}")

# Guess the Word Game - Part 2

# Store the secret word
secret = 'water'

# Number of turns allowed
turns = 6

# String to keep track of all guesses
guesses = ''

print("Let's play Guess the Word")
print(f"You have {turns} turns to guess the word!")
print("_ " * len(secret))  # Display underscores for each letter

while turns > 0:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()
    
    # Store the guess in guesses variable
    guesses += guess

    # Show currently guessed letters and underscores for missing ones
    for letter in secret:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

    # End of game message (only one guess per run, as per provided example)
    print("End of Game")
    break  # End after one guess as in the example.

 Guess the Word Game - Part 3

secret = 'water'
turns = 6
guesses = ''

print("Let's play Guess the Word")
print(f"You have {turns} turns to guess the word!")
print("_ " * len(secret))  # Show underscores at start

while turns > 0:
    guess = input("Guess a letter: ").lower()
    guesses += guess
    turns -= 1

    # Show progress
    for letter in secret:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()

print("End of Game")

 Guess the Word Game - Part 4,5,6

import random

# List of possible secret words
words = ['water', 'python', 'robot', 'science', 'apple', 'school']

# Pick a random word from the list
secret = random.choice(words)

# Set number of turns based on length of the secret word
turns = len(secret)

# String to keep track of all guesses
guesses = ''

print("Let's play Guess the Word")
print(f"The secret word has {len(secret)} letters.")
print(f"You have {turns} turns to guess the word!")
print('_ ' * len(secret))  # Show underscores for each letter at the start

while turns > 0:
    guess_input = input("Guess a letter: ").strip()
    # Take just the first character if the user enters more than one
    if guess_input == "":
        print("Please enter a letter!")
        continue
    guess = guess_input[0].lower()  # Always work with lowercase

    # Add the guess to the guesses string (if not already guessed)
    if guess not in guesses:
        guesses += guess
    else:
        print("You already guessed that letter.")



    # Display the current state (letters or underscores)
    found = True
    display = ''
    for letter in secret:
        if letter.lower() in guesses:
            display += letter + ' '
        else:
            display += '_ '
            found = False
    print(display.strip())

    # Check for win
    if found:
        print(f"Congratulations! You guessed the word: {secret}")
        break

    turns -= 1
    print(f"Turns left: {turns}")

if not found and turns == 0:
    print(f"Game Over! The word was: {secret}")

 Improved Guess the Word Game: part - 7,8

import random

# List of possible secret words
words = ['water', 'python', 'robot', 'science', 'apple', 'school']
secret = random.choice(words)
turns = len(secret)  # Number of turns equals word length
guesses = ''

print("Let's play Guess the Word")
print(f"The secret word has {len(secret)} letters.")
print(f"You have {turns} turns to guess the word!")
print('_ ' * len(secret))  # Show underscores for each letter

while turns > 0:
    guess_input = input("Guess a letter: ").strip()
    if guess_input == "":
        print("Please enter a letter!")
        continue
    guess = guess_input[0].lower()  # Only take the first character, normalize case

    # Add the guess only if it hasn't been guessed yet
    if guess not in guesses:
        guesses += guess
    else:
        print("You already guessed that letter.")

    # Display the current state and count dashes (missed letters)
    missed = 0
    display = ""
    for letter in secret:
        if letter.lower() in guesses:
            display += letter + " "
        else:
            display += "_ "
            missed += 1
    print(display.strip())

    # Win condition: no dashes printed
    if missed == 0:
        print(f"Congratulations! You guessed the word: {secret}")
        break

    # Lose a turn ONLY if guess is not in secret
    if guess not in secret:
        turns -= 1
        print(f"Wrong guess. Turns left: {turns}")

if turns == 0 and missed != 0:
    print(f"Game Over! The word was: {secret}")
