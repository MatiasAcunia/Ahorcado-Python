import json
from pathlib import Path
from game import Jugador
import secrets
import hashlib

def cargar_jugadores():
    archivo = Path(__file__).resolve().parent / "players.json"

    if not archivo.exists():
        return {}

    with open(archivo, "r", encoding="utf-8") as f:
        datos = json.load(f)
        jugadores = {}
        for email, datos_jugador in datos.items():
            jugador = Jugador.from_dict(datos_jugador)
            jugadores[email] = jugador
    return jugadores

def guardar_jugadores(jugadores):
    archivo = Path(__file__).resolve().parent / "players.json"
    datos = {}
    for email, datos_jugador in datos.items():
        datos[email] = datos_jugador.to_dict()
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent = 4)

def registrar_jugador(jugadores, email, nombre, password):
    email = email.strip().lower()
    if email in jugadores:
        return False
    salt = secrets.token_bytes(16)
    password_Hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 600_000)
    salt = salt.hex()
    password_Hash = password_Hash.hex()
    jugador = Jugador(email, nombre, password_Hash, salt)
    jugadores[email] = jugador
    guardar_jugadores(jugadores)
    return True

def iniciar_sesion(jugadores, email, password):
    email = email.strip().lower()
    if email not in jugadores:
        return None
    jugador = jugadores[email]
    contraseniaCorrecta = jugador.verificar_password(password)
    if contraseniaCorrecta:
        return jugador
    else:
        return None

def obtener_leaderboard(jugadores):
    ranking = sorted(jugadores.values(), key=lambda j: j.puntos, reverse=True)
    return ranking