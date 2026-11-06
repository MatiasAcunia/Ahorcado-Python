class HangmanGame:
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

  if letter not in self.sectret_word:
    self.errors += 1
    return False
  return True

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
