#!/usr/bin/python
# coding: utf-8

import copy
from random import randint
import random

# Mutacao de um individuo com 1 genes
def mutacao2(individuo):
    individuo_mutado = copy.copy(individuo)
    x = random.randint(0, len(individuo_mutado)-1)
    y = random.randint(0, len(individuo_mutado)-1)

    # Troca a posicao entre dois individuos
    temp = individuo_mutado[x]
    individuo_mutado[x] = individuo_mutado[y]
    individuo_mutado[y] = temp

    return individuo_mutado
