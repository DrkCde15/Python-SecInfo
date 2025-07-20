from cryptography.fernet import Fernet
import os

# Função para descriptografar os arquivos
def dec_file(key, files):
    for file_path in files:
        with open(file_path, 'rb') as bin_file:
            content = bin_file.read()
        decrypted_content = Fernet(key).decrypt(content)
        with open(file_path, 'wb') as bin_file:
            bin_file.write(decrypted_content)

# Função para listar os arquivos no diretório
def list_files(base_dir):
    all_files = []
    for entry in os.listdir(base_dir):
        full_path = os.path.abspath(os.path.join(base_dir, entry))
        if os.path.isdir(full_path):
            all_files += list_files(full_path)
        elif os.path.isfile(full_path):
            all_files.append(full_path)
    return all_files

def main():
    # Solicitar ao usuário a chave de criptografia
    key_input = input("Digite a chave de descriptografia: ")

    try:
        # Converter a chave para o formato de bytes
        key = key_input.encode()  # Converte a chave digitada para bytes
        fernet = Fernet(key)  # Isso vai lançar um erro se a chave for inválida
        dir = 'C:'  # Defina o diretório onde os arquivos criptografados estão
        arqs = list_files(dir)

        # Descriptografar os arquivos
        dec_file(key, arqs)
        print("Arquivos descriptografados com sucesso.")

    except Exception as e:
        print(f"Ocorreu um erro ao tentar descriptografar: {e}")

if __name__ == "__main__":
    main()