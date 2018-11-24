

import os
data = [0,1,2,3,4,5]
pomiar = [19,11,12,13,14,15]
while True:
    print("Menu:")
    print("Informacja o autorze, wybierz a")
    print("wyjście, wybierz q")
    print("smog i info, wybierz cokolwiek")
    decyzja = input()
    os.system('cls')


    if decyzja == "a":

        print("Ada Pilarska")
    elif decyzja == "q":
        break
    else:

        print("Smog")

        while True:
            print("wyświetlenie informacji o smogu dzisiaj, wybierz a")
            print("Dodawanie pomiarow, wybierz b")
            print("Usunięcie pomiarów, wybierz c")
            print("minimalna wartość, wybierz d")
            print("maksymalna wartość wybierz e")
            print("wyjście, dowolny klawisz")
            wybor = input()
            os.system('cls')
            if wybor == "a":
                print("podaj datę, jaką wyświetlamy")
                dzien = int(input())
                print("Data pomiaru to:",data[dzien],"Wartość:", pomiar[dzien])
            elif wybor == "b":
                print("podaj datę pomiaru")
                data1 = int(input())
                data.append(data1)
                print("podaj wartość pomiaru")
                pom1 = int(input())
                pomiar.append(pom1)
                for i in range(len(data)):
                    print(data[i], pomiar[i])
            elif wybor == "c":
                print("podaj dzien do usunięcia")
                usuwanie = int(input())
                print("podaj dzien do usunięcia")
                usuwanie = int(input())
                databez = data[:]
                pomiarbez = pomiar[:]
                for i in databez:
                    if i == usuwanie:
                        databez.remove(i)

                print("podaj pomiar do usunięcia")
                usuniecie = int(input())
                for i in pomiarbez:
                    if i == usuniecie:
                        pomiarbez.remove(i)
                for j in range(len(pomiarbez)):
                    print(pomiarbez[j], data[j])


            elif wybor == "d":
                print("maksymalna wartość pomiarów to:")
                maks = 0
                for i in range(len(pomiar)):
                    if maks < pomiar[i]:
                        maks = pomiar[i]
                print(maks)
            elif wybor == "e":
                print("minimalna wartość pomiarów to:")
                min = pomiar[0]
                for i in range(len(pomiar)):
                    if min > pomiar[i]:
                        min = pomiar[i]
                print(min)
            else:
                break
