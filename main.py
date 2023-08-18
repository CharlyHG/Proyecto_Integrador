import os

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


        