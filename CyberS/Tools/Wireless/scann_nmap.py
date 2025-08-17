import nmap
import os
from datetime import datetime

def banner():
    print("="*60)
    print("                SCANNER NMAP EM PYTHON")
    print("="*60)

def menu():
    print("\nEscolha o tipo de scan:")
    print("[1] Scan Rápido")
    print("[2] Scan Agressivo (-A -T5)")
    print("[3] Scan Stealth (furtivo)")
    print("[0] Sair")
    return input("\nDigite a opção desejada: ").strip()

def scan_rapido(alvo):
    print(f"\n[+] Iniciando Scan Rápido em: {alvo}")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=alvo, ports='1-1024', arguments='-T5')
    resultado = exibir_resultados(scanner, alvo, "rapido")
    salvar_em_txt(alvo, "rapido", resultado)

def scan_agressivo(alvo):
    print(f"\n[+] Iniciando Scan Agressivo em: {alvo}")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=alvo, arguments='-A -T5')
    resultado = exibir_resultados(scanner, alvo, "agressivo")
    salvar_em_txt(alvo, "agressivo", resultado)

def scan_stealth(alvo):
    print(f"\n[+] Iniciando Scan Stealth (furtivo) em: {alvo}")
    scanner = nmap.PortScanner()
    argumentos_stealth = "-sS -T1 -Pn -n -f -D RND:5 --scan-delay 1s --max-rate 10"
    scanner.scan(hosts=alvo, ports='1-1024', arguments=argumentos_stealth)
    resultado = exibir_resultados(scanner, alvo, "stealth")
    salvar_em_txt(alvo, "stealth", resultado)

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

def salvar_em_txt(alvo, modo, resultado):
    data_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pasta = os.path.join("resultados", "scans")
    os.makedirs(pasta, exist_ok=True)

    nome_arquivo = f"{alvo.replace('.', '_')}_{modo}_{data_hora}.txt"
    caminho = os.path.join(pasta, nome_arquivo)

    with open(caminho, "w", encoding='utf-8') as f:
        f.write(f"Scan em: {alvo}\nModo: {modo}\nData: {data_hora}\n\n")
        f.write(resultado)

    print(f"\n[✔] Resultado salvo em: {caminho}")

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

        if opcao == '1':
            scan_rapido(alvo)
        elif opcao == '2':
            scan_agressivo(alvo)
        elif opcao == '3':
            scan_stealth(alvo)
        else:
            print("[-] Opção inválida.")

if __name__ == '__main__':
    main()
