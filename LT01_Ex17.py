# Algoritmo Lote 01 - Exercício 17

# Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l
# Receber o tempo de percurso e a velocidade média.

#inicio.

tempo = float(input('digite o tempo de percurso: '))
velocidade = float(input('digite a velocidade média: '))
distancia = float(velocidade*tempo)
consumo = 12
litros = distancia/consumo

print('A quantidade de litros gastos na viagem é de :',litros)

#fim.