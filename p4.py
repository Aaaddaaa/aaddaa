import os
import random
import time

litera = random.choice("qazwse")
print(litera)

start = time.clock()
while True:

    reakcja = input()
    if litera == "a" or litera == "e":
        if reakcja == "a":
            koniec = time.clock()
            break
        else:
            print("zły klawisz")

    else:
        if reakcja == "s":
            koniec = time.clock()
            break
        else:
            print("zły klaiwsz")
litera = random.choice("qazwse")
print(litera)
start1 = time.clock()
while True:

    reakcja = input()
    if litera == "a" or litera =="e":
        if reakcja == "a":
            koniec1 = time.clock()
            break
        else:
            print("zły klawisz")

    else:
        if reakcja == "s":
            koniec1 = time.clock()
            break
        else:
            print("zły klaiwsz")
litera = random.choice("qazwse")
print(litera)
start2 = time.clock()
while True:

    reakcja = input()
    if litera == "a" or litera == "e":
        if reakcja == "a":
            koniec2 = time.clock()
            break
        else:
            print("zły klawisz")

    else:
        if reakcja == "s":
            koniec2 = time.clock()
            break
        else:
            print("zły klaiwsz")
os.system('cls')
czas_trwania = koniec - start
czas_trwania1 = koniec1 - start1
czas_trwania2 = koniec2 - start2
print("Wynik 1:", czas_trwania)
print("wynik 2:", czas_trwania1)
print("wynik 3:", czas_trwania2)

suma = czas_trwania + czas_trwania1 + czas_trwania2
srednia = suma / 3

print("Średnia czasu reakcji:", round(srednia,2))
