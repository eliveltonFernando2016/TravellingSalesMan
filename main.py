#!/usr/bin/python
# coding: utf-8

from readCsv import parser
from sys import argv
from algoritmoGenetico import algoritmo_genetico
from algoritmoGenetico import cria_matriz_de_distancia
from algoritmoGenetico import gen_pop
from algoritmoGenetico import fitness

if __name__ == '__main__':
    if len(argv) != 2:
        print("Argumentos inválidos!")

    noDimensao = parser(argv[1])

    matriz = cria_matriz_de_distancia(noDimensao[0], noDimensao[1])
    pop = gen_pop(noDimensao[0], 100)

    # Definição dos parametros na definicao da funçao
    best = algoritmo_genetico(pop_inicial = pop, f = fitness, matriz_dist = matriz, k = 50, tx_mutacao = 10, elitismo = 1, reproducao = "ordenado", tipo_mutacao = 1)
