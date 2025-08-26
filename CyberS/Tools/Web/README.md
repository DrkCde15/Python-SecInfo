# Web Attacks Toolkit

Este repositório contém uma coleção de scripts em **Python** voltados para testes de segurança, automação de reconhecimento e exploração em ambientes controlados.  

⚠️ **Atenção:** Todo o conteúdo é apenas para **uso educacional em laboratórios de teste autorizados**.

---

## 📂 Estrutura

- **table/**  
  - `bd.py` → Script relacionado a banco de dados (ex: testes de autenticação ou força bruta em credenciais de DB).  
  - `bf.py` → Script de **brute force genérico**, utilizando wordlists.  

- **wordlist.txt**  
  Wordlist de exemplo para testes de força bruta (senhas comuns).

- **ddos.py**  
  Script simples para simulação de ataque **DDoS** (negação de serviço).  
  Usado apenas para estudo de impacto em ambientes controlados.

- **proxies.txt**  
  Lista de proxies que pode ser usada nos ataques de ddos para evitar bloqueios.

---

## 🚀 Como Usar

1. Clone este repositório:
```bash
git clone https://github.com/DrkCde15/SecInfo/.git
cd SecInfo/Cyber/Tools/Web
