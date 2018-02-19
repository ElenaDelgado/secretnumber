#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def main():
    import random
    randomNumber = random.randrange(0,100)
    print("Generado número al azar")
    guessed = False
    while guessed==False:
        userInput = int(input("Tu intento, por favor: "))
        if userInput==randomNumber:
            guessed = True
            print("Bien hecho!")
        elif userInput>100:
            print("El rango es entre 0 y 100")
        elif userInput<0:
            print("El rango es entre 0 y 100")
        elif userInput>randomNumber:
            print("Intentelo otra vez, mas bajo")
        elif userInput < randomNumber:
            print("Intentelo otra vez, mas alto")

    print("Fin")

if __name__ == "__main__":
    main()
