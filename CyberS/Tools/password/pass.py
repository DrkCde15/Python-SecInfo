import random #biblioteca para gerar numeros aleatorios

print('Bem-vindo ao gerador de senha!') # gerador de senhas
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}|:<>?' #caracteres disponíveis
n = int(input('Quantidade de caracteres: ')) #tamanho da senha
amount = int(input('Quantidade de senhas: ')) #quantidade de senhas

size = len(chars) #tamanho dos caracteres
for i in range(amount): #quantidade de senhas geradas
    password = '' #string vazia para armazenar a senha
    for j in range(n): #tamanho da senha gerada 
        password += random.choice(chars) #escolhe um caracter aleatorio
    print(password) #imprime a senha