from datetime import datetime

class Propriedade:
    def __init__(self, codigo, endereco, preco):
        self.codigo = codigo
        self.endereco = endereco
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}, Endereço: {self.endereco}, Preço: {self.preco}")


class PerfilAgente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome do Agente: {self.nome}, E-mail do Agente: {self.email}")


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

    def adicionar_propriedade(self, propriedade):
        self.propriedades.append(propriedade)

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
    
    def obter_perfil_agente_por_nome(self, nome):
        for perfil in self.perfis_agentes:
            if perfil.nome == nome:
                return perfil
        return None

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

        propriedade = Propriedade(codigo, endereco, preco)
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
    else:
        print("Opção inválida. Tente novamente.")

