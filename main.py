from os.path import exists

size = int(input("Entrez la taille du labyrinthe"))

filename = input("Entrez un nom de fichier")

if not exists(filename):
    file = open(filename, "a+")
    # generation de labyrinthe
    file.close()
else:
    print("File already exists.")