import sqlite3
import hashlib
import os

DB_PATH = './table/users.db'

def carregar_usuarios():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT email, password FROM users")
    usuarios = cur.fetchall()
    con.close()
    return usuarios

def quebrar_hash_por_wordlist(hash_alvo, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as arquivo:
            for linha in arquivo:
                senha = linha.strip()
                hash_tentativa = hashlib.sha256(senha.encode('utf-8')).hexdigest()
                if hash_tentativa == hash_alvo:
                    return senha
    except FileNotFoundError:
        print(f"Arquivo '{wordlist_path}' não encontrado.")
    return None

def main():
    print("=== BREAK HASHES ===")
    wordlist_path = input("Digite o caminho da wordlist: ").strip()

    if not os.path.exists(wordlist_path):
        print("Wordlist não encontrada.")
        return

    usuarios = carregar_usuarios()
    print(f"\nVerificando {len(usuarios)} usuários...\n")

    for email, senha_hash in usuarios:
        senha_quebrada = quebrar_hash_por_wordlist(senha_hash, wordlist_path)
        if senha_quebrada:
            print(f"{email} → {senha_quebrada}")
        else:
            print(f"{email} → Não encontrada na wordlist.")

if __name__ == "__main__":
    main()
