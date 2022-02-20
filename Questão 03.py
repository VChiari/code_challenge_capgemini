#Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra podem ser
# realocadas para formar a outra palavra. Dada uma string qualquer,
# desenvolva um algoritmo que encontre o número de pares de substrings que são anagramas.


import itertools
from time import sleep

print("="*50)
print("Vamos verificar a quantidade pares de anagramas em uma palavra!!")
palavra = str(input("Informe a palavra: "))
print("="*50)
print("Verificando quantidade de anagramas....")
sleep(2)

qtyAnagrama = 0
for g in range(1, len(palavra)):
    for i in range(0, len(palavra) - 1):
        pf = set()
        pf.update("".join(f) for f in itertools.permutations(palavra[i:i + g], g))
        for x in pf:
            if palavra[i + 1:len(palavra)].count(x):
                qtyAnagrama += 1
print(f"A quantidade de anagramas pares contidos na palavra '{palavra}' é de {qtyAnagrama}")