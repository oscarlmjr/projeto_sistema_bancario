"""
    Esse módulo inicia os tipos de conta disponíveis na agência: conta corrente
    (pessoa física ou jurídica) e conta poupança (pessoa física)"""

print('3.0_')
class Contas:   # 3.1.0_
    print('3.1.0_')
    def __init__(self, agencia):   # 3.1.1_
        print('3.1.1_')
        self.valor_agencia = agencia['valor_agencia']
        self.lista_boa_vista_bank_json = 'lista_boa_vista_bank.json'
        self.lista_agencia = ['0001']
        self.lista_conta_json = f'lista_conta_{self.valor_agencia}.json'
        self.lista_contas = [[], []]
        # self.lista_pessoa_json = f'lista_pessoa_{self.valor_agencia}.json'
        # self.lista_pessoa = [[], []]
        self.nome_conta = 'Conta'
        self.classe_nome = Contas.__name__
        self.dado_rg = 'RG'
        self.dado_cnpj = 'CNPJ'
        self.dado_variavel = None
        self.valor_dado_variavel = None
        # self.dado_valor = None
        # self.opcao_conta = None
        self.digito_conta = None
        self.valor_conta_variavel = None
        self.conta_cadastrada = None
        self.tipo_conta = 'Tipo Conta'
        self.conta_corrente = 'Conta Corrente'
        self.conta_poupanca = 'Conta Poupança'
        self.conta_variavel = None
        self.tipo_pessoa = 'Tipo Pessoa'
        self.pessoa_fisica = 'Pessoa Física'
        self.pessoa_juridica = 'Pessoa Jurídica'
        self.pessoa_variavel = None
        # self.conta_transferir = None
        self.valor_agencia_transferir = None
        self.senha = 'Senha'
        # self.opcao = None

        self.mes = 'mês'
        self.mes_extrato = None
        self.valor_saldo = 0
        self.saldo = 'Saldo'
        self.valor_debito = 0
        self.debito = 'Débito'
        self.valor_credito = 0 
        self.credito = 'Crédito'
        self.valor_extrato = []
        self.extrato = 'Extrato'
        self.saque = 'Saque'
        self.valor_saque = 0
        self.deposito = 'Depósito'
        self.valor_deposito = 0
        self.historico = 'Histórico'
        # self.lista_historico = [[self.valor_agencia, self.valor_conta_variavel]]

        self.self_contas = self

    def menu_self(self, lista_self, valor_agencia_filial):   # 3.1.2_
        print('3.1.2_')
        self_contas = self.self_contas 
        lista_self.update({'self_contas': self_contas})

        from modulo_pessoa.modulo_pessoa import Pessoa
        Pessoa(self.__dict__).menu_self(lista_self, valor_agencia_filial)
