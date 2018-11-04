# !/bin/bash
# argv[1] = nome do problema
# argv[2] = reproducao (ordenado/alternado)
# argv[3] = mutacao (1/2)
# argv[4] = elitismo (1/0)
echo "Script de Execução"


#Cross-over ordenado, mutação 1, elitismo, estagnação
echo "--------LOTE 1----------"
echo "Cross-over ordenado, mutação 1, elitismo, estagnação"
python main.py berlin52.tsp ordenado 1 1