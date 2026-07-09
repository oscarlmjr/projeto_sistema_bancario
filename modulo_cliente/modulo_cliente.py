print('5.1.0_')
class Cliente:   # 5.1.1.0_
    print('5.1.1.0_')
    def __init__(self):   # 5.1.1.1_
        print('5.1.1.1_')
        self.classe_nome = Cliente.__name__
        self.lista_cliente = []
        self.lista_boa_vista_bank_json = 'lista_boa_vista_bank.json'
        self.dado_agencia = 'Agência'
        self.lista_contas = [[], []]
        self.valor_conta = None
        self.dado_conta = 'Conta'
        self.valor_matricula = None
        self.matricula = 'Matrícula'
        self.valor_senha = None
        self.senha = 'Senha'
        self.dado_rg = 'RG'
        self.dado_cnpj = 'CNPJ'
        self.dado_variavel = self.dado_rg
        self.dado_nome = 'Nome'
        self.dado_sexo = 'Sexo'
        self.opcao = 'cadastrar'
        self.opcao_conta = 0 
        self.indice_conta = 0
        self.valor_saldo = 0
        self.saldo = 'Saldo'
        self.valor_extrato = []
        self.extrato = 'Extrato'
        self.saque = 'Saque'
        self.valor_saque = 0
        self.deposito = 'Depósito'
        self.valor_deposito = 0
        self.valor_debito = 0
        self.debito = 'Débito'
        self.valor_credito = 0 
        self.credito = 'Crédito' 
        self.mes_extrato = None
        self.tipo_conta = 'Tipo Conta'
        self.conta_corrente = 'Conta Corrente'
        self.conta_poupanca = 'Conta Poupança'

        self.modulo_menu_cliente = 'modulo_menu_cliente'
        self.modulo_lista_cliente = 'modulo_lista_cliente'

    def cliente_autenticacao(self):   # 5.1.1.2_
        print('5.1.1.2_')
        from modulo_menu_cliente import Menu
        Menu.menu_autenticacao(self)

Cliente().cliente_autenticacao()
