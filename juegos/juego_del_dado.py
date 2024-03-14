import random

def juego_del_dado():
    puntuacion_usuario=0 
    puntuacion_pc = 0
    while puntuacion_usuario<30 and puntuacion_pc < 30:
        input("Apreta ENTER para lanzar el dado! \n")
        numero = random.randint(1,6)
        print("Sacaste", numero, "\n")
        puntuacion_usuario+=numero

        print("Turno de la computadora \n")
        numero= random.randint(1,6)
        print("La computadora saco", numero, "\n")
        puntuacion_pc+=numero

        print("PUNTUACION ACTUAL:")
        print("---- TU:", puntuacion_usuario)
        print("---- PC:", puntuacion_pc, "\n" )

    if puntuacion_usuario>=30:
        print("GANASTE, tu puntuacion", puntuacion_usuario," puntucion pc", puntuacion_pc)
    else:
        print("PERDISTE :(, puntuacion pc", puntuacion_pc, "tu puntuacion", puntuacion_usuario)
    pass

