from modulo_menu import Menu
# criar funções
# módulo + pessoas > contas > cliente + agencia + banco > usuário
# shift + ctrl + l = comenta / ctrl + l = descomenta


class Contas:
    def __init__(self):
        self.lista_json_variavel = 'lista_conta.json'
        self.lista_json_variavel_2 = 'lista_pessoa.json'
        self.classe = Contas
        self.classe_nome = Contas.__name__
        self.classe_funcao = Contas.listar_contas
        self.lista_variavel = [[], []]
        self.tipo_variavel = 'Tipo Conta'
        self.tipo_variavel_1 = 'Conta Corrente'
        self.tipo_variavel_2 = 'Conta Poupança'

        Menu.menu_opcao(self, self.__dict__)
                   
    def listar_contas(self, opcao, valor_variavel):

        if valor_variavel == self.tipo_variavel_1:

            return ContaCorrente(self.__dict__, opcao, valor_variavel, self.tipo_variavel_1, self.tipo_variavel_2)
        ContaPoupanca(self.__dict__, opcao, valor_variavel, self.tipo_variavel_1, self.tipo_variavel_2)


class ContaCorrente:
    
    def __init__(self, lista_menu, opcao, valor_variavel, tipo_variavel_1, tipo_variavel_2):  
        
        return Menu.menu_acao(self, lista_menu, opcao, valor_variavel, 
        tipo_variavel_1, tipo_variavel_2, 'Número da Conta', 'RG', 'CNPJ')
    

class ContaPoupanca:    
    
    def __init__(self, lista_menu, opcao, valor_variavel, tipo_variavel_1, tipo_variavel_2):

        return Menu.menu_acao(self, lista_menu, opcao, valor_variavel, 
        tipo_variavel_1, tipo_variavel_2, 'Número da Conta', 'RG', True)
    

Contas()


##########################
