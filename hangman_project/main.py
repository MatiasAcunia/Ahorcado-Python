import os
import sys
from getpass import getpass

from game import HangmanGame
from players_manager import (
    cargar_jugadores,
    guardar_jugadores,
    registrar_jugador,
    iniciar_sesion,
    obtener_leaderboard,
)
from utils import calcular_puntos, get_random_word, load_word_from_file, validate_input


def limpiar_pantalla():
  if sys.stdout.isatty() and (os.name == "nt" or os.getenv("TERM")):
    os.system("cls" if os.name == "nt" else "clear")


def esperar_menu():
  input("\nPresioná Enter para volver al menú...")


def main():
  jugadores = cargar_jugadores()
  wordlist_path = os.path.join(os.path.dirname(__file__), "wordlist.txt")
  words = load_word_from_file(wordlist_path)
  jugador_actual = None

  while True:
    limpiar_pantalla()
    print("¡Bienvenido al juego del Ahorcado!\n")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Ver leaderboard")
    print("4. Jugar")
    print("5. Cerrar sesión")
    print("0. Salir")

    numero = input("\nIngresá la opción correspondiente: ").strip()
    if numero not in ("0", "1", "2", "3", "4", "5"):
      print("\nOpción incorrecta. Elegí una opción del menú.")
      esperar_menu()
      continue
    elif numero == "0":
      print("\n¡Hasta la próxima!")
      break
    elif numero == "1":
      email = input("\nIngresá tu email: ")
      nombre = input("Ingresá tu nombre: ")
      password = getpass("Ingresá tu contraseña: ")
      validacion = registrar_jugador(jugadores, email, nombre, password)
      if validacion:
        print("\n¡Registro exitoso! Ya podés iniciar sesión.")
      else:
        print("\nEse email ya está registrado.")
    elif numero == "2":
      if jugador_actual is None:
        email = input("\nIngresá tu email: ")
        password = getpass("Ingresá tu contraseña: ")
        jugador_actual = iniciar_sesion(jugadores, email, password)
        if jugador_actual is not None:
          print(f"\n¡Sesión iniciada! Bienvenido, {jugador_actual.nombre}.")
        else:
          print("\nEmail o contraseña incorrectos.")
      else:
        print("\nYa hay una sesión iniciada. Cerrala primero.")
        esperar_menu()
        continue
    elif numero == "3":
      ranking = obtener_leaderboard(jugadores)
      print("\n=== LEADERBOARD ===")
      if not ranking:
        print("Todavía no hay jugadores registrados.")
      for posicion, jugador in enumerate(ranking, start=1):
        partidas = jugador.victorias + jugador.derrotas

        print(f"{posicion}. {jugador.nombre}")
        print(f"   Puntos: {jugador.puntos}")
        print(f"   Partidas: {partidas}")
        print(f"   Victorias: {jugador.victorias}")
        print(f"   Derrotas: {jugador.derrotas}\n")
        
    elif numero == "4":
      if jugador_actual is None:
        print("\nDebés iniciar sesión para jugar.")
        esperar_menu()
        continue
      while True:

        secret = get_random_word(words)
        game = HangmanGame(secret)

        while not game.is_won() and not game.is_lost():
          limpiar_pantalla()

          print(game.HANGMAN_STAGES[game.errors])
          print(f"\nPalabra: {game.get_masked_word()}")
          print(f"Errores: {game.errors} / {game.max_errors}")
          print(f"Letras intentadas: {', '.join(sorted(game.guessed_letters))}")

          letter = None
          while letter is None:
            user_input = input("Adiviná una letra: ")
            letter = validate_input(user_input, game.guessed_letters)
          game.guess(letter)
        limpiar_pantalla()
        print(game.HANGMAN_STAGES[game.errors])
        if game.is_won():
          print(f"¡Felicitaciones! Has ganado. La palabra era: {game.secret_word}")
          puntos = calcular_puntos(game.secret_word, game.errors)
          jugador_actual.registrar_victoria(puntos)
          print(f"Sumaste {puntos} puntos.")
        else:
          print(f"¡Te has quedado sin intentos! Has perdido. La palabra era: {game.secret_word}")
          jugador_actual.registrar_derrota()
        guardar_jugadores(jugadores)
        print("-----------------------------------")

        respuesta = input("¿Querés volver a jugar? (s/n): ").strip().lower()

        if respuesta != "s":
          break
    elif numero == "5":
      if jugador_actual is None:
        print("\nNo hay ninguna sesión iniciada.")
      else:
        jugador_actual = None
        print("\nSesión cerrada correctamente.")
    esperar_menu()


if __name__ == "__main__":
  main()

