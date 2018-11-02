#!/usr/bin/python
# coding: utf-8

def parser(arq):
    infile = open(arq, 'r')

    # Leitura do cabecalho
    Name           = infile.readline().strip().split()[1]
    FileType       = infile.readline().strip().split()[1]
    Comment        = infile.readline().strip().split()[1]
    Dimension      = infile.readline().strip().split()[1] 
    EdgeWeightType = infile.readline().strip().split()[1]
    infile.readline()

    # Leitura dos nós
    node_list = []
    N = int(Dimension)
    for i in range(0, int(Dimension)):
        xy = infile.readline().strip().split()[1:]
        node_list.append([int(float(xy[0])), int(float(xy[1]))])

    return node_list, N