# Ahorcado-Python

## 1. Descripción del proyecto

Proyecto UTEC.

Juego de ahorcado desarrollado en Python, interactivo a través de consola. El objetivo es adivinar una palabra antes de llegar a los 6 errores.

También cuenta con un sistema de jugadores, donde cada uno puede registrarse, iniciar sesión, jugar partidas y acumular puntos para aparecer en el ranking.

## 2. Funcionalidades

- En 'wordlist.txt' se encuentran las palabras.
- Las letras ingresadas se validan si se corresponden a la palabra dada o no.
- Se manejan los intentos repetidos.
- Se visualiza el progreso de la palabra.
- Hay revelado automático de espacios y símbolos.
- Se detecta en caso de victoria y derrota.
- Se muestra el dibujo del ahorcado a medida que se cometen errores.
- Se pueden jugar varias partidas sin tener que volver a ejecutar el programa.

También agregamos un sistema de jugadores:

- Cada jugador se puede registrar con su nombre, email y contraseña.
- Se puede iniciar y cerrar sesión.
- Para jugar es necesario tener una sesión iniciada.
- Se guardan los jugadores en un archivo JSON.
- Las contraseñas no se guardan directamente, sino mediante hashes.
- Se registran las victorias, derrotas y puntos de cada jugador.
- Se calculan los puntos obtenidos al ganar una partida.
- Los puntos se van acumulando entre partidas.
- Hay un ranking que muestra a los jugadores ordenados por puntos.
- Los datos quedan guardados aunque se cierre el programa.

## 3. Tecnologías utilizadas

- Python 3.
- Biblioteca estándar de Python.
- JSON para guardar los jugadores.
- Sin dependencias externas.

## 4. Estructura del proyecto

- main.py: ejecución e interacción con el usuario.
- game.py: clases y lógica del juego.
- players_manager.py: funciones para registrar jugadores, iniciar sesión, guardar datos y obtener el ranking.
- utils.py: funciones auxiliares.
- wordlist.txt: palabras y frases disponibles.
- players.json: archivo donde se guardan los jugadores. Se genera automáticamente.

## 5. Instalación y ejecución

Requisito: tener Python 3 instalado.

Para clonar o descargar el repositorio:

Clonar:

    git clone https://github.com/MatiasAcunia/Ahorcado-Python

Descargar:

- Ingresá al repositorio en GitHub.
- Hacé clic en Code → Download ZIP.
- Extraé el archivo ZIP en la carpeta que prefieras.
- Abrí la carpeta 'hangman_project' en Visual Studio Code.

Uso:

Desde la terminal en la carpeta 'hangman_project':

    python3 main.py

En Windows también se puede ejecutar con:

    python main.py

Al ejecutar el programa aparece un menú con las siguientes opciones:

1. Registrarse.
2. Iniciar sesión.
3. Ver ranking.
4. Jugar.
5. Cerrar sesión.
0. Salir.

Primero hay que registrarse o iniciar sesión con una cuenta existente. Después ya se puede jugar normalmente.

## 6. Reglas del juego

- Se necesita iniciar sesión para jugar.
- Se ingresa una letra por turno.
- Solo se aceptan caracteres alfabéticos.
- Las letras repetidas no se aceptan.
- Se permiten hasta 6 errores.
- Se gana al descubrir todas las letras.
- Se pierde al llegar a los 6 errores.
- Al terminar la partida se muestra la palabra que había que adivinar.

Puntuación:

Para calcular los puntos se tiene en cuenta la cantidad de letras diferentes que tiene la palabra y los errores que cometió el jugador.

La fórmula que usamos es:

    puntos = round(100 * letras_diferentes / (letras_diferentes + errores))

- Si se gana sin errores, se obtienen 100 puntos.
- Cuantos más errores se cometan, menos puntos se obtienen.
- Si se pierde, no se suman puntos.
- Los puntos obtenidos se agregan a los que ya tenía el jugador.
- El ranking se ordena según los puntos totales de cada uno.

Al finalizar una partida también se puede elegir si jugar otra o volver al menú.

## 7. Integrantes

- Avril Cabrera.
- Matías Acuña.
- Sofía da Silva (?).
