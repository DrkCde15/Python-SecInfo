import nmap
import os
import json
import socket
from datetime import datetime

def banner():
    print("="*60)
    print("                SCANNER NMAP EM PYTHON")
    print("="*60)

def menu():
    print("\nEscolha o tipo de scan:")
    print("[1] Scan Rápido")
    print("[2] Scan Agressivo")
    print("[3] Scan Stealth (furtivo)")
    print("[0] Sair")
    return input("\nDigite a opção desejada: ").strip()

# Resolver DNS e listar IPs
def resolver_ips(alvo):
    try:
        print(f"\n[*] Resolvendo {alvo}...")
        infos = socket.getaddrinfo(alvo, None)
        ips = list({info[4][0] for info in infos})  # elimina duplicados
        print("[+] IPs encontrados:")
        for i, ip in enumerate(ips, 1):
            print(f"   [{i}] {ip}")
        escolha = input("\nDigite o número do IP que deseja escanear (ou ENTER para o primeiro): ").strip()
        if escolha.isdigit() and 1 <= int(escolha) <= len(ips):
            return ips[int(escolha) - 1]
        return ips[0]  # padrão: primeiro IP
    except Exception as e:
        print(f"[!] Falha ao resolver domínio: {e}")
        return alvo  # tenta escanear o alvo original mesmo assim

def scan_rapido(alvo):
    print(f"\n[+] Iniciando Scan Rápido em: {alvo}")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=alvo, ports='1-1024', arguments='-T5')
    resultado = exibir_resultados(scanner, alvo, "rapido")
    salvar_resultados(alvo, "rapido", resultado, scanner)

def scan_agressivo(alvo):
    print(f"\n[+] Iniciando Scan Agressivo em: {alvo}")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=alvo, arguments='-A -T5')
    resultado = exibir_resultados(scanner, alvo, "agressivo")
    salvar_resultados(alvo, "agressivo", resultado, scanner)

def scan_stealth(alvo):
    print(f"\n[+] Iniciando Scan Stealth (furtivo) em: {alvo}")
    scanner = nmap.PortScanner()
    argumentos_stealth = "-sS -T1 -Pn -n -f -D RND:5 --scan-delay 1s --max-rate 10"
    scanner.scan(hosts=alvo, ports='1-1024', arguments=argumentos_stealth)
    resultado = exibir_resultados(scanner, alvo, "stealth")
    salvar_resultados(alvo, "stealth", resultado, scanner)

def exibir_resultados(scanner, alvo, modo):
    saida = []
    if alvo not in scanner.all_hosts():
        msg = "[!] Alvo não respondeu ou está offline."
        print(msg)
        return msg

    saida.append(f"[+] Host: {alvo}")
    saida.append(f"    Estado: {scanner[alvo].state()}")

    if 'osmatch' in scanner[alvo] and scanner[alvo]['osmatch']:
        saida.append("\n[+] Sistema Operacional (se detectado):")
        for os in scanner[alvo]['osmatch']:
            saida.append(f"  -> {os['name']} (confiança: {os['accuracy']}%)")
            break

    saida.append("\n[+] Portas abertas:")
    for proto in scanner[alvo].all_protocols():
        ports = scanner[alvo][proto].keys()
        for port in sorted(ports):
            estado = scanner[alvo][proto][port]['state']
            servico = scanner[alvo][proto][port].get('name', 'desconhecido')
            saida.append(f"  -> Porta {port}/{proto} | {estado} | Serviço: {servico}")

    if 'hostscript' in scanner[alvo]:
        saida.append("\n[+] Scripts NSE:")
        for script in scanner[alvo]['hostscript']:
            saida.append(f"  -> {script['id']}:\n{script['output']}\n")

    print("\n".join(saida))
    return "\n".join(saida)

def salvar_resultados(alvo, modo, resultado, scanner):
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pasta = os.path.join("resultados", "scans")
    os.makedirs(pasta, exist_ok=True)

    # Arquivo TXT
    nome_arquivo_txt = f"{alvo.replace('.', '_')}_{modo}_{data_hora}.txt"
    caminho_txt = os.path.join(pasta, nome_arquivo_txt)

    with open(caminho_txt, "w", encoding='utf-8') as f:
        f.write(f"Scan em: {alvo}\nModo: {modo}\nData: {data_hora}\n\n")
        f.write(resultado)

    print(f"\n[✔] Resultado TXT salvo em: {caminho_txt}")

    # Arquivo JSON só se houver resultados
    if alvo in scanner.all_hosts():
        nome_arquivo_json = f"{alvo.replace('.', '_')}_{modo}_{data_hora}.json"
        caminho_json = os.path.join(pasta, nome_arquivo_json)

        with open(caminho_json, "w", encoding='utf-8') as f:
            json.dump(scanner[alvo], f, indent=4, ensure_ascii=False)

        print(f"[✔] Resultado JSON salvo em: {caminho_json}")
    else:
        print("[!] Nenhum dado para salvar em JSON (host não respondeu).")

def main():
    banner()
    while True:
        opcao = menu()
        if opcao == '0':
            print("Encerrando scanner. Até mais!")
            break

        alvo = input("\nDigite o IP ou domínio do alvo: ").strip()
        if not alvo:
            print("[-] Alvo inválido.")
            continue

        # resolve domínio -> retorna IP válido
        alvo_resolvido = resolver_ips(alvo)

        if opcao == '1':
            scan_rapido(alvo_resolvido)
        elif opcao == '2':
            scan_agressivo(alvo_resolvido)
        elif opcao == '3':
            scan_stealth(alvo_resolvido)
        else:
            print("[-] Opção inválida.")

if __name__ == '__main__':
    main()