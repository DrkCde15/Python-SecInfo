# ps_bkdr – Servidor de Backdoor em PowerShell e Python

Este repositório contém um servidor didático de **payloads** para execução remota via PowerShell, utilizando **Python e HTTP**.
O objetivo é educacional, permitindo estudar payloads, comunicação remota e manipulação de comandos de forma controlada em laboratórios de segurança.
⚠️ **Atenção:** Todo o conteúdo é para **uso educacional e em ambientes autorizados**. O uso indevido pode ser considerado crime digital.

📂 Estrutura

``ps_bkdr.py → Script principal que inicia o servidor HTTP para receber e enviar payloads.``

``payload/basic_shell.py → Stage básico de execução remota via PowerShell.``

``stagers/basic.ps1 → Comandos PowerShell.``

# ⚙️ Requisitos

-> Python 3.10

-> Bibliotecas padrão do Python: http.server, argparse, base64, logging

# Clone o repositório:
```bash
git clone https://github.com/DrkCde15/SecInfo/.git
cd SecInfo/Cyber/Tools/Backdoor

▶️ Como usar

python ps_bkdr.py -i 0.0.0.0 -p 8000 -s basic