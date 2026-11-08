import hashlib
import hmac

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

class Jugador:
    def __init__(self, email, nombre, password_hash, salt):
        self.email = email.strip().lower()
        self.nombre = nombre
        self.password_hash = password_hash
        self.salt = salt
        self.puntos = 0
        self.partidas = 0
        self.victorias = 0
        self.derrotas = 0

    def verificar_password(self, password):
      salt = bytes.fromhex(self.salt)
      hash_guardado = bytes.fromhex(self.password_hash)

      hash_ingresado = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000
      )

      return hmac.compare_digest(hash_ingresado, hash_guardado)

    def registrar_victoria(self, puntos):
      self.victorias += 1
      self.partidas += 1
      self.puntos += puntos

    def registrar_derrota(self):
      self.derrotas += 1
      self.partidas += 1

    def to_dict(self):
      return {
        "email": self.email,
        "nombre": self.nombre,
        "password_hash": self.password_hash,
        "salt": self.salt,
        "puntos": self.puntos,
        "partidas": self.partidas,
        "victorias": self.victorias,
        "derrotas": self.derrotas
    }

    @classmethod
    def from_dict(cls, data):
      jugador = cls(
        data["email"],
        data["nombre"],
        data["password_hash"],
        data["salt"]
      )

      jugador.puntos = data["puntos"]
      jugador.partidas = data["partidas"]
      jugador.victorias = data["victorias"]
      jugador.derrotas = data["derrotas"]

      return jugador

