# TravellingSalesmanProblem :walking::thought_balloon:

## O Problema
O Problema do Caixeiro Viajante (TSP - Travelling Salesman Problem) é um dos problemas de otimização combinatória mais estudados e conhecidos. Ele é intrigante pois possui uma formulação simples e fácil de compreender, mas não existem algoritmos exatos eficientes que o resolvam. O problema de otimização é NP-difícil, enquanto o problema de decisão relacionado é NP-completo.

## Implementação
O seguinte trabalho faz parte de uma das atividades da disciplina de Inteligência Artificial (IA), tem como objetivo o estudo e implementação de um algoritmo genético. Durante a elaboração do trabalho foram elencados alguns requisitos mínimos que deverão ser cumpridos, sendo eles:

• Cross-over ordenado e alternativo

• 2 procedimentos de mutação

• Elitismo e não-elitismo

• Função fitness própria

• Critério de estagnação para parada

A linguagem de programação escolhida para implementação foi o Python por motivos de afinidade e nível de complexidade. O trabalho está organizado basicamente em duas pastas, a pasta raiz contém toda a implementação do algoritmo, dentro desta há também uma pasta chamada Testes, nela se encontra alguns conjuntos de entradas possível para executar o algoritmo.

O conjunto de testes foi retirado da TSPLIB que é uma grande coleção de vários conjuntos de dados usados para avaliar algoritmos que visam resolver o TSP. O link para esta coleção é:  https://typo.iwr.uni-heidelberg.de/groups/comopt/groups/comopt/software/TSPLIB95/tsp/

### Execução
A execução deste trabalho pode ser realizada primeiramente com o clone deste repositório para seu computador. Depois disto é necessário verificar algumas dependências que são elas:

#### Python 
Verifique se em sua máquina existe o programa Python na versão 3.7.1 ou superior, certifique também se as variáveis de ambiente para o tal estão devidamente configuradas e aptas a execução pela linha de comando.
É possível encontrar documentação e o download do Python 3.7.1 no seguinte link: (https://www.python.org/)

#### Bibliotecas
Algumas bibliotecas de terceiros devem ser instaladas para a execução plena do trabalho, segue abaixo os comandos para instalação de cada uma.
> Numpy 
```sh
$ pip install -U numpy
```
> Pandas
```sh
$ pip install -U pandas
```
> matplotlib.pyplot
```sh
$ pip install -U matplotlib
```

#### Run
Assim que todo o ambiente estiver preparado podemos executar o trabalho e realizar alguns testes, abaixo segue um exemplo de como deve ser feita a execução e os devidos parâmetros.
```sh
$ python main.py ./Testes/u1432.tsp
```



