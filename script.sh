# !/bin/bash
# argv[1] = nome do problema
# argv[2] = reproducao (ordenado/alternado)
# argv[3] = mutacao (1/2)
# argv[4] = elitismo (1/0)
echo "Script de Execução"


#Cross-over ordenado, mutação 1, elitismo, estagnação
echo "--------LOTE 1----------"
echo "Cross-over ordenado, mutação 1, elitismo, estagnação"
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1
python main.py kroD100.tsp ordenado 1 1


#Cross-over ordenado, mutação 2, elitismo, estagnação
echo "--------LOTE 2----------"
echo "Cross-over ordenado, mutação 2, elitismo, estagnação"
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1
python main.py kroD100.tsp ordenado 2 1

#Cross-over alternativo, mutação 1, elitistmo, estagnação
echo "--------LOTE 3----------"
echo "Cross-over alternativo, mutação 1, elitistmo, estagnação"
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1
python main.py kroD100.tsp alternativo 1 1


#Cross-over alternativo, mutação 2, elitismo, estagnação
echo "--------LOTE 4----------"
echo "Cross-over alternativo, mutação 2, elitismo, estagnação"
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1
python main.py kroD100.tsp alternativo 2 1