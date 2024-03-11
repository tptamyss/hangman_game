
def play_hangman(secretWord):
  print("Welcome to the game Hangman!")
  word = secretWord.lower()
  word_length = len(word)
  word_progress = ["_"] * word_length

  lettersGuessed = set()  # Store guessed letters
  mistakesMade = 0
  availableLetters = set("abcdefghijklmnopqrstuvwxyz")

  print(f"I am thinking of a word that is {word_length} letters long.")

  while mistakesMade < 8:
    print(" ".join(word_progress))
    print(f"Available letters: {''.join(availableLetters)}")

    guess = input("Guess a letter: ").lower()
    if guess in availableLetters:
      availableLetters.remove(guess)
      lettersGuessed.add(guess)  # Add guess to tracked letters
      if guess in word:
        # Update word progress
        for i in range(word_length):
          if word[i] == guess:
            word_progress[i] = guess
        if word_progress == list(word):
          print(" ".join(word_progress))
          print("Congratulations, you won!")
          break
      else:
        print("Oops! That letter is not in my word.")
        mistakesMade += 1  # Increment mistakes on wrong guess
    else:
      print(f"Oops! You've already guessed the letter '{guess}'.")

  if mistakesMade == 8:
    print(" ".join(word_progress))
    print(f"Sorry, you ran out of guesses. The word was: {word}")

