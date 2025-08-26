# Wireless Toolkit

Este repositório contém uma coleção de scripts em **Python** voltados para testes de segurança, automação de reconhecimento e exploração em Redes/Dominios.  
⚠️ **Atenção:** Todo o conteúdo é para **uso educacional e em ambientes autorizados**. O uso indevido pode ser considerado crime digital.

---

## 📂 Estrutura do Projeto

- **brute_force.py**  
  Script para ataques de força bruta em serviços autenticáveis.  
  Permite testar senhas a partir de uma wordlist.

- **fuzz.py**  
  Fuzzer simples para descobrir diretórios e arquivos escondidos em aplicações web.  
  Ideal para **teste de enumeração**.

- **port_scan.py**  
  Scanner de portas básico implementado em Python.  
  Verifica quais portas estão abertas em um host alvo.

- **scann_nmap.py**  
  Wrapper para o **Nmap** via Python.  
  Executa varreduras avançadas aproveitando as funcionalidades da ferramenta nmap(com scanns stealth, agressivo e rápido).

- **wifi_pass.py**  
  Script para listar e recuperar senhas de redes Wi-Fi salvas no sistema.  
  Útil em auditorias de redes sem fio.

---

## 🚀 Como Usar

1. Clone o repositório:
```bash
git clone https://github.com/DrkCde15/SecInfo/Cyber/Tools.git
cd SecInfo/Cyber/Tools/Wireless
