import copy
from random import randint
import random

def crossover_alternativo(pai, mae):
    filho = copy.copy(pai)
    corte = random.randrange(1, len(pai)-1)
    for i in range(corte, len(pai)):
        if (pai[i] not in mae[0:i]) and (mae[i] not in pai[0:i]):
            filho[i] = mae[i]

    return filho