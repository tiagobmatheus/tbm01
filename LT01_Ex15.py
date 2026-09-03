# Algoritmo Lote 01 - Exercício 15
# Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.

#inicio

cat1 = float(input('Digite um dos catetos: '))
cat2 = float(input('Digite o outro cateto: '))
hip = ((cat1*cat1 + cat2*cat2)**(1/2))

print('A medida da hipotenusa é:',hip)

#fim