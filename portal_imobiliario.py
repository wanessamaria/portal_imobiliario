from datetime import datetime
import folium
import os

class Avaliacao:
    def __init__(self, usuario, comentario, classificacao):
        self.usuario = usuario
        self.comentario = comentario
        self.classificacao = classificacao

    def exibir_informacoes(self):
        print(f"Usuário: {self.usuario}")
        print(f"Comentário: {self.comentario}")
        print(f"Classificação: {self.classificacao}")

class CalculadoraHipoteca:
    def calcular_pagamento_mensal(self, valor_emprestimo, taxa_juros, anos):
        # Fórmula para calcular o pagamento mensal de uma hipoteca
        taxa_juros_mensal = (taxa_juros / 100) / 12
        numero_pagamentos = anos * 12
        pagamento_mensal = (valor_emprestimo * taxa_juros_mensal) / (1 - (1 + taxa_juros_mensal) ** -numero_pagamentos)
        return pagamento_mensal

class Mapa:
    def __init__(self):
        self.propriedades = []

    def adicionar_propriedade(self, propriedade):
        self.propriedades.append(propriedade)

    def exibir_mapa_interativo(self):
        # Cria um mapa centrado em uma localização inicial
        mapa = folium.Map(location=[-23.5505, -46.6333], zoom_start=10)  # Pode ajustar as coordenadas e o nível de zoom

        # Adiciona marcadores para cada propriedade
        for propriedade in self.propriedades:
            folium.Marker([propriedade.latitude, propriedade.longitude], popup=propriedade.endereco).add_to(mapa)

        # Exibe o mapa interativo (pode ser aberto em um navegador)
        mapa.save(os.path.join(os.getcwd(), 'mapa_interativo.html'))
        print("Mapa interativo gerado. Abra o arquivo 'mapa_interativo.html' em um navegador para visualizá-lo.")

class AnaliseMercado:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao

    def exibir_informacoes(self):
        print(f"Título da Análise: {self.titulo}")
        print(f"Descrição da Análise: {self.descricao}")

class ConsultaCliente:
    def __init__(self, cliente, agente, data_hora):
        self.cliente = cliente
        self.agente = agente
        self.data_hora = data_hora

    def exibir_informacoes(self):
        print(f"Consulta para o cliente {self.cliente}:")
        print(f"Agendada por: {self.agente.nome}")
        print(f"Data e Hora: {self.data_hora}")

class TourVirtual:
    def __init__(self, descricao, url):
        self.descricao = descricao
        self.url = url

    def exibir_informacoes(self):
        print(f"Descrição do Tour Virtual: {self.descricao}")
        print(f"URL do Tour Virtual: {self.url}")


class Propriedade:
    def __init__(self, codigo, endereco, preco, latitude, longitude):
        self.codigo = codigo
        self.endereco = endereco
        self.preco = preco
        self.latitude = latitude
        self.longitude = longitude
        self.tours_virtuais = []
        self.avaliacoes = []

    def adicionar_tour_virtual(self, tour_virtual):
        self.tours_virtuais.append(tour_virtual)

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}, Endereço: {self.endereco}, Preço: {self.preco}")
        print(f"Localização: Latitude {self.latitude}, Longitude {self.longitude}")
        print("Tours Virtuais:")
        for tour_virtual in self.tours_virtuais:
            tour_virtual.exibir_informacoes()
        print("Avaliações:")
        for avaliacao in self.avaliacoes:
            avaliacao.exibir_informacoes()



class PerfilAgente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.avaliacoes = []

    def adicionar_avaliacao(self, avaliacao):
        self.avaliacoes.append(avaliacao)

    def exibir_informacoes(self):
        print(f"Nome do Agente: {self.nome}, E-mail do Agente: {self.email}")
        print("Avaliações:")
        for avaliacao in self.avaliacoes:
            avaliacao.exibir_informacoes()


class Consulta:
    def __init__(self, propriedade, agente, cliente, data_hora):
        self.propriedade = propriedade
        self.agente = agente
        self.cliente = cliente
        self.data_hora = data_hora

    def exibir_informacoes(self):
        print(f"Consulta para a propriedade {self.propriedade.codigo}:")
        print(f"Agendada por: {self.agente.nome}")
        print(f"Cliente: {self.cliente}")
        print(f"Data e Hora: {self.data_hora}")


class GerenciadorPropriedades:
    def __init__(self):
        self.propriedades = []
        self.perfis_agentes = []
        self.consultas = []
        self.consultas_clientes = []
        self.analises_mercado = []
        self.mapa = Mapa()

    def adicionar_propriedade(self, propriedade):
        self.propriedades.append(propriedade)
        self.mapa.adicionar_propriedade(propriedade)

    def exibir_mapa_interativo(self):
        self.mapa.exibir_mapa_interativo()

    def listar_propriedades(self):
        print("Lista de Propriedades:")
        for propriedade in self.propriedades:
            propriedade.exibir_informacoes()

    def editar_propriedade(self, codigo, novo_endereco, novo_preco):
        for propriedade in self.propriedades:
            if propriedade.codigo == codigo:
                propriedade.endereco = novo_endereco
                propriedade.preco = novo_preco
                print(f"A propriedade {codigo} foi editada com sucesso.")
                return
        print(f"Propriedade com o código {codigo} não encontrada.")

    def excluir_propriedade(self, codigo):
        for propriedade in self.propriedades:
            if propriedade.codigo == codigo:
                self.propriedades.remove(propriedade)
                print(f"A propriedade {codigo} foi excluída com sucesso.")
                return
        print(f"Propriedade com o código {codigo} não encontrada.")

    def adicionar_perfil_agente(self, perfil):
        self.perfis_agentes.append(perfil)

    def listar_perfis_agentes(self):
        print("Lista de Perfis de Agentes:")
        for perfil in self.perfis_agentes:
            perfil.exibir_informacoes()

    def editar_perfil_agente(self, nome_antigo, novo_nome, novo_email):
        for perfil in self.perfis_agentes:
            if perfil.nome == nome_antigo:
                perfil.nome = novo_nome
                perfil.email = novo_email
                print(f"O perfil do agente {nome_antigo} foi editado com sucesso.")
                return
        print(f"Perfil do agente {nome_antigo} não encontrado.")

    def excluir_perfil_agente(self, nome):
        for perfil in self.perfis_agentes:
            if perfil.nome == nome:
                self.perfis_agentes.remove(perfil)
                print(f"O perfil do agente {nome} foi excluído com sucesso.")
                return
        print(f"Perfil do agente {nome} não encontrado.")

    def agendar_consulta(self, codigo_propriedade, agente, cliente, data_hora):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            consulta = Consulta(propriedade, agente, cliente, data_hora)
            self.consultas.append(consulta)
            print("Consulta agendada com sucesso!")
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def listar_consultas(self):
        print("Lista de Consultas:")
        for consulta in self.consultas:
            consulta.exibir_informacoes()

    def obter_propriedade_por_codigo(self, codigo):
        for propriedade in self.propriedades:
            if propriedade.codigo == codigo:
                return propriedade
        return None

    def adicionar_tour_virtual(self, codigo_propriedade, descricao, url):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            tour_virtual = TourVirtual(descricao, url)
            propriedade.adicionar_tour_virtual(tour_virtual)
            print(f"Tour Virtual adicionado à propriedade {codigo_propriedade} com sucesso!")
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def listar_tours_virtuais(self, codigo_propriedade):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            print(f"Tours Virtuais para a propriedade {codigo_propriedade}:")
            for tour_virtual in propriedade.tours_virtuais:
                tour_virtual.exibir_informacoes()
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def obter_perfil_agente_por_nome(self, nome):
        for perfil in self.perfis_agentes:
            if perfil.nome == nome:
                return perfil
        return None
    def agendar_consulta_cliente(self, cliente, agente, data_hora):
        consulta_cliente = ConsultaCliente(cliente, agente, data_hora)
        self.consultas_clientes.append(consulta_cliente)
        print("Consulta de cliente agendada com sucesso!")

    def listar_consultas_clientes(self):
        print("Lista de Consultas de Clientes:")
        for consulta_cliente in self.consultas_clientes:
            consulta_cliente.exibir_informacoes()

    def obter_perfil_cliente_por_nome(self, nome):
        for perfil in self.perfis_clientes:
            if perfil.nome == nome:
                return perfil
        return None
    def adicionar_analise_mercado(self, titulo, descricao):
        analise_mercado = AnaliseMercado(titulo, descricao)
        self.analises_mercado.append(analise_mercado)
        print("Análise de mercado adicionada com sucesso!")
    def listar_analises_mercado(self):
        print("Lista de Análises de Mercado:")
        for analise_mercado in self.analises_mercado:
            analise_mercado.exibir_informacoes()
    def calcular_pagamento_hipoteca(self, codigo_propriedade, valor_emprestimo, taxa_juros, anos):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)
        if propriedade:
            calculadora_hipoteca = CalculadoraHipoteca()
            pagamento_mensal = calculadora_hipoteca.calcular_pagamento_mensal(valor_emprestimo, taxa_juros, anos)
            print(f"O pagamento mensal estimado para a propriedade {codigo_propriedade} é de R${pagamento_mensal:.2f}.")       
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")
    def avaliar_propriedade(self, codigo_propriedade):
        propriedade = self.obter_propriedade_por_codigo(codigo_propriedade)

        if propriedade:
            usuario = input("Digite seu nome de usuário: ")
            comentario = input("Digite seu comentário: ")
            classificacao = int(input("Digite a classificação (de 1 a 5): "))

            avaliacao = Avaliacao(usuario, comentario, classificacao)
            propriedade.adicionar_avaliacao(avaliacao)
            print("Avaliação adicionada com sucesso!")
        else:
            print(f"Propriedade com código {codigo_propriedade} não encontrada.")

    def avaliar_agente(self, nome_agente):
        agente = self.obter_perfil_agente_por_nome(nome_agente)

        if agente:
            usuario = input("Digite seu nome de usuário: ")
            comentario = input("Digite seu comentário: ")
            classificacao = int(input("Digite a classificação (de 1 a 5): "))

            avaliacao = Avaliacao(usuario, comentario, classificacao)
            agente.adicionar_avaliacao(avaliacao)
            print("Avaliação adicionada com sucesso!")
        else:
            print(f"Agente com o nome {nome_agente} não encontrado.")




# Função para obter entrada do usuário para agendar uma consulta
def obter_entrada_consulta(gerenciador):
    codigo_propriedade = input("Digite o código da propriedade para a consulta: ")
    
    # Lista os perfis de agentes para o usuário escolher quem está agendando a consulta
    print("Lista de Perfis de Agentes:")
    gerenciador.listar_perfis_agentes()
    
    agente_nome = input("Digite o nome do agente que está agendando a consulta: ")
    agente = gerenciador.obter_perfil_agente_por_nome(agente_nome)
    
    if not agente:
        print(f"Agente com o nome {agente_nome} não encontrado.")
        return None
    
    cliente = input("Digite o nome do cliente: ")
    data_hora_str = input("Digite a data e hora da consulta (formato: YYYY-MM-DD HH:MM): ")

    try:
        data_hora = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M")
    except ValueError:
        print("Formato de data e hora inválido. Use o formato: YYYY-MM-DD HH:MM")
        return None

    return codigo_propriedade, agente, cliente, data_hora

# Função para obter entrada do usuário para adicionar um tour virtual
def obter_entrada_tour_virtual(gerenciador):
    codigo_propriedade = input("Digite o código da propriedade para adicionar o Tour Virtual: ")
    descricao = input("Digite a descrição do Tour Virtual: ")
    url = input("Digite a URL do Tour Virtual: ")

    return codigo_propriedade, descricao, url

# Função para obter entrada do usuário
def obter_entrada_usuario():
    print("\nEscolha uma opção:")
    print("1 - Adicionar Propriedade")
    print("2 - Listar Propriedades")
    print("3 - Editar Propriedade")
    print("4 - Excluir Propriedade")
    print("5 - Adicionar Perfil de Agente")
    print("6 - Listar Perfis de Agentes")
    print("7 - Editar Perfil de Agente")
    print("8 - Excluir Perfil de Agente")
    print("9 - Agendar Consulta")
    print("10 - Listar Consultas")
    print("11 - Adicionar Tour Virtual")
    print("12 - Listar Tours Virtuais")
    print("13 - Agendar Consulta de Cliente")
    print("14 - Listar Consultas de Clientes")
    print("15 - Adicionar Análise de Mercado")
    print("16 - Listar Análises de Mercado")
    print("17 - Exibir Mapa Interativo")
    print("18 - Calculadora de Hipoteca")
    print("19 - Avaliar Propriedade")
    print("20 - Avaliar Agente")
    print("0 - Sair")

    return input("Digite o número da opção desejada: ")

# Exemplo de uso com interação do usuário
gerenciador = GerenciadorPropriedades()

while True:
    escolha = obter_entrada_usuario()

    if escolha == "0":
        print("Saindo do programa. Até mais!")
        break
    elif escolha == "1":
        codigo = input("Digite o código da propriedade: ")
        endereco = input("Digite o endereço da propriedade: ")
        preco = input("Digite o preço da propriedade: ")
        latitude = input("Digite a latitude da propriedade: ")
        longitude = input("Digite a longitude da propriedade: ")

        propriedade = Propriedade(codigo, endereco, preco, latitude, longitude)
        gerenciador.adicionar_propriedade(propriedade)
        print("Propriedade adicionada com sucesso!")
    elif escolha == "2":
        gerenciador.listar_propriedades()
    elif escolha == "3":
        codigo = input("Digite o código da propriedade que deseja editar: ")
        novo_endereco = input("Digite o novo endereço: ")
        novo_preco = input("Digite o novo preço: ")

        gerenciador.editar_propriedade(codigo, novo_endereco, novo_preco)
    elif escolha == "4":
        codigo = input("Digite o código da propriedade que deseja excluir: ")
        gerenciador.excluir_propriedade(codigo)
    elif escolha == "5":
        nome_agente = input("Digite o nome do agente: ")
        email_agente = input("Digite o email do agente: ")

        perfil_agente = PerfilAgente(nome_agente, email_agente)
        gerenciador.adicionar_perfil_agente(perfil_agente)
        print("Perfil do agente adicionado com sucesso!")
    elif escolha == "6":
        gerenciador.listar_perfis_agentes()
    elif escolha == "7":
        nome_antigo = input("Digite o nome do agente que deseja editar: ")
        novo_nome_agente = input("Digite o novo nome do agente: ")
        novo_email_agente = input("Digite o novo email do agente: ")

        gerenciador.editar_perfil_agente(nome_antigo, novo_nome_agente, novo_email_agente)
    elif escolha == "8":
        nome_agente_excluir = input("Digite o nome do agente que deseja excluir: ")
        gerenciador.excluir_perfil_agente(nome_agente_excluir)
    elif escolha == "9":
        entrada_consulta = obter_entrada_consulta(gerenciador)
        if entrada_consulta:
            gerenciador.agendar_consulta(*entrada_consulta)
    elif escolha == "10":
        gerenciador.listar_consultas()
    elif escolha == "11":
        entrada_tour_virtual = obter_entrada_tour_virtual(gerenciador)
        if entrada_tour_virtual:
            gerenciador.adicionar_tour_virtual(*entrada_tour_virtual)
    elif escolha == "12":
        codigo_propriedade_tour_virtual = input("Digite o código da propriedade para listar os Tours Virtuais: ")
        gerenciador.listar_tours_virtuais(codigo_propriedade_tour_virtual)
    elif escolha == "13":
        cliente_nome = input("Digite o nome do cliente para a consulta: ")
        agente_nome = input("Digite o nome do agente que está agendando a consulta: ")
        agente = gerenciador.obter_perfil_agente_por_nome(agente_nome)

        if not agente:
            print(f"Agente com o nome {agente_nome} não encontrado.")
            continue

        data_hora_str = input("Digite a data e hora da consulta (formato: YYYY-MM-DD HH:MM): ")

        try:
            data_hora = datetime.strptime(data_hora_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Formato de data e hora inválido. Use o formato: YYYY-MM-DD HH:MM")
            continue

        gerenciador.agendar_consulta_cliente(cliente_nome, agente, data_hora)
    elif escolha == "14":
        gerenciador.listar_consultas_clientes()
    elif escolha == "15":
        titulo_analise = input("Digite o título da análise de mercado: ")
        descricao_analise = input("Digite a descrição da análise de mercado: ")
        gerenciador.adicionar_analise_mercado(titulo_analise, descricao_analise)

    elif escolha == "16":
        gerenciador.listar_analises_mercado()
    elif escolha == "17":
        print("Diretório Atual:", os.getcwd())
        gerenciador.exibir_mapa_interativo()
    elif escolha == "18":
        codigo_propriedade_hipoteca = input("Digite o código da propriedade para calcular a hipoteca: ")
        valor_emprestimo = float(input("Digite o valor do empréstimo: "))
        taxa_juros = float(input("Digite a taxa de juros anual (%): "))
        anos = int(input("Digite o número de anos do empréstimo: "))

        gerenciador.calcular_pagamento_hipoteca(codigo_propriedade_hipoteca, valor_emprestimo, taxa_juros, anos)
    elif escolha == "19":
        gerenciador.avaliar_propriedade(input("Digite o código da propriedade para avaliar: "))
    elif escolha == "20":
        gerenciador.avaliar_agente(input("Digite o nome do agente para avaliar: "))
    else:
        print("Opção inválida. Tente novamente.")