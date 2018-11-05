#!/usr/bin/python
# coding: utf-8

import copy
from random import randint

def crossoverOrdenado(pai, mae):
    filho = copy.copy(pai)
    p = []
    s = []
    p_ord = []
    for x in range(0, randint(1, len(pai))):
        num_random = randint(0, len(pai)-1)
        if num_random not in p:
            p.append(num_random)
    p.sort()
    for x in p:
        s.append(pai[x])
    for x in mae:
        if x in s:
            p_ord.append(s.index(x))

    for i in range(len(s)):
        filho[p[i]] = s[p_ord[i]]

    return filho
