# Algoritmo - Lote 01 - Exercício 05
# Receba os coeficientes A, B e C de uma equação do 2º grau (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possue 2 raízes).

#inicio.

a = float(input('Digite o coeficiente A: '))
b = float(input('Digite o coeficiente B: '))
c = float(input('Digite o coeficiente C: '))

x1 = (-b+((b*b-4*a*c)*(1/2)))/(2*a)
x2 = (-b-((b*b-4*a*c)*(1/2)))/(2*a)

print('As raízes dessa equação são :', x1,x2)

#fim.