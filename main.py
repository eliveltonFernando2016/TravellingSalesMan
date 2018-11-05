#!/usr/bin/python
# coding: utf-8

from readCsv import parser
from sys import argv
from algoritmoGenetico import algoritmoGenetico
from algoritmoGenetico import matrizDistancia
from algoritmoGenetico import gen_pop
from algoritmoGenetico import fitness

if __name__ == '__main__':
    if len(argv) != 2:
        print("Argumentos inválidos!")

    noDimensao = parser(argv[1])

    matriz = matrizDistancia(noDimensao[0], noDimensao[1])
    pop = gen_pop(noDimensao[0], noDimensao[1])

    # Definição dos parametros na definicao da funçao
    best = algoritmoGenetico(pop_inicial = pop, f = fitness, matriz_dist = matriz, k = 100, tx_mutacao = 10, elitismo = 1, reproducao = "ordenado", tipo_mutacao = 1)
