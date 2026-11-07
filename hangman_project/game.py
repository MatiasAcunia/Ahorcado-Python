class HangmanGame:
  HANGMAN_STAGES = [
    r"""  +---+
  |   |
      |
      |
      |
      |
=========""",

    r"""  +---+
  |   |
  O   |
      |
      |
      |
=========""",

    r"""  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",

    r"""  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",

    r"""  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",

    r"""  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",

    r"""  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]
  def __init__(self, word):
    self.secret_word = word.lower()
    self.guessed_letters = set()
    self.max_errors = 6
    self.errors = 0

  def guess(self, letter):
    letter = letter.lower()
    if letter in self.guessed_letters:
      return False

    self.guessed_letters.add(letter)

    if letter not in self.secret_word:
      self.errors += 1
      return False
    return True

  def process_guess(self, letter):
    if letter in self.secret_word:
      self.guessed_letters.add(letter)
      return True

    else:
      self.errors += 1
      self.guessed_letters.add(letter)
      return False

  def display_progress(self):
    masked = []
    for char in self.secret_word:
      if char.isalpha():
        if char in self.guessed_letters:
          masked.append(char)
        else:
          masked.append("_")

      else:
        masked.append(char)

    return " ".join(masked)


  def is_won(self):
    for char in self.secret_word:
      if char.isalpha() and char not in self.guessed_letters:
        return False

    return True

  def is_lost(self):
    return self.errors >= self.max_errors

  def get_masked_word(self):
    palabra = self.secret_word
    adivinado = self.guessed_letters
    for i, letra in enumerate(palabra):
      if  letra.isalpha() and letra not in adivinado:
        palabra = palabra[:i] + "_" + palabra[i+1:]
    return palabra
    
