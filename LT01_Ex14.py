# Algoritmo Lote 01 - Exercício 14
# Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.

#inicio.

Angulo1 = float(input('Digite um dos ângulos do triângulo: '))
Angulo2 = float(input('Digite outro ângulo: '))
Angulo3 = (180 - (Angulo1 + Angulo2))

print('A medida do 3° ângulo é de:',Angulo3)

#fim
