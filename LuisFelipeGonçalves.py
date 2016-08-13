#EXERCICIO I

a = int(input('A: '))
b = int(input('B: '))
print(a+b)

#EXERCICIO II

me = int(input('Metros: '))
print("Milimetros:",me*1000)

#EXERCICIO III

dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
sec = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos
print('Corresponde à %d segundos' %sec)

#EXERCICIO IV

salario = float(input('Salario atual: '))
porc_aumento = int(input('Porcentagem de aumento: '))
acre = (salario * porc_aumento) / 100
aumento = salario + acre
print('Novo salario: %.2f' %aumento)
print('Acrescimo salarial: %.2f' %acre)

#EXERCICIO V

mercadoria = float(input('Preço atual: '))
porc_desconto = int(input('Porcentagem de desconto: '))
decre = (mercadoria * porc_desconto) / 100
desconto = mercadoria - decre
print('Novo preço: %.2f' %desconto)
print('Desconto: %.2f' %decre)

#EXERCICIO VI

dist = float(input("Digite a distancia em Km: "))
velo = float(input("Digite a velocidade média: "))

tempo = dist / velo

print ('Tempo em horas %.1f' %tempo)

#EXERCICIO VII

c = input("Digite a temperatua em Celsius: ")
f = 9*c/5 + 32

print ('%d Fahrenheit' %f)

#EXERCICIO VIII

f = input("Digite a temperatua em Fahrenheit: ")
c = (f - 32) / 1.8

print ('%d graus Celsius' %c)

#EXERCICIO IX

kmp = int(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

print ('Valor do aluguel: R$ %.2f' %(kmp*0.15 + dias*60) )

#EXERCICIO X


qntCigarros = int(input("Qnts cigarros por dia: "))
anosFumando = int(input("Anos fumando: "))

totalCigarros = (anosFumando * 365)*qntCigarros
diasPerdidos = (totalCigarros * 10)/24

print ('Dias perdidos %d' %diasPerdidos )

#EXERCICIO XI

print(len(str(2**1000000)))
