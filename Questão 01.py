#Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere * e espaços.
# A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter nenhum espaço.
from time import sleep
print("="*50)
tamanho = int(input(('Digite um valor para o tamanho de sua escada: ')))

caracter = str(input("Digite UM caracter que você gostaria de usar para construir sua escada, por exemplo [*]: "))
print("="*50)

for i in range(1, tamanho+1):
    print(' ' * (tamanho - i)  + f'{caracter}' * i)