import socket
import ipaddress

caminho = input("Digite o caminho do arquivo de endpoints: ")

def fuzz_endpoint(ip, port, endpoints):
    for endpoint in endpoints:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.settimeout(3)
                client.connect((ip, port))
                print(f"Testando endpoint: {endpoint}")
                client.sendall(endpoint.encode() + b'\n')  # + b'\n' se necessário
                response = client.recv(1024)
                print(f"Resposta de {endpoint}: {response.decode(errors='ignore')}\n")
        except Exception as e:
            print(f"Erro ao testar endpoint {endpoint}: {e}")

# Validação do IP
ip = input("Digite o IP do alvo: ")
try:
    ipaddress.ip_address(ip)
except ValueError:
    print("IP inválido.")
    exit()

# Validação da porta
try:
    port = int(input("Digite a porta do alvo: "))
    if not (0 < port < 65536):
        raise ValueError
except ValueError:
    print("Porta inválida.")
    exit()

# Leitura do arquivo
try:
    with open(caminho, "r") as f:
        endpoints = f.read().splitlines()
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
    exit()

if not endpoints:
    print("Lista de endpoints vazia.")
    exit()

fuzz_endpoint(ip, port, endpoints)