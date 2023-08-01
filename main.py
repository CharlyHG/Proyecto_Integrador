print("Nombre del jugador")
jugador = input()
print(f"Estamos muy felices de tenerte {jugador},git ¡Bienvenido a tu nuevo equipo! Estamos muy felices de que formes parte del juego. ¡Qué alegría tenerte con nosotros, bienvenido {jugador}!")

import readchar

while True:
    keypress = readchar.readkey()
    print(keypress)
    if keypress == readchar.key.UP:
        break
   