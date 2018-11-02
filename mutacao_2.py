import copy
from random import randint
import random

def mutar_v2(individuo):
    individuo_mutado = copy.copy(individuo)
    # Return a random integer N such that a <= N <= b
    x = random.randint(0, len(individuo_mutado)-1)
    y = random.randint(0, len(individuo_mutado)-1)

    # Troca a posicao entre dois individuos
    temp = individuo_mutado[x]
    individuo_mutado[x] = individuo_mutado[y]
    individuo_mutado[y] = temp

    return individuo_mutado