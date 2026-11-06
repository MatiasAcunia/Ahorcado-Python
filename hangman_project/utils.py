import random

def load_word_from_file(filepath):
  try:
    with open(filepath, "r", encoding="utf-8") as file:
      words = [line.strip() for line in file if line.strip()]
    return words if words else ["python", "ahorcado"]
  except FileNotFoundError:
    return ["python", "ahorcado"]

def get_random_word(words):
  return random.choice(words)

def validate_input(user_input):
  user_input = user_input.strip().lower()
  if len(user_input) != 1 or not user_input.isalpha():
    print("Entrada inválida. Por favor, ingresa solo una letra.")
    return None
  return user_input
  
