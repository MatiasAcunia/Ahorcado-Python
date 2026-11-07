import random

def load_word_from_file(filepath):
  try:
    with open(filepath, "r", encoding="utf-8") as file:
      words = [line.strip() for line in file if line.strip()]
    return words if words else ["python", "ahorcado"]
  except FileNotFoundError:
    return ["python", "ahorcado"]

#Ahora pide la lista como se la dan en main
def get_random_word(words):
  return random.choice(words)

def validate_input(user_input, guessed_letters):
  cleaned_input = user_input.strip().lower()
  if len(cleaned_input) != 1 or not cleaned_input.isalpha():
    print("Entrada inválida. Por favor, ingresa solo una letra.")
    return None

  if cleaned_input in guessed_letters:
    print(f"Error: Ya has intentado la letra '{cleaned_input}'. Prueba con otra")
    return None
  return cleaned_input
  
