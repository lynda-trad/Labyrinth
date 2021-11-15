# Un mur aléatoire est ensuite choisi.
# Si les cellules séparées par ce mur ont des identifiants différents, le même identifiant leur sera associé,
# et il faudra alors abattre le mur.
# Sinon, un autre mur sera choisi.
import random

import Cells

while True:
    try:
        num = int(input("Please enter labyrinth size between 1 and 30\n"))
        if int(num) <= 0 or int(num) > 30:
            continue
        break
    except ValueError:
        print("Please input integer only.")
        continue

mazeSize = num * 2 + 1

cellArray = Cells.initCellArray(mazeSize)

# mur quand i est pair
i = random.randint(2, mazeSize - 2)
while i % 2 != 0:
    i = random.randint(2, mazeSize - 2)
# on a un mur random, on check deux voisins de chaque direction (gauche - droite) ou (haut - bas)
# si le couple a des index differents alors ils auront tous les deux lindex du premier membre
# si ils ont le meme index on prend le couple de lautre direction et on check la 1ere condition

