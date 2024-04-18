import random

# Sample word bank
word_bank = {
  'Animals': ['tiger', 'elephant', 'kangaroo'],
  'Fruits': ['apple', 'banana', 'orange']
}

# Just For title and Show first Menu
class Game:
  def __init__(self, title):
    self.title = title

  def display_instructions(self):
    print(f"\nWelcome to {self.title} Game!")
    print("Guess the word letter by letter and win a prize! You have a limited number of incorrect guesses\n")

# Define Choose Bank,Category,Word,Displayed Word in Menu,Incorrect Guess, Amount of try
class Hangman(Game):

  def __init__(self, title, word_bank):
    super().__init__(title)
    self.word_bank = word_bank
    self.chosen_category = None
    self.chosen_word = None
    self.displayed_word = None
    self.incorrect_guesses = []
    self.lives = 6

# Randomly select a Category and Word
  def choose_word(self):
    self.chosen_category = random.choice(list(self.word_bank.keys()))
    self.chosen_word = random.choice(self.word_bank[self.chosen_category])

# Create a list with underscores representing the word      
    self.displayed_word = ["_" for _ in self.chosen_word] 

# Convert guess to lowercase
  def handle_guess(self, guess):
    guess = guess.lower()  

# Check if guess is valid (a single letter)
    if len(guess) != 1 or not guess.isalpha():
      print("Invalid guess. Please enter a single letter.")
      return

# Check if guess has already been made
    if guess in self.incorrect_guesses:
      print(f"You already guessed '{guess}'. Try again.")
      return

    # Check if guess is in the word
    if guess in self.chosen_word:
    # Update displayed word with correct guess
      for i, letter in enumerate(self.chosen_word):
        if letter == guess:
          self.displayed_word[i] = guess
    else:
    # Incorrect guess, add to incorrect guesses and decrease lives
      self.incorrect_guesses.append(guess)
      self.lives -= 1
      print(f"Incorrect guess. You have {self.lives} lives left.")

  #Check Lose or Win
  def check_win_lose(self):
    # Win condition: all letters guessed correctly
    if "".join(self.displayed_word) == self.chosen_word:
      print(f"Congratulations! You guessed the word '{self.chosen_word}'!")
      return True

    # Lose condition: no lives left
    if self.lives == 0:
      print(f"Oh no! You ran out of lives. The word was '{self.chosen_word}'.")
      return True
    return False


  def play(self):
    self.display_instructions()
    self.choose_word()

    while True:
      # Display the current state of the game
      print(f"Category: {self.chosen_category}")
      print(f"Word: {' '.join(self.displayed_word)}")
      print(f"Incorrect guesses: {', '.join(self.incorrect_guesses) if self.incorrect_guesses else 'None'}")

      # Get player guess
      guess = input("Guess a letter: ")

      self.handle_guess(guess)

      # Check win/lose condition and break loop if game is over
      if self.check_win_lose():
        break


# Create and play the Hangman game
game = Hangman("Hangman", word_bank)
game.play()      

