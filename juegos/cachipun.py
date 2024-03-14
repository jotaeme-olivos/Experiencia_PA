import random
    
def cachipun():
<<<<<<< HEAD
    import random
    posibilidades = ["piedra", "papel", "tijera"]
    jugada_1 = input("cual es tu movimiento? ")
=======
    posibilidades = ["piedra", "papel", "tijera"]
    jugada_1 = input(f"Ingresa tu elección: ")
>>>>>>> 40b6a4441f4dbb3a33cc70461142ad04a515a800
    indice = random.randint(0,2)
    jugada_pc = posibilidades[indice]
    if jugada_1 == "piedra":
        if jugada_pc == "papel":
            return "PERDISTE"
        if jugada_pc == "tijera":
            return "GANASTE"
        if jugada_pc == "piedra":
            return "EMPATE"
        
    elif jugada_1 == "papel":
        if jugada_pc == "papel":
            return "EMPATE"
        if jugada_pc == "tijera":
            return "PERDISTE"
        if jugada_pc == "piedra":
            return "GANASTE"
        
    elif jugada_1 == "tijera":
        if jugada_pc == "papel":
            return "GANASTE"
        if jugada_pc == "tijera":
            return "EMPATE"
        if jugada_pc == "piedra":
            return "PERDISTE"
<<<<<<< HEAD


=======
>>>>>>> 40b6a4441f4dbb3a33cc70461142ad04a515a800
