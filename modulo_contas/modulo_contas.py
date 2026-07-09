"""
    Esse módulo inicia os tipos de conta disponíveis na agência: conta corrente
    (pessoa física ou jurídica) e conta poupança (pessoa física)"""

class Contas:   # _3.1.0

    def __init__(self, agencia):   # _3.1.1
        self.modulo_contas = agencia['modulo_contas']
        self.valor_agencia = agencia['valor_agencia']
        self.lista_boa_vista_bank_json = 'lista_boa_vista_bank.json'
        self.lista_agencia = ['0001']
        self.lista_conta_json = f'lista_conta_{self.valor_agencia}.json'
        self.lista_contas = [[], []] 
        self.lista_pessoa_json = f'lista_pessoa_{self.valor_agencia}.json'          
        self.lista_pessoa = [[], []]
        self.dado_rg = 'RG'
        self.dado_cnpj = 'CNPJ'         
        self.dado_variavel = self.dado_rg
        self.opcao_conta = 0
        self.digito_conta = '1'
        self.valor_conta_variavel = None
        self.conta_cadastrada = None
        self.tipo_conta = 'Tipo Conta'
        self.conta_corrente = 'Conta Corrente'
        self.conta_poupanca = 'Conta Poupança'        
        self.conta_variavel = self.conta_corrente 

        self.valor_dado_variavel = None
        self.lista_cliente_json = f'lista_cliente_{self.valor_dado_variavel}.json'        
        self.lista_cliente = []     
        self.lista_transferencia_json = 'lista_transferencia.json'
        self.lista_transferencia = [] 
        self.lista_temporaria = [] 
        self.lista_historico = [self.valor_agencia]
        self.historico = 'Histórico'
        self.conta_transferir = False
        self.agencia_transferir = None
        self.senha = 'Senha'
        self.opcao = None  

        self.nome_conta = 'Conta'
        self.classe_nome = Contas.__name__
        self.valor_saldo = 0
        self.saldo = 'Saldo'
        self.valor_debito = 0
        self.debito = 'Débito'
        self.valor_credito = 0 
        self.credito = 'Crédito'
        self.valor_extrato = []
        self.extrato = 'Extrato'
        self.nome_conta_cliente = 'Conta Cliente'
        # self.mes_extrato = None
        
        self.modulo_menu_contas = 'modulo_menu_contas'
        self.modulo_lista_contas = 'modulo_lista_contas'

        self.self_contas = self
    
    def menu_self(self, lista_self):   # _3.1.2
        self_contas = self.self_contas 
        lista_self.update({'self_contas': self_contas})

        from modulo_pessoa.modulo_pessoa import Pessoa
        Pessoa(self.__dict__).menu_self(lista_self)
        
    # def menu_opcao(self, agencia, lista_self):   # _3.1.3

    #     from modulo_contas.modulo_menu_contas import Menu
    #     Menu.menu_opcao(self, agencia, lista_self)
    