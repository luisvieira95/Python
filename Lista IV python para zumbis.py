import random
from random import randint

#EXERCICIO I

lista = []
for k in range(10):
    lista.append(random.randint(1, 100))
    lista.sort()
print("Maior", lista[-1])
print("Menor", lista[0])
print("Lista completa", lista)

#EXERCICIO II

listaPar = []
listaImpar = []
lista = [] 

for k in range(20):
    lista.append(random.randint(1, 100))
    if lista[k] % 2 == 0:
        listaPar.append(lista[k])
    else:
        listaImpar.append(lista[k])
    
print("Lista completa", lista)
print("Par", listaPar)
print("Impar", listaImpar)

#EXERCICIO III

listaUm = []
listaDois = []

for k in range(10):
    listaUm.append(random.randint(1, 100))
for y in range(10):
    listaDois.append(random.randint(1, 100))
listaTres = listaUm + listaDois
print('Lista um: ' , listaUm)
print('Lista dois: ', listaDois)
print('Lista um e dois: ' ,listaTres)

#EXERCICIO IV

texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'''.upper()

T = texto.split()
palavra = []
c = len(T)
k = 0
while k < len(T):
    if T[k].endswith("."):
        T[k] = T[k].replace(".","")
    k += 1
for x in range(c) :
    if T[x].startswith("P") or T[x].startswith("Y") or T[x].startswith("T") or T[x].startswith("H") or T[x].startswith("O") or T[x].startswith("N") :
       palavra.append(T[x])
       
print(palavra)


#EXERCICIO V

texto = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone.
Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles.
We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'''.upper()

T = texto.split()
palavra = []
c = len(T)
k = 0
while k < len(T):
    if T[k].endswith("."):
        T[k] = T[k].replace(".","")
    k += 1
for x in range(c) :
    if T[x].startswith("P") or T[x].startswith("Y") or T[x].startswith("T") or T[x].startswith("H") or T[x].startswith("O") or T[x].startswith("N"):
        if len(T[x]) > 4:
           palavra.append(T[x])
print(palavra)
