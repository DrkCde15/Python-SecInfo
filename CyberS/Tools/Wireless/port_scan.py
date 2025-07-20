import socket #biblioteca de rede eletrônica para comunicação com o computador

hostname = input("Alvo: ") #nome do alvo
porta = range(0, 1000) #portas abertas no alvo a serem pesquisadas
file = open("Scanned.txt",'+w') #cria o arquivo de saida
print("Arquivo Salvo em ==>> Scanned.txt") #mensagem de saida
file.write(f"Alvo: {hostname}\n\n") #escreve o nome do alvo

try: #verifica se o alvo existe na rede
    for p in porta: #percorre as portas abertas
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket de comunicação com o alvo e define o tipo de comunicação
        client.settimeout(0.05) #configura o timeout de comunicação para 0.01 segundos
        scan = client.connect_ex((hostname, p)) #verifica se a porta está aberta no alvo
        if scan == 0: #se a porta estiver aberta
            file.write(f"Porta aberta: {p} {socket.getservbyport(p)}\n") #escreve a porta aberta e o serviço associado a ela
            
except: #se o alvo não existir
    print("Alvo não encontrado!") #mensagem de erro