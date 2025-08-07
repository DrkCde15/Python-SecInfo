import sqlite3
import os
import hashlib

DB_PATH = './table/users.db'
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Criação da tabela
con = sqlite3.connect(DB_PATH)
cur = con.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
""")
con.commit()
con.close()

# Função para hashear senha com SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Inserção de usuário
con = sqlite3.connect(DB_PATH)
cur = con.cursor()

email = input("Digite o email: ")
passwd = input("Digite sua senha: ")
passwd_hash = hash_password(passwd)

cur.execute("SELECT * FROM users WHERE email = ?", (email,))
if cur.fetchone():
    print("Já existe um usuário com esse email.")
else:
    try:
        cur.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, passwd_hash))
        con.commit()
        print("Usuário inserido com sucesso!")
    except sqlite3.IntegrityError:
        print("Falha ao inserir. Email já existente.")

con.close()