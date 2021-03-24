import random
from words import words
from hangman_level import board

def play_hangman():
  selected_word = random.choice(words).upper()
  guessed_letters = set()
  guessed_word = "_" * len(selected_word)
  lives_remaining = 6

  while lives_remaining > 0 and guessed_word.find("_") != -1:
    print(board[lives_remaining])
    print(f"The word is: {guessed_word}   ||   You've already guessed: {' '.join(guessed_letters)}\n")
    current_guess = input("What letter do you want to guess? ").upper()

    if current_guess in guessed_letters:
      print(f"   You have already guessed this {current_guess}!")

    elif selected_word.find(current_guess) == -1:
      print(f"   {current_guess} is not in the selected word!")
      guessed_letters.add(current_guess)
      lives_remaining = lives_remaining - 1

    else:
      print(f"   {current_guess} is in the selected word!")
      guessed_letters.add(current_guess)
      guessed_word = "".join([x if x in guessed_letters else "_" for x in selected_word])
  
  if lives_remaining == 0:
    print(board[lives_remaining])
    print("Oh no! You ran out of lives!")
    print(f"The word you were guessing was: {selected_word}")
    print("Better luck next time!")

  else:
    print()
    print(f"Congratulations! You correctly guessed the word {selected_word}")
  
play_hangman()