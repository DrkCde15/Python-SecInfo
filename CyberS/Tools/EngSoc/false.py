import random
from datetime import datetime, timedelta

def luhn(digits):
    """Calcula o dígito verificador pelo algoritmo de Luhn"""
    sum_ = 0
    reverse_digits = digits[::-1]
    for i, d in enumerate(reverse_digits):
        n = int(d)
        if i % 2 == 0:
            n *= 2
            if n > 9:
                n -= 9
        sum_ += n
    return (10 - (sum_ % 10)) % 10

def gerar_numero_cartao():
    # Gerar os primeiros 15 dígitos do cartão de crédito aleatoriamente
    prefixo_cartao = [str(random.randint(0, 9)) for _ in range(15)]
    # Calcular o dígito verificador com base nos 15 dígitos gerados
    digito_verificador = luhn(prefixo_cartao)
    # Adicionar o dígito verificador ao número do cartão
    prefixo_cartao.append(str(digito_verificador))
    # Retornar o cartão no formato correto
    return ''.join(prefixo_cartao)

def formata_cartao(cartao):
    # Formatando o número do cartão no formato XXXX XXXX XXXX XXXX
    return f"{cartao[:4]} {cartao[4:8]} {cartao[8:12]} {cartao[12:16]}"

def gera_cartoes_em_lote(quantidade):
    cartoes = []
    for _ in range(quantidade):
        cartao = gerar_numero_cartao()
        cartoes.append(formata_cartao(cartao))
    return cartoes

def gerar_cpf():
    cpf = [random.randint(0, 9) for _ in range(9)]
    for _ in range(2):
        val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - val if val > 1 else 0)
    return ''.join(map(str, cpf[:3])) + '.' + ''.join(map(str, cpf[3:6])) + '.' + ''.join(map(str, cpf[6:9])) + '-' + ''.join(map(str, cpf[9:]))

def gerar_rg():
    rg = [random.randint(0, 9) for _ in range(8)]
    return ''.join(map(str, rg[:2])) + '.' + ''.join(map(str, rg[2:5])) + '.' + ''.join(map(str, rg[5:8])) + '-' + str(random.randint(0, 9))

def gerar_data_nascimento():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2005, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%d/%m/%Y')

def gerar_telefone(estado):
    ddd = {
        'AC': ['68'], 'AL': ['82'], 'AP': ['96'], 'AM': ['92', '97'],
        'BA': ['71', '73', '74', '75', '77'], 'CE': ['85', '88'],
        'DF': ['61'], 'ES': ['27', '28'], 'GO': ['62', '64'],
        'MA': ['98', '99'], 'MT': ['65', '66'], 'MS': ['67'],
        'MG': ['31', '32', '33', '34', '35', '37', '38'],
        'PA': ['91', '93', '94'], 'PB': ['83'], 'PR': ['41', '42', '43', '44', '45', '46'],
        'PE': ['81', '87'], 'PI': ['86', '89'], 'RJ': ['21', '22', '24'],
        'RN': ['84'], 'RS': ['51', '53', '54', '55'],
        'RO': ['69'], 'RR': ['95'], 'SC': ['47', '48', '49'],
        'SP': ['11', '12', '13', '14', '15', '16', '17', '18', '19'],
        'SE': ['79'], 'TO': ['63']
    }.get(estado, ['11'])  # Default para SP
    return f"({random.choice(ddd)}) {random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

def gerar_dados():
    # Listas de nomes masculinos e femininos
    nomes_masculinos = ["João Silva", "Carlos Souza", "Lucas Almeida", "Paulo Sérgio Costa", "Gustavo Fernandes", 
    "Felipe Duarte", "Pedro Gonçalves", "José Barbosa", "Thiago Matos", "Daniel Moreira", 
    "Vinicius Alves", "Matheus Ribeiro", "Henrique Teixeira", "Rodrigo Costa", "Eduardo Lima", 
    "Rafael Pereira", "André Silva", "Diego Mendes", "Gabriel Alves", "Bruno Oliveira", 
    "Leonardo Azevedo", "Marcelo Almeida", "Antonio Melo", "Miguel Santana", "Guilherme Ferreira", 
    "Caio Souza", "Ruan Ribeiro", "Arthur Rocha", "Junior Santos", "Heitor Martins", "Vitor Lima", 
    "Igor Alves", "Hugo Fernandes", "Otávio Ribeiro", "Leandro Batista", "Pablo Matos", "Fábio Gomes", 
    "Robson Lima", "Patrick Oliveira", "Diogo Gonçalves", "Roberto Santos", "Alan Nunes", "Wagner Almeida", 
    "Otávio Nunes", "Samuel Silva", "Enzo Costa", "Filipe Cardoso", "Victor Araújo", "Murilo Santos", 
    "Danilo Costa", "Alexandre Martins", "Cláudio Rocha", "Francisco Pereira", "Ricardo Teixeira", 
    "Fabiano Oliveira", "Leandro Nunes", "Douglas Lima", "Marcos Silva", "Eduardo Rocha", "Alex Silva", 
    "Lucas Teixeira", "Thiago Almeida", "Gustavo Costa", "Vinícius Ribeiro", "Guilherme Santos", 
    "Robson Rocha", "Felipe Souza", "Afonso Martins", "William Almeida", "Daniela Costa", "Marcelo Santos", 
    "Fernando Azevedo", "Arthur Teixeira", "Tiago Lima", "Renato Ribeiro", "Claudio Fernandes", "Lucas Mendes", 
    "Gabriel Cardoso", "Victor Pereira", "Maurício Silva", "Vítor Souza", "Carlos Martins", "André Barbosa", 
    "Felipe Nunes", "Mateus Souza", "David Lima", "Thiago Ribeiro", "Pedro Martins", "Leandro Souza", 
    "Vanderlei Silva", "Wagner Santos", "Paulo Azevedo", "Hugo Almeida", "Luiz Costa", "Alexandre Azevedo", 
    "Ricardo Barbosa", "Fábio Ribeiro", "Vinicius Nunes", "Carlos Azevedo", "Thiago Gomes", "Davi Lima", 
    "Roberto Silva", "Pablo Costa", "Samuel Pereira", "Rafael Nunes", "Renato Santos", "André Costa", 
    "Eduardo Ribeiro", "Marcelo Lima", "Bruno Azevedo", "Diego Teixeira", "Maurício Costa", "Gustavo Almeida", 
    "Ricardo Silva", "Vítor Ribeiro", "Marcelo Nunes", "Alan Rocha", "Robson Ribeiro", "Victor Nunes", 
    "Hugo Costa", "Marcos Ribeiro", "Vinicius Gomes", "Afonso Silva", "Felipe Pereira", "Leonardo Ribeiro", 
    "Carlos Souza", "Júlio Teixeira", "Gabriel Rocha", "Arthur Silva", "Felipe Gomes", "Paulo Ribeiro", 
    "Rafael Costa", "Tiago Santos", "Alex Ribeiro", "Bruno Mendes", "Carlos Teixeira", "Vítor Gomes", 
    "Samuel Nunes", "Leandro Pereira", "Lucas Gomes", "Danilo Ribeiro", "Felipe Fernandes", "Ricardo Lima", 
    "Pedro Souza", "Gilberto Nunes", "Douglas Ribeiro", "Mateus Ribeiro", "Rafael Gomes", "Alan Santos"
    ]
    
    nomes_femininos = ["Rosa Pietra Sophia Fogaca", "Maria Oliveira", "Ana Beatriz Martins", 
        "Fernanda Pereira", "Mariana Gonçalves", "Clara Mendes", "Isabella Ribeiro", "Camila Araújo", "Sofia Carvalho", "Laura Nunes",
        "Gabriela Rocha", "Julia Ferreira", "Lara Santos", "Luana Souza", "Livia Andrade", "Yasmin Almeida", "Alice Martins",
        "Helena Correia", "Sophia Machado", "Valentina Barbosa", "Carolina Rocha", "Beatriz Nunes", "Cecilia Fernandes", "Clara Gomes",
        "Lorena Vieira", "Renata Cardoso", "Marina Moreira", "Amanda Costa", "Flávia Silva", "Elisa Nunes", "Nicole Ferreira",
        "Rafaela Mendes", "Marcia Souza", "Tainá Araújo", "Letícia Pereira", "Joana Andrade", "Aline Duarte", "Cristina Nogueira", "Larissa Teixeira",
        "Emilly Carvalho", "Daniela Souza", "Bruna Martins", "Sandra Costa", "Mirela Ferreira",
        "Lorraine Vieira", "Isabel Fernandes", "Melina Rocha",
        "Stephanie Souza", "Clarice Matos", "Geovana Pereira", "Eduarda Alves",
        "Jéssica Almeida", "Bianca Ribeiro", "Marcela Souza", "Sara Martins",
        "Amanda Gonçalves", "Manuela Lima", "Raquel Mendes", "Lívia Fernandes"
    ]

    # Escolher aleatoriamente entre masculino e feminino
    sexo = random.choice(["Masculino", "Feminino"])
    
    # Escolher um nome correspondente ao sexo
    if sexo == "Masculino":
        nome = random.choice(nomes_masculinos)
    else:
        nome = random.choice(nomes_femininos)

    # Gerar email a partir do nome
    email = nome.lower().replace(' ', '.') + "@gmail.com"

    # Outros dados
    signos = ["Áries", "Touro", "Gêmeos", "Câncer", "Leão", "Virgem", "Libra", "Escorpião", "Sagitário", "Capricórnio", "Aquário", "Peixes"]
    estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
    cidades = {
        "AC": ["Rio Branco", "Cruzeiro do Sul"],
        "AL": ["Maceió", "Arapiraca"],
        "AP": ["Macapá", "Santana"],
        "AM": ["Manaus", "Parintins"],
        "BA": ["Salvador", "Feira de Santana"],
        "CE": ["Fortaleza", "Caucaia"],
        "DF": ["Brasília"],
        "ES": ["Vitória", "Cariacica"],
        "GO": ["Goiânia", "Anápolis"],
        "MA": ["São Luís", "Imperatriz"],
        "MT": ["Cuiabá", "Várzea Grande"],
        "MS": ["Campo Grande", "Dourados"],
        "MG": ["Belo Horizonte", "Uberlândia"],
        "PA": ["Belém", "Ananindeua"],
        "PB": ["João Pessoa", "Campina Grande"],
        "PR": ["Curitiba", "Londrina"],
        "PE": ["Recife", "Jaboatão dos Guararapes"],
        "PI": ["Teresina", "Parnaíba"],
        "RJ": ["Rio de Janeiro", "São Gonçalo"],
        "RN": ["Natal", "Mossoró"],
        "RS": ["Porto Alegre", "Caxias do Sul"],
        "RO": ["Porto Velho", "Ji-Paraná"],
        "RR": ["Boa Vista"],
        "SC": ["Florianópolis", "Joinville"],
        "SP": ["São Paulo", "Guarulhos"],
        "SE": ["Aracaju", "Nossa Senhora do Socorro"],
        "TO": ["Palmas", "Araguaína"]
    }
    # Dicionários de bairros por estado
    bairros_por_estado = {
        "RJ": ["Copacabana", "Ipanema", "Leblon", "Barra da Tijuca", "Tijuca", 
               "Botafogo", "Flamengo", "Laranjeiras", "Santa Teresa", "Centro",
               "Vila Isabel", "Grajaú", "Jacarepaguá", "Recreio dos Bandeirantes",
               "São Conrado", "Gávea", "Jardim Botânico", "Catete", "Cosme Velho",
               "Leme", "Urca", "Rocinha", "Vidigal", "Méier", "Madureira"],
        
        "SP": ["Moema", "Pinheiros", "Vila Madalena", "Itaim Bibi", "Jardins",
              "Morumbi", "Brooklin", "Liberdade", "Bela Vista", "Consolação",
              "Perdizes", "Vila Olímpia", "Santo Amaro", "Lapa", "Tatuapé",
              "Vila Mariana", "Higienópolis", "Campo Belo", "Paraíso", "Butantã",
              "Santana", "Vila Leopoldina", "Alphaville", "Interlagos", "Ipiranga"],
        
        "MG": ["Savassi", "Funcionários", "Lourdes", "Sion", "Belo Horizonte",
              "Santa Tereza", "Pampulha", "Cidade Nova", "Barro Preto", "Nova Lima",
              "Contagem", "Betim", "Venda Nova", "Santa Efigênia", "Horto"],
        
        "BA": ["Barra", "Ondina", "Rio Vermelho", "Pituba", "Brotas",
              "Graça", "Caminho das Árvores", "Horto Florestal", "Stella Maris",
              "Itaigara", "Cabula", "Liberdade", "Pelourinho", "Comércio", "Federação"],
        
        "RS": ["Moinhos de Vento", "Bela Vista", "Petrópolis", "Boa Vista", "Menino Deus",
              "Jardim Botânico", "Tristeza", "Cidade Baixa", "Centro Histórico", "Santana",
              "Partenon", "Vila Assunção", "Auxiliadora", "Floresta", "Independência"],
        
        "PR": ["Batel", "Água Verde", "Bigorrilho", "Centro Cívico", "Cabral",
              "Mercês", "Jardim Social", "Cristo Rei", "Portão", "Santa Felicidade",
              "Vila Izabel", "Hugo Lange", "Alto da Glória", "Seminário", "Juvevê"],
        
        "PE": ["Boa Viagem", "Pina", "Brasília Teimosa", "Casa Forte", "Graças",
              "Espinheiro", "Parnamirim", "Poço da Panela", "Santana", "Apipucos",
              "Madalena", "Torre", "Derby", "Ilha do Leite", "Santo Antônio"],
        
        "CE": ["Meireles", "Aldeota", "Praia de Iracema", "Dionísio Torres", "Varjota",
              "Benfica", "Fátima", "Parquelândia", "Montese", "Jardim América",
              "Cocó", "Papicu", "Cambeba", "Edson Queiroz", "Sapiranga"],
        
        "DF": ["Asa Sul", "Asa Norte", "Lago Sul", "Lago Norte", "Sudoeste",
              "Cruzeiro", "Guará", "Taguatinga", "Águas Claras", "Sobradinho",
              "Planaltina", "Gama", "Brazlândia", "Núcleo Bandeirante", "Park Way"]
    }
    
    # Dicionários de endereços por estado
    enderecos_por_estado = {
        "RJ": [
            "Avenida Atlântica, 1702", "Rua Visconde de Pirajá, 142", "Avenida Ayrton Senna, 3000",
            "Rua das Laranjeiras, 300", "Rua Conde de Bonfim, 500", "Rua General Glicério, 200",
            "Rua Marquês de São Vicente, 100", "Rua Voluntários da Pátria, 300", "Rua Jardim Botânico, 700",
            "Rua Dias Ferreira, 200", "Avenida Vieira Souto, 400", "Rua Barão da Torre, 300",
            "Rua Santa Clara, 100", "Rua Siqueira Campos, 150", "Rua Tonelero, 200"
        ],
        
        "SP": [
            "Avenida Paulista, 1000", "Rua Oscar Freire, 800", "Rua Haddock Lobo, 500",
            "Avenida Brigadeiro Faria Lima, 2000", "Rua Augusta, 1500", "Alameda Santos, 500",
            "Avenida Rebouças, 1000", "Rua da Consolação, 700", "Rua Bela Cintra, 300",
            "Avenida Europa, 200", "Rua Estados Unidos, 100", "Rua Joaquim Floriano, 400",
            "Rua Dr. Melo Alves, 200", "Avenida Angélica, 300", "Rua Pamplona, 500"
        ],
        
        "MG": [
            "Avenida Getúlio Vargas, 1000", "Rua da Bahia, 500", "Avenida do Contorno, 2000",
            "Rua Cláudio Manoel, 300", "Rua Antônio de Albuquerque, 400", "Avenida Afonso Pena, 1500",
            "Rua Tupis, 200", "Rua dos Inconfidentes, 300", "Avenida Cristóvão Colombo, 500",
            "Rua Professor Moraes, 100", "Rua Alagoas, 200", "Rua Espírito Santo, 300",
            "Rua Curitiba, 400", "Rua dos Otoni, 500", "Rua Gonçalves Dias, 600"
        ],
        
        "BA": [
            "Avenida Oceânica, 100", "Rua Portugal, 200", "Avenida Sete de Setembro, 300",
            "Rua João das Botas, 400", "Rua Marques de Leão, 500", "Avenida Tancredo Neves, 1000",
            "Rua das Hortênsias, 200", "Rua Patrocínio, 300", "Avenida ACM, 500",
            "Rua Dias D'Ávila, 400", "Rua do Tijolo, 100", "Rua do Paço, 200",
            "Rua Chile, 300", "Rua Carlos Gomes, 400", "Rua da Graça, 500"
        ],
        
        "RS": [
            "Avenida Ipiranga, 1000", "Rua da República, 500", "Avenida João Pessoa, 200",
            "Rua Gonçalo de Carvalho, 300", "Rua Santana, 400", "Avenida Getúlio Vargas, 500",
            "Rua Castro Alves, 100", "Rua Ramiro Barcelos, 200", "Avenida Protásio Alves, 300",
            "Rua João Alfredo, 400", "Rua Venâncio Aires, 500", "Rua Dr. Timóteo, 100",
            "Rua Lima e Silva, 200", "Rua Sarmento Leite, 300", "Rua Andrade Neves, 400"
        ],
        
        "PR": [
            "Avenida Batel, 1000", "Rua XV de Novembro, 500", "Avenida Visconde de Guarapuava, 200",
            "Rua Marechal Deodoro, 300", "Rua Trajano Reis, 400", "Avenida República Argentina, 500",
            "Rua Brigadeiro Franco, 100", "Rua Desembargador Motta, 200", "Avenida Silva Jardim, 300",
            "Rua Padre Anchieta, 400", "Rua Comendador Araújo, 500", "Rua 24 de Maio, 100",
            "Rua São Francisco, 200", "Rua Saldanha Marinho, 300", "Rua Cândido Lopes, 400"
        ],
        
        "PE": [
            "Avenida Boa Viagem, 1000", "Rua do Riachuelo, 500", "Avenida Conde da Boa Vista, 200",
            "Rua da Aurora, 300", "Rua do Sol, 400", "Avenida Agamenon Magalhães, 500",
            "Rua do Hospício, 100", "Rua Gervásio Pires, 200", "Avenida Dantas Barreto, 300",
            "Rua da Hora, 400", "Rua Sete de Setembro, 500", "Rua do Imperador, 100",
            "Rua da Matriz, 200", "Rua do Amparo, 300", "Rua da Concórdia, 400"
        ],
        
        "CE": [
            "Avenida Beira Mar, 1000", "Rua Ildefonso Albano, 500", "Avenida Dom Luís, 200",
            "Rua Barbosa de Freitas, 300", "Rua José Vilar, 400", "Avenida Santos Dumont, 500",
            "Rua Carlos Vasconcelos, 100", "Rua Professor Dias da Rocha, 200", "Avenida Washington Soares, 300",
            "Rua Canuto de Aguiar, 400", "Rua Osório de Paiva, 500", "Rua 24 de Maio, 100",
            "Rua Guilherme Rocha, 200", "Rua Senador Pompeu, 300", "Rua Pedro I, 400"
        ],
        
        "DF": [
            "SHIS QI 5 Bloco A", "CLS 104 Bloco C", "SQS 302 Bloco B",
            "CLN 202 Bloco D", "SCS Qd. 7 Bloco A", "SHIN QI 11 Bloco F",
            "CLSW 301 Bloco B", "SHS Quadra 3 Bloco A", "CLN 404 Bloco C",
            "SCES Trecho 2", "SMDB Conjunto 12", "SHDB Conjunto 25",
            "CLN 106 Bloco B", "SCEN Trecho 2", "SGAN 601 Módulo D"
        ]
    }
    tipo_sanguineo = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

    estado = random.choice(estados)
    cidade = random.choice(cidades[estado])
    bairro = random.choice(bairros_por_estado.get(estado, ["Centro"]))  # Default para "Centro" se estado não estiver na lista
    endereco = random.choice(enderecos_por_estado.get(estado, ["Rua Principal, 100"]))  # Default se estado não estiver na lista
    cep = f"{random.randint(10000, 99999)}-{random.randint(100, 999)}"

    return {
        "nome": nome,
        "cpf": gerar_cpf(),
        "rg": gerar_rg(),
        "data_nasc": gerar_data_nascimento(),
        "sexo": sexo,
        "signo": random.choice(signos),
        "mae": f"Josefa {random.choice(['Antônia', 'Maria', 'Clara'])}",
        "pai": f"Marcelo {random.choice(['Pedro', 'João', 'Carlos'])} Silva",
        "email": email,
        "cep": cep,
        "endereço": endereco,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "telefone_fixo": gerar_telefone(estado),
        "celular": gerar_telefone(estado),
        "altura": f"1,{random.randint(50, 80)}",
        "tipo_sanguíneo": random.choice(tipo_sanguineo)
    }

def verificar_bin(bin):
    print(f"Verificando BIN: {bin}")
    banks = ["Banco do Brasil", "Itau", "Caixa Economica", "Bradesco"]
    random_bank = random.choice(banks)
    print(f"Banco: {random_bank}")
    print("País: Brasil")
    print("Tipo de Cartão: Crédito")

def testar_luhn(numero_cartao):
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10
    
    valido = luhn_checksum(int(numero_cartao)) == 0
    print(f"O número do cartão {numero_cartao} é {'válido' if valido else 'inválido'}.")

def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Gerar Cartão de Crédito")
        print("2. Verificar BIN")
        print("3. Testar Luhn")
        print("4. Gerar Dados")
        print("5. Gerar Cartões em Lote")
        print("6. Sair")
        opcao = input("Opção: ")
        
        if opcao == "1":
            cartao = gerar_numero_cartao()
            print(f"Cartão gerado: {formata_cartao(cartao)}")
        elif opcao == "2":
            bin = input("Digite os primeiros 6 dígitos (BIN): ")
            if len(bin) == 6 and bin.isdigit():
                verificar_bin(bin)
            else:
                print("BIN inválido. Deve conter exatamente 6 dígitos.")
        elif opcao == "3":
            numero_cartao = input("Digite o número do cartão: ")
            if numero_cartao.isdigit():
                testar_luhn(numero_cartao)
            else:
                print("Número do cartão inválido. Deve conter apenas dígitos.")
        elif opcao == "4":
            dados = gerar_dados()
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
        elif opcao == "5":
            quantidade = int(input("Digite a quantidade de cartões de crédito que deseja gerar: "))
            cartoes = gera_cartoes_em_lote(quantidade)
            for cartao in cartoes:
                print(cartao)
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()