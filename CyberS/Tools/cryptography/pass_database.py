import sqlite3
import os
from cryptography.fernet import Fernet

# --- CONFIGURAÇÃO DE CHAVE AUTOMÁTICA ---
def carregar_ou_gerar_chave():
    # Se a chave não existir, ele cria uma nova
    if not os.path.exists("chave.key"):
        chave = Fernet.generate_key()
        with open("chave.key", "wb") as key_file:
            key_file.write(chave)
    
    # Lê a chave do arquivo
    return open("chave.key", "rb").read()

# Inicializa o objeto de criptografia globalmente
CHAVE = carregar_ou_gerar_chave()
fernet = Fernet(CHAVE)

# --- INICIALIZAÇÃO DO AMBIENTE ---
def preparar_ambiente():
    # Garante que a pasta data exista para não dar erro no SQLite
    if not os.path.exists("data"):
        os.makedirs("data")

def iniciar_db():
    conn = sqlite3.connect("./data/cofre.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS senhas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            servico TEXT NOT NULL,
            usuario TEXT NOT NULL,
            senha_cripto BLOB NOT NULL
        )
    ''')
    conn.commit()
    return conn

# --- FUNÇÕES PRINCIPAIS ---
def salvar_senha(servico, usuario, senha_pura):
    conn = iniciar_db()
    cursor = conn.cursor()
    
    # Criptografa a senha usando a chave automática
    senha_cripto = fernet.encrypt(senha_pura.encode())
    
    cursor.execute("INSERT INTO senhas (servico, usuario, senha_cripto) VALUES (?, ?, ?)", 
                   (servico, usuario, senha_cripto))
    conn.commit()
    conn.close()
    print(f"\n✅ Senha para {servico} salva com sucesso!")

def listar_senhas():
    conn = iniciar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT servico, usuario, senha_cripto FROM senhas")
    
    print("\n--- SUAS SENHAS SALVAS ---")
    rows = cursor.fetchall()
    
    if not rows:
        print("Nenhuma senha encontrada.")
    else:
        for servico, usuario, senha_cripto in rows:
            # Descriptografa automaticamente
            senha_decripto = fernet.decrypt(senha_cripto).decode()
            print(f"Serviço: {servico.ljust(15)} | Usuário: {usuario.ljust(15)} | Senha: {senha_decripto}")
    
    conn.close()

# --- MENU ---
def menu():
    preparar_ambiente()
    iniciar_db()
    
    while True:
        print("\n=== GERENCIADOR DE SENHAS ===")
        print("[1] Salvar Nova Senha")
        print("[2] Ver Senhas Salvas")
        print("[3] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            serv = input("Serviço: ")
            user = input("Usuário: ")
            pw = input("Senha: ")
            salvar_senha(serv, user, pw)
        elif opcao == "2":
            listar_senhas()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()