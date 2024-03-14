import random

def memoria():
    sequence = [random.randint(1, 100) for _ in range(4)]
    print(f"La secuencia a memorizar es la siguiente: {sequence}")
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))
    c = int(input("Ingresa el tercer número: "))
    d = int(input("Ingresa el cuarto número: "))

    lista_nueva = [a, b, c, d]
    if lista_nueva == sequence:
        print(f"Correcto! La secuencia era {sequence}")
    else:
        print(f"Incorrecto, la secuencia era {sequence}")
    pass