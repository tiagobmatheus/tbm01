# Algoritmo Lote 01 - Exercício 12
# Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.

# inicio.

nascimento = int(input('Digite o ano de nascimento '))
atual = int(input('Digite o ano atual '))
idade = atual - nascimento
idade_17 = idade + 17

print('A idade atual é',idade,'e a idade em 17 anos será de',idade_17)

#fim.