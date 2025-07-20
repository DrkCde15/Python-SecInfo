import getpass
import os

arquivo = 'usuarios.txt'

def salvar_usuario(usuario, senha):
    with open(arquivo, 'a') as f:
        f.write(f'{usuario}:{senha}\n')

def carregar_usuarios():
    if not os.path.exists(arquivo):
        return {}
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    usuarios = {}
    for linha in linhas:
        if ':' in linha:
            u, s = linha.strip().split(':', 1)
            usuarios[u] = s
    return usuarios

def cadastrar_usuario():
    banco = carregar_usuarios()
    while True:
        usuario = input("Crie um novo usuário: ")
        if usuario in banco:
            print("Usuário já existe. Tente outro nome.")
            continue

        senha = getpass.getpass("Crie uma senha: ")
        if senha in banco.values():
            print("Esta senha já está em uso. Tente outra senha.")
            continue

        senha2 = getpass.getpass("Confirme sua senha: ")
        if senha == senha2:
            salvar_usuario(usuario, senha)
            print("suário cadastrado com sucesso!")
            break
        else:
            print("As senhas não coincidem. Tente novamente.")

def consultar_usuario():
    banco = carregar_usuarios()
    usuario = input("Digite o nome de usuário: ")

    if usuario not in banco:
        print("Usuário não encontrado.")
        return

    senha = getpass.getpass("Digite a senha: ")

    if senha == banco[usuario]:
        print("Login bem-sucedido!")
    else:
        print("Senha incorreta.")

# Menu principal
while True:
    print("\n--- MENU ---")
    print("1 - Criar nova conta")
    print("2 - Consultar (Login)")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_usuario()
    elif opcao == '2':
        consultar_usuario()
    elif opcao == '3':
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
