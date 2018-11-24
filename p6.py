#zadanie 1
'''
def sprawdzZeroLubJeden(znak):
    if znak == "1":
        wynik = "prawda"
    elif znak == "0":
        wynik = "prawda"
    else:
        wynik = "fałsz"
    return wynik
liczba = input()
print(sprawdzZeroLubJeden(liczba))
'''
#zadanie 2
'''def nieparzysta(liczba):
    if liczba %2 == 0:
        rezultat = "fałsz"
    else:
        rezultat = "prawda"
    return rezultat
liczba = int(input())
print(nieparzysta(liczba))'''


#zdanie 3

'''def xnor(zmiennaP, zmiennaQ):
    if zmiennaP == 1 or zmiennaP == 0:
        if zmiennaQ == 1 or zmiennaQ == 0:
            print("dobre cyferki")
            if (zmiennaP == zmiennaQ):


                wynik = "prawda"
            else:
                wynik = "fałsz"
        else:
            print("ups")
            wynik = "złe cyferki"


    else:
        print("ups")
        wynik = "złe cyferki"

    return wynik
pierwszy = int(input())
drugi = int(input())
print(xnor(pierwszy,drugi))
'''

'''#zadanie 4
def dodawanieDoListe(lista,liczba):
    listka = []
    for i in range(0,4):
        listka.append(lista[i] + liczba)
        rezultat = listka
    return rezultat
print("utwórz listę")
listeczka = []
for i in range(0,4):
    dodawanie = int(input())
    listeczka.append(dodawanie)
print("teraz o ile dodajemy")
powiększanie = int(input())
print(dodawanieDoListe(listeczka,powiększanie))'''


#zadanie 5
'''def sprawdzSamogloske(znak):
    samogloski=['a','e','i','o','u','y']
    if znak in samogloski:
        wynik = "prawda"
    else:
        wynik = "fałsz"
    return wynik
znaczek = input()
print(sprawdzSamogloske(znaczek))'''
