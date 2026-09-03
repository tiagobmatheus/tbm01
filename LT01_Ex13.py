# Algoritmo Lote 01 - Exercício 13
# Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.

# inicio.

Quantidade = float(input('Digite a Quantidade de alimento em Kg '))
Consumo = float(50)
Duracao = Quantidade * 1000 / 50

print('A duração desse alimento em dias é de', Duracao)

#fim.