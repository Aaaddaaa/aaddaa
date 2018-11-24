import os
import random
while True:
    print("Menu, info o autorze = a")
    print("Gra wciśnij b")
    print("wyjście, q")
    wybor = input()
    if wybor == "a":
        print("Ada Pilarska")
        print("Naciśnij aby kontynuować")
        input()
        os.system('cls')
    elif wybor == "q":
        break
    elif wybor == "b":
        print("Gra, aby przerwać wciśnij q")
        kasa = 10
        while True:
            print("jednoręki bandyta \nNaciśnij aby kontynuować")
            key = input()
            if key == "q":
                break
            else:
                los1 = random.randint(1,10)
                print(los1)
                los2=random.randint(1,10)
                print(los2)
                los3 = random.randint(1,10)
                print(los3)
                if los1 == los2 and los1 == los3:
                    print("Wygrana!")
                    kasa +=10
                elif los1 == los3 or los2 == los3 or los1 == los2:
                    print("Prawie wygrana!")
                    kasa +=2
                else:
                    print("próbuj dalej")
                print("Naciśnij aby kontynuować")
                input()
                os.system('cls')
                print("kasa:", kasa)
    else:
        print("zły klawisz")
