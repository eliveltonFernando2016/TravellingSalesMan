import copy
from random import randint
import random

# MUTACAO DE UM INDIVIDUO COM 2 GENES
def mutar_v1(individuo):
    individuo_mutado = copy.copy(individuo)

    # Gerar uma lista com 4 numeros aleatorios nao repetidos entre 0 e o tamanho do individuo
    count = 0
    randomicos = []
    while count != 4:
        temp = random.randint(0, len(individuo_mutado)-1)
        if temp not in randomicos:
            randomicos.append(temp)
            count += 1

    # Trocar a posicao dos genes
    individuo_mutado[randomicos[0]], individuo_mutado[randomicos[1]] = individuo_mutado[randomicos[1]], individuo_mutado[randomicos[0]]
    individuo_mutado[randomicos[2]], individuo_mutado[randomicos[3]] = individuo_mutado[randomicos[3]], individuo_mutado[randomicos[2]]

    return individuo_mutado