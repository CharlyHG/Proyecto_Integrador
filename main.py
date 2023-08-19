import os
import readchar
# Parte 3
num= 0
while num < 51:
    print(num)
    num = num + 1
    entry = input("Deseas terminar el conteo ? Y/N ")
    if entry == "n":
        os.system('cls' if os.name=='nt' else 'cls')
    if entry == "y":
        break
    
# Parte 4
laberinto = "..###################\n..........#.#.....#.#\n#.###.#####.#.#.###.#\n#...#.........#.....#\n#.#######.#.###.#.###\n#.#.......#.#...#...#\n#.#.#####.###.#.#.#.#\n#.#...#...#...#.#.#.#\n#.#####.#####.#.#####\n#.#.#...#.....#.....#\n###.#.#####.#######.#\n#.......#.#...#.....#\n#.#######.#.###.###.#\n#.#...#.......#.#.#.#\n#####.#####.#.###.###\n#.#.........#...#.#.#\n#.###.###.#####.#.#.#\n#.#...#...#.......#.#\n#.#.###.#####.#.#.#.#\n#.....#...#...#.#...#\n###################.."

laberinto_split = list(laberinto.split("\n"))

matriz = []

for fila in laberinto_split:
    matriz.append(list(fila))

def imprimir_matriz(mapa):
    os.system('cls' if os.name=='nt' else 'cls')
    for filas in mapa:
        print(''.join(filas))

def main_loop(mapa, posicion_inicial, posicion_final):
    px = posicion_inicial[0]
    py = posicion_inicial[1]

    mapa[px][py] = "p"
    imprimir_matriz(mapa)
    print("\n" +"posición: " + str(px) + ", " + str(py))

    while True:
        i = readchar.readkey()
        if i == readchar.key.UP:
            if 0 < px <= len(mapa):
                if mapa[px - 1][py] != "#":
                    mapa[px][py] = "."
                    px -= 1
        elif i == readchar.key.DOWN:
            if 0 <= px < len(mapa) - 1:
                if mapa[px + 1][py] != "#":
                    mapa[px][py] = "."
                    px += 1 

        elif i == readchar.key.LEFT:
            if 0 < py <= len(mapa[px]):
                if mapa[px][py - 1] != "#":
                    mapa[px][py] = "."
                    py -= 1 
        
        elif i == readchar.key.RIGHT        :
            if 0 <= py < len(mapa[px]) - 1:
                if mapa[px][py + 1] != "#":
                    mapa[px][py] = "."
                    py += 1 

        mapa[px][py] = "p"
        imprimir_matriz(mapa)
        print("\n" + "posición: " + str(px) +","+ str(py))

        if px == posicion_final[0] and py == posicion_final[1]:
            print("felicidades")
            break

main_loop(matriz, (0, 0), (20, 20))


        