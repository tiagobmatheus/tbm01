# Algoritmo Lote 01 - Exercício 16
# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes.
# Calcule o salário que serão as horas trabalhadas x o valor por hora.
# Calcule o salário líquido (= Salário Bruto – desconto).
# A cada dependente será acrescido R$ 100 no Salário Líquido.
# Exiba o salário a receber.

# Algoritmo Lote 01 - Exercício 16

# Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes.
# Calcule o salário que serão as horas trabalhadas x o valor por hora.
# Calcule o salário líquido (= Salário Bruto – desconto).
# A cada dependente será acrescido R$ 100 no Salário Líquido.
#Exiba o salário a receber.

#inicio.

horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
valor_hora =  float(input('Digite o valor por hora trabalhada: '))
desconto =  float(input('digite o percentual de desconto: '))
depentendes = int(input('Digite a quantidade de dependentes: '))

bruto = (horas_trabalhadas*valor_hora)
liquido = (bruto-(bruto*desconto/100))
acrescimo_dependente = (depentendes*100)
recebe=liquido+acrescimo_dependente

print('O Salário a receber é de:',recebe)

#fim.
