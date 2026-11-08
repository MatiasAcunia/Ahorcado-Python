import os
from game import HangmanGame
from utils import load_word_from_file, get_random_word, validate_input
from players_manager import cargar_jugadores

def main():
  jugadores = cargar_jugadores()
  wordlist_path = os.path.join(os.path.dirname(__file__), "wordlist.txt")
  words = load_word_from_file(wordlist_path)


  print("¡Bienvenido al juego del Ahorcado!")
  while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver leaderboard")
    print("4. Jugar")
    print("0. Salir")
    while True:

      secret = get_random_word(words) 
      game = HangmanGame(secret)

      while not game.is_won() and not game.is_lost():
        os.system("cls" if os.name == "nt" else "clear")

        print(game.HANGMAN_STAGES[game.errors])
        print(f"\nPalabra: {game.get_masked_word()}")
        print(f"Errores: {game.errors} / {game.max_errors}")
        print(f"Letras intentadas: {', '.join(sorted(game.guessed_letters))}")

        letter = None
        while letter is None:
          user_input = input("Adivina una letra: ")
          letter = validate_input(user_input, game.guessed_letters)
        

        
        game.guess(letter)
        print("\n-----------------------------------")
      
      if game.is_won():
        print(f"¡Felicitaciones! Has ganado. La palabra era: {game.secret_word}")
      else:
        print(f"¡Te has quedado sin intentos! Has perdido. La palabra era: {game.secret_word}")
      print("-----------------------------------")

      respuesta = input("¿Querés volver a jugar? (s/n): ").strip().lower()

      if respuesta != "s":
          break

if __name__ == "__main__":
  main()
