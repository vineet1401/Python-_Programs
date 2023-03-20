import random

# ASCII value for displaying lives of hangman
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

# Creating list of random words
word_list = ["vineet", "omraje", "", "snehal", "atharva", "pratik", "nehal"]

# Choosing random word from created list
chosen_word = random.choice(word_list)
# Its optional to display the choosn word for testing
print(chosen_word)
# Creating display list of "_" for entering guesses
display = ["_" for i in range(len(chosen_word))]

# Initiating lives to a player
lives = 6

# applying
cond = True
while (cond):
    print("<----------------------------------------------------------------->")
    guess = (input("Enter Guess : ").lower())  # Entering Guessed letter

    # Checking the guess in the choosen word and replacing the guess with display list
    for i in range(len(chosen_word)):
        if (guess == chosen_word[i]):
            display[i] = guess
    # if guess is not in word reduce lives
    if (guess not in chosen_word):
        lives -= 1
    # when lives is zero you loose
    if (lives == 0):
        print("You Loose")
        cond = False

        # display the lives with the help of hanging man
    print(display)
    print(stages[5-lives])
    print("<----------------------------------------------------------------->")
