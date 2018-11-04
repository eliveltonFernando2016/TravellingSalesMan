#!/usr/bin/python
# coding: utf-8

from readCsv import parser
from sys import argv
from algoritmoGenetico import algoritmo_genetico
from algoritmoGenetico import cria_matriz_de_distancia
from algoritmoGenetico import gen_pop
from algoritmoGenetico import fitness

if __name__ == '__main__':
    noDimensao = parser(argv[1])

    matriz = cria_matriz_de_distancia(noDimensao[0], noDimensao[1])
    pop = gen_pop(noDimensao[0], noDimensao[1])

    # Definição dos parametros na definicao da funçao
    best = algoritmo_genetico(pop_inicial = pop, f = fitness, matriz_dist = matriz, k = 100, tx_mutacao = 10, elitismo = int(argv[4]), reproducao = str(argv[2]), tipo_mutacao = str(argv[3]))
    
    # argv[2] = reproducao (ordenado/alternado)
    # argv[3] = mutacao (1/2)
    # argv[4] = elitismo (1/0)
    # Definição dos parametros na definicao da funçao
    #best = algoritmo_genetico(pop_inicial = pop, f = fitness, matriz_dist = matriz, k = 100, tx_mutacao = 10, elitismo = argv[4], reproducao = argv[2], tipo_mutacao = argv[3])
