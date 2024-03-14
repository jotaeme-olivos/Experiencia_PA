import random
def adivinar_par_o_impar():
    eleccion = input(f"Ingresa tu elección, 'par' o 'impar': ")
    numero = random.randint(0,100)
    resultado = numero % 2
    if resultado == 0:
        if eleccion == "par":
            print(f"El número es {numero} y es par. ¡Adivinaste!")
        else:
            print(f"El número es {numero} y es par. No adivinaste.")
    else:
        if eleccion == "impar":
            print(f"El número es {numero} y es impar. ¡Adivinaste!")
        else:
            print(f"El número es {numero} y es impar. No adivinaste.")
    pass
