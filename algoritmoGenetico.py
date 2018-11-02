#!/usr/bin/python
# coding: utf-8

import math
import numpy as np
from random import randint
import random
import copy
import functools
import matplotlib.pyplot as plt
from crossover_ordenado import crossover_ordenado
from crossover_alternativo import crossover_alternativo
from mutacao_1 import mutar_v1
from mutacao_2 import mutar_v2


# DISTANCIA EUCLIDIANA ENTRE DOIS PONTOS
def dist_euclid(x1, y1, x2, y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))

# CRIA MATRIZ DE DISTANCIA ENTRE OS NOS
def cria_matriz_de_distancia(matriz, tamanho):
    # cria matriz e preenche com 0
    n_matriz = np.zeros((tamanho, tamanho), dtype=float)

    # preenche primeira linha e primeira coluna com o numero do nó
    for row in range(0, tamanho):
        for col in range(0, tamanho):
            if (col == 0 and row == 0):
                n_matriz[row][col] = 0
            if (col == 0 and row != 0):
                n_matriz[row][col] = row
            if (row == 0 and col != 0):
                n_matriz[row][col] = col

    # preenche a n_matriz com as distancias entre os pontos
    for x in range(0, tamanho):
        for i in range(0, tamanho):
            dist = dist_euclid(
                matriz[x][0], matriz[x][1], matriz[i][0], matriz[i][1])
            n_matriz[x][i] = dist

    return n_matriz

# GERA POPULACAO, N = quantidade de genes de cada individuo, tamanho = quantos individuos terá a população
def gen_pop(N, tamanho):
    populacao = []
    individuo = random.sample(range(0, len(N)), tamanho)
    random.shuffle(individuo)
    for x in range(0, tamanho):
        populacao.append(copy.copy(individuo))
        random.shuffle(individuo)

    return populacao

# VERIFICA O CUSTO DO INDIVIDUO
def fitness(individuo, matriz_dist):
    # CUSTO ENTRE O PRIMEIRO NO E O ULTIMO
    custo = matriz_dist[individuo[0]][individuo[len(individuo)-1]]

    # PERCORRE O VETOR INDIVIDUO E CALCULA O CUSTO ENTRE OS NÓS
    for i in range(len(individuo)-1):
        custo = custo + matriz_dist[individuo[i]][individuo[i+1]]

    return custo

# Função auxiliar para computar a FDA (Função de distribuição acumulada)
def acumular(v):
    acum = 0
    r = []
    for i in v:
        r.append(i + acum)
        acum = r[-1]
    return r

# Função de seleção de indivíduo que escolhe com maior probabilidade os indivíduos mais aptos
def selecionar_individuo(pop, f, matriz_dist):
    fits = list(map(lambda x: (1/f(x, matriz_dist)), pop))
    soma = functools.reduce(lambda x, y: x + y, fits)
    norms = list(map(lambda x, y: x / y, fits, [soma] * len(pop)))
    acum = list(acumular(norms))
    r = random.random()
    for i in range(len(acum)):
        if r > acum[i]:
            break
    return pop[i]


# REPRODUCAO DE UM INDIVIDUO


# REPRODUCAO DE UM INDIVIDUO


# Função reproduzir
def reproduzir(pai, mae):
    filho1 = copy.copy(pai)
    filho2 = copy.copy(mae)
    corte = random.randrange(1, len(filho1))
    for i in range(corte, len(filho1)):
        x = pai.index(filho1[i])
        x2 = pai.index(filho2[i])
        y = mae.index(filho1[i])
        y2 = mae.index(filho2[i])
        filho1[x], filho1[y] = filho1[y], filho1[x]
        filho2[x2], filho2[y2] = filho2[y2], filho2[x2]
    return filho1, filho2


# Pega o indice do menor elemento do vetor
def argmin(V):
    menor = 0
    for i in range(1, len(V)):
        if V[i] < V[menor]:
            menor = i
    return menor

# elitismo recebe True ou False para ativar ou desativar respectivamente
# k é a quantidade de geracoes que o algoritmo é executado sem melhora no fit
# tx_mutacao é a probabilidade em porcentagem do individuo receber uma mutação
# reproducao é o tipo de reproducao escolhida, crossover_ordernado = ordenado, crossover_alternativo = qualquer coisa diferente de ordenado.
def algoritmo_genetico(pop_inicial, f, matriz_dist, k, tx_mutacao, elitismo, reproducao, tipo_mutacao):
    # Contador de gerações
    geracao = 0

    max_fits = []
    med_fits = []
    # Faz uma cópia da população inicial
    pop = copy.copy(pop_inicial)

    # Calcula o fitness de todos os individuos da população e coloca em uma lista
    fit = list(map(lambda x: f(x, matriz_dist), pop))

    # Calcula o individuo mais fit da população inicial
    mais_fit = pop[argmin(fit)]

    # Armazena a melhor solução encontrada
    melhor_solucao = mais_fit

    # Enquanto nao passar k geracoes desde a ultima melhora, então:
    while (geracao < k):
        p_nova = []
        for i in range(len(pop)-1):
            x = selecionar_individuo(pop, f, matriz_dist)
            y = selecionar_individuo(pop, f, matriz_dist)

            if(reproducao == 'ordenado'):
                novo = crossover_ordenado(x, y)
            else:
                novo = crossover_alternativo(x, y)

            r = random.randrange(0, 100)
            if r < tx_mutacao:
                if(tipo_mutacao == 1):
                    novo = mutar_v1(novo)
                else:
                    novo = mutar_v2(novo)

            p_nova.append(novo)

        max_fits.append(min(fit))
        med_fits.append(sum(fit) / len(fit))
        # Armazena o mais fit da população passada
        mais_fit = pop[argmin(fit)]

        # População atual recebe invidivuos da nova população
        pop = p_nova

        # Se há elitismo:
        if(elitismo == True):
            pop.append(mais_fit)

        # Calcula o fitness de todos os individuos da população e coloca em uma lista
        fit = list(map(lambda x: f(x, matriz_dist), pop))

        # Mais Fitness da nova população
        mais_fit = pop[argmin(fit)]

        # Se o mais fitness da nova população é melhor que o mais fitness da antiga população, então a melhor solução é o novo mais fitness
        if f(mais_fit, matriz_dist) < f(melhor_solucao, matriz_dist):
            melhor_solucao = mais_fit
            # Se houve melhora entao reseta o contador de geracoes
            geracao = 0

        else:
            # Se nao houve melhora no mais fit entao acrescenta 1 no contador de geracao
            geracao += 1

    a = f(melhor_solucao, matriz_dist)
    print("Melhor Solucao: ", melhor_solucao, "\n")
    print("Custo da melhor solucao: ", a, "\n")
    plt.figure()
    plt.plot(max_fits, label='Fitness minimo')
    plt.plot(med_fits, label='Fitness medio')
    plt.legend()
    plt.ylabel('Fitness')
    plt.xlabel('Geracoes')
    plt.show()
    return melhor_solucao
