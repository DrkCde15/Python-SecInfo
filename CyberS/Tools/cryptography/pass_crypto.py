import random #biblioteca para gerar uma chave aleatória 
import string #biblioteca para trabalhar com strings

# Definindo o conjunto de caracteres possíveis
chars = " " + string.punctuation + string.digits + string.ascii_letters #servem para criptografar e descriptografar
chars = list(chars) #transformando em uma lista

# Gerando uma chave aleatória
key = chars.copy()
random.shuffle(key)

# Função para criptografar
def encrypt(plain_text):
    cipher_text = ""
    for letter in plain_text:
        index = chars.index(letter)
        cipher_text += key[index]
    return cipher_text

# Função para descriptografar
def decrypt(cipher_text):
    plain_text = ""
    for letter in cipher_text:
        index = key.index(letter)
        plain_text += chars[index]
    return plain_text

# Menu de opções
while True:
    print("\nEscolha uma opção:")
    print("1. Criptografar uma mensagem")
    print("2. Descriptografar uma mensagem")
    print("3. Sair")
    
    choice = input("Digite o número da opção: ")

    if choice == "1":
        plain_text = input("Digite a mensagem para criptografar: ")
        cipher_text = encrypt(plain_text)
        print(f"Mensagem original: {plain_text}")
        print(f"Mensagem criptografada: {cipher_text}")
    
    elif choice == "2":
        cipher_text = input("Digite a mensagem para descriptografar: ")
        plain_text = decrypt(cipher_text)
        print(f"Mensagem criptografada: {cipher_text}")
        print(f"Mensagem original: {plain_text}")
    
    elif choice == "3":
        print("Saindo, obrigado por usar o programa...")
        break
    
    else:
        print("Opção inválida, tente novamente.")