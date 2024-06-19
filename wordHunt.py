import random

hangmanDrawing = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
                  '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
                  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
                  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
                  '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
                  '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
                  '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

wordList = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
            'coyote crow deer dog donkey duck eagle ferret fox frog goat '
            'goose hawk lion lizard llama mole monkey moose mouse mule newt '
            'otter owl panda parrot pigeon python rabbit ram rat raven '
            'rhino salmon seal shark sheep skunk sloth snake spider '
            'stork swan tiger toad trout turkey turtle weasel whale wolf '
            'wombat zebra ').split()


def game():
    # Game conditions
    solved = False
    lost = False

    # Randomly select word
    selectedWord = random.choice(wordList)
    hiddenWord = list('_' * len(selectedWord))
    print(hiddenWord)
    guessedLetters = set()

    # Keep trak of guesses and how many times to draw
    drawingCount = 0
    guessCount = 0

    # While either condition is not met
    while not solved and not lost:
        letter = input("Enter letter: ").lower()  # Convert input to lowercase

        # If letter already guessed
        if letter in guessedLetters:
            print(f"{hangmanDrawing[drawingCount]} \n")
            drawingCount += 1
            print(f"You already guessed '{letter}'. Try a different letter.\n")
            print(hiddenWord)
        else:
            guessedLetters.add(letter)
            if letter not in selectedWord:
                print("WRONG!\n")
                print(hangmanDrawing[drawingCount])
                guessCount += 1
                drawingCount += 1
                print(hiddenWord)
            else:
                for i in range(len(selectedWord)):
                    if selectedWord[i] == letter:
                        hiddenWord[i] = letter
                print(hiddenWord)
                guessCount += 1

        # If the user completes the word
        if hiddenWord == list(selectedWord):
            print(
                f"\nCongratulations! The correct word was '{selectedWord}' and you guessed it in {guessCount} attempts.")
            solved = True
        # If the drawing is full
        elif hangmanDrawing == 6:
            print(f"Unfortunately you lose! The correct word was '{selectedWord}'.")
            lost = True


game()
