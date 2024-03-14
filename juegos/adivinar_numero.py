import random

def adivinar_numero():

    Random = random.randint(1,10)

    Usuario = int(input())

    if Usuario == Random:

        print('Adivinaste')

    else:

        print('Te equivocaste, el numero era' , Random)
