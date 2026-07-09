class Contas:
    def __init__(self, lista_menu_agencia):
        self.agencia = lista_menu_agencia['agencia']
        self.numero_agencia = lista_menu_agencia['numero_agencia']
        self.lista_transferencia = lista_menu_agencia['lista_transferencia']
        self.lista_json_transferencia = lista_menu_agencia['lista_json_transferencia']
        self.lista_json_variavel = 'lista_conta.json'
        self.classe = Contas
        self.classe_nome = Contas.__name__
        self.classe_funcao = Contas.listar_contas
        self.classe_opcao = Contas.opcao_menu
        self.lista_variavel = [[], []] 
        self.valor_saldo = 0
        self.extrato = 'Extrato'
        self.valor_extrato = 0
        self.debito = 'Débito'
        self.valor_debito = 0
        self.credito = 'Crédito'
        self.valor_credito = 0 
        self.tipo_variavel = 'Tipo Conta'
        self.tipo_variavel_1 = 'Conta Corrente'
        self.tipo_variavel_2 = 'Conta Poupança' 
        
    def opcao_menu(self):

        from modulo_menu_contas import Menu
        Menu.menu_opcao(self, self.__dict__)
                   
    def cadastrar_menu(self, lista_acao_contas, lista):
        
        from modulo_lista_contas import Lista
        Lista(self.__dict__, lista_acao_contas, lista)
                   
    def listar_contas(self, opcao, valor_variavel):

        if valor_variavel == self.tipo_variavel_1:
            ContaCorrente(self.__dict__, opcao, valor_variavel)
        ContaPoupanca(self.__dict__, opcao, valor_variavel)


class ContaCorrente:
    
    def __init__(self, lista_menu_contas, opcao, valor_variavel):  
        
        from modulo_menu_contas import Menu
        return Menu.menu_acao(self, lista_menu_contas, opcao, valor_variavel, 'Número da Conta', 'RG', 'CNPJ')
    

class ContaPoupanca:    
    
    def __init__(self, lista_menu_contas, opcao, valor_variavel):

        from modulo_menu_contas import Menu
        return Menu.menu_acao(self, lista_menu_contas, opcao, valor_variavel, 'Número da Conta', 'RG', True)
   
