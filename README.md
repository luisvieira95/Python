# miscelaniadepython
#Exercícios de principiante na linguagem python

'''Calcula o salário do mes e descontos de impostos'''

ghora = float(input('Digite quanto voce ganha por hora: '))
thora = int(input('Digite as horas trabalhadas no mês: '))
salario_bruto = ghora * thora
ir = (salario_bruto * (11 / 100)) - salario_bruto
inss = (salario_bruto * (8 / 100)) - salario_bruto
sindicato = (salario_bruto * (5 / 100)) - salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato
impostos = (ir - inss - sindicato)

print("Você receberá R$%.2f" %salario_liquido)
print("Você paga um total de R$%.2f de impostos" %(impostos))
