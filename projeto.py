class Propriedade:
    def __init__(self, codigo, endereco, preco):
        self.codigo = codigo
        self.endereco = endereco
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Código: {self.codigo}, Endereço: {self.endereco}, Preço: {self.preco}")


class GerenciadorPropriedades:
    def __init__(self):
        self.propriedades = []

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

    def filtrar_imoveis(self, criterios):
        imoveis_filtrados = []
        for propriedade in self.propriedades:
            if all(getattr(propriedade, atributo, None) == valor for atributo, valor in criterios.items()):
                imoveis_filtrados.append(propriedade)
        return imoveis_filtrados


# Função para obter entrada do usuário
def obter_entrada_usuario():
    print("\nEscolha uma opção:")
    print("1 - Adicionar Propriedade")
    print("2 - Listar Propriedades")
    print("3 - Editar Propriedade")
    print("4 - Excluir Propriedade")
    print("5 - Pesquisar Propriedades")
    print("0 - Sair")

    return input("Digite o número da opção desejada: ")


# Função para obter critérios de pesquisa do usuário
def obter_criterios_pesquisa():
    criterios = {}
    codigo = input("Digite o código da propriedade (ou deixe em branco para ignorar): ")
    if codigo:
        criterios['codigo'] = codigo

    endereco = input("Digite o endereço da propriedade (ou deixe em branco para ignorar): ")
    if endereco:
        criterios['endereco'] = endereco

    preco = input("Digite o preço da propriedade (ou deixe em branco para ignorar): ")
    if preco:
        criterios['preco'] = preco

    return criterios


# Exemplo de uso com interação do usuário e pesquisa
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
        criterios_pesquisa = obter_criterios_pesquisa()
        resultados_pesquisa = gerenciador.filtrar_imoveis(criterios_pesquisa)

        if resultados_pesquisa:
            print("\nResultados da Pesquisa:")
            for propriedade in resultados_pesquisa:
                propriedade.exibir_informacoes()
        else:
            print("\nNenhum imóvel encontrado com os critérios fornecidos.")
    else:
        print("Opção inválida. Tente novamente.")
