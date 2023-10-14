T = [0] * 50

for i in range(50):
    T[i] = int(input(f"Entrez un entier pour la position {i + 1} : "))

n = int(input("Entrez un entier à rechercher : "))

c = 0  

for i in range(50):
    if T[i] == n:
        c += 1

print(f"Le nombre d'occurrences de {n} dans le tableau est : {c}")
