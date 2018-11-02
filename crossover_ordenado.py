#!/usr/bin/python
# coding: utf-8

import copy
from random import randint

def crossover_ordenado(pai, mae):
        # filho que recebera genes do pai e da mae, começa sendo uma copia do pai
    filho = copy.copy(pai)

    # lista da posicao de k elementos aleatorios em ordem
    p = []

    # subconjunto com os k elementos de p1 correspondentes as posicoes na lista p
    s = []

    # indices dos elementos de s ordenados em relacao a suas posicoes em p2
    p_ord = []

    # loop responsavel por inserir dados em p
    for x in range(0, randint(1, len(pai))):
        # Gera numero randomico para ser colocado em p
        num_random = randint(0, len(pai)-1)
        # Verifica se o numero gerado nao esta na lista
        if num_random not in p:
            p.append(num_random)
    # Ordena a lista da posicao de k elementos
    p.sort()

    # loop responsavel por inserir dados em s
    for x in p:
        s.append(pai[x])

    # loop responsavel por inserir em p_ord
    for x in mae:
        if x in s:
            p_ord.append(s.index(x))

    # coloca genes da mae no filho
    for i in range(len(s)):
        filho[p[i]] = s[p_ord[i]]

    return filho
