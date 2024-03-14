def cachipun():
    import random
    posibilidades = ["piedra", "papel", "tijera"]
    jugada_1 = input("cual es tu movimiento? ")
    indice = random.randint(0,2)
    jugada_pc = posibilidades[indice]
    print("Computador escogió", jugada_pc)
    if jugada_1 == "piedra":
        
        if jugada_pc == "papel":
            
            print("PERDISTE")
        if jugada_pc == "tijera":
            
            print("GANASTE")
        if jugada_pc == "piedra":
            
            print("EMPATE")
        
    elif jugada_1 == "papel":
        if jugada_pc == "papel":
            print("EMPATE")
        if jugada_pc == "tijera":
            print("PERDISTE")
        if jugada_pc == "piedra":
            print("GANASTE")
        
    elif jugada_1 == "tijera":
        if jugada_pc == "papel":
            print("GANASTE")
        if jugada_pc == "tijera":
            print("EMPATE")
        if jugada_pc == "piedra":
            print("PERDISTE")


