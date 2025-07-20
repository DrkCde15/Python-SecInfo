import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from geopy.geocoders import Nominatim
from datetime import datetime

def analisar_numero(numero_str):
    try:
        numero = phonenumbers.parse(numero_str)
        if phonenumbers.is_valid_number(numero):
            localizacao = geocoder.description_for_number(numero, "en")
            operadora = carrier.name_for_number(numero, "en")
            fuso_horario = timezone.time_zones_for_number(numero)
            horario = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Usando geopy para pegar latitude e longitude
            geolocator = Nominatim(user_agent="numero-localizador")
            coordenadas = geolocator.geocode(localizacao)

            latitude = coordenadas.latitude if coordenadas else "Não encontrado"
            longitude = coordenadas.longitude if coordenadas else "Não encontrado"

            resultado = (
                f"[{horario}]\n"
                f"Número: {numero_str}\n"
                f"País / Região: {localizacao}\n"
                f"Operadora: {operadora if operadora else 'Desconhecida'}\n"
                f"Fuso Horário: {', '.join(fuso_horario)}\n"
                f"Latitude: {latitude}\n"
                f"Longitude: {longitude}\n"
                f"Válido: Sim\n"
                "-----------------------------\n"
            )

            print("\n=== Resultado da Análise ===")
            print(resultado)

            # Salvar no arquivo
            with open("relatorio_numeros.txt", "a", encoding="utf-8") as f:
                f.write(resultado)

        else:
            print(f"\nNúmero inválido: {numero_str}\n")

    except phonenumbers.NumberParseException as e:
        print(f"\nErro ao analisar o número: {e}\n")

    except Exception as e:
        print(f"\nErro ao obter coordenadas: {e}\n")


print("=== LOCALIZADOR DE NÚMEROS ===")
print("Digite 'sair' para encerrar.\n")

while True:
    entrada = input("Digite o número com DDI (ex: +5511987654321): ")
    if entrada.strip().lower() == "sair":
        print("\nEncerrado. Resultados salvos em 'relatorio_numeros.txt'")
        break
    analisar_numero(entrada)