import os
from game import HangmanGame
from game import Jugador
from utils import load_word_from_file, get_random_word, validate_input
from players_manager import (
    cargar_jugadores,
    guardar_jugadores,
    registrar_jugador,
    iniciar_sesion,
    obtener_leaderboard
)
from getpass import getpass
from utils import calcular_puntos

def main():
  jugadores = cargar_jugadores()
  wordlist_path = os.path.join(os.path.dirname(__file__), "wordlist.txt")
  words = load_word_from_file(wordlist_path)
  jugador_actual = None

  print("¡Bienvenido al juego del Ahorcado!")
  while True:
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver leaderboard")
    print("4. Jugar")
    print("0. Salir")
    print("5. Cerrar sesión")

    numero = input("Ingresa la opción correspondiente: ")
    numero = numero.strip()
    if numero not in ("0", "1", "2", "3", "4"):
      print("Opción incorrecta\n")
      os.system("cls" if os.name == "nt" else "clear")
      continue
    elif numero == "0":
      break
    elif numero == "1":
      email = input("Inserte su email: \n")
      nombre = input("Inserte su nombre: \n")
      password = getpass("Inserte su contraseña: \n")
      validacion = registrar_jugador(jugadores, email, nombre , password)
      if validacion:
        print("Exitoso\n")
      else:
        print("Email ya ingresado\n")
    elif numero == "2":
      if jugador_actual is None:
        email = input("Inserte su email: \n")
        password = getpass("Inserte su contraseña: \n")
        jugador_actual = iniciar_sesion(jugadores, email, password)
        if jugador_actual != None:
          print("Inicio de sesión exitoso: \n")
        else:
          print("Inicio de sesión defectuoso: \n")
      else:
        print("Ya hay una sesión inciada. Cerrala primero.")
        continue
    elif numero == "3":
      ranking = obtener_leaderboard(jugadores)
      for posicion, jugador in enumerate(ranking, start=1):
        print(f"{posicion}. {jugador.nombre} - {jugador.puntos} puntos")
    elif numero == "4":
      if jugador_actual is None:
        print("Debes iniciar sesión para jugar.\n")
        continue
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
          puntos = calcular_puntos(game.secret_word, game.errors)
          jugador_actual.registrar_victoria(puntos)
          guardar_jugadores(jugadores)
        else:
          print(f"¡Te has quedado sin intentos! Has perdido. La palabra era: {game.secret_word}")
          jugador_actual.registrar_derrota()
          guardar_jugadores(jugadores)
        print("-----------------------------------")

        respuesta = input("¿Querés volver a jugar? (con el mismo jugador) (s/n): ").strip().lower()

        if respuesta != "s":
            break
    elif numero == "5":
      if jugador_actual is None:
        print("No hay ninguna sesión iniciada")
      else:
        jugador_actual = None
        print("Sesión cerrada correctamente")
if __name__ == "__main__":
  main()
