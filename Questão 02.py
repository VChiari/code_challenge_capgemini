#Débora se inscreveu em uma rede social para se manter em contato com seus amigos.
# A página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser forte.
# O site considera uma senha forte quando ela satisfaz os seguintes critérios:
#Possui no mínimo 6 caracteres.
#Contém no mínimo 1 digito.
#Contém no mínimo 1 letra em minúsculo.
#Contém no mínimo 1 letra em maiúsculo.
#Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+
#Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma senha forte.
# Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de caracteres que devem ser
# adicionados para uma string qualquer ser considerada segura

from time import sleep

print("Vamos validar sua senha?")
print("Uma senha válida precisa cumprir os seguintes requisítos : \n"
      "Possui no mínimo 6 caracteres \n"
      "Contém no mínimo 1 digito \n"
      "Contém no mínimo 1 letra em minúsculo \n"
      "Contém no mínimo 1 letra em maiúsculo \n"
      "Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+")

a, b, c, d = 0, 0, 0, 0
s = str(input('Digite sua senha: '))

print("Vamos validar sua senha, aguarde....")

sleep(2)

if (len(s) >= 6):
    for i in s:
        if (i.islower()):
            a+=1
        if (i.isupper()):
            b+=1
        if (i.isdigit()):
            c+=1
        if(i=='!'or i=='@' or i=='#' or i=='$' or i=='%' or i=="^" or i=='&' or i== '*' or i=='(' or i==')' or i=='-' or i=='+'):
            d+=1
print("="*30)
print("Relatório final:")
print("="*30)
if (a>=1 and b>=1 and c>=1 and d>=1 and a+c+b+d==len(s)):
    print("Senha válida")
else:
    print("Senha inválida")
    if a == 0:
        print("Sua senha não possui um caracter minúsculo")
    if b ==0:
        print("Sua senha não possui um caracter maiúsculo")
    if c == 0:
        print("Sua senha não possui um dígito")
    if d == 0:
        print("Sua senha não possui um caracter especial")