print('5.0_')   # 5.0
class Cliente:   # 5.1.0_
	print('5.1.0_')
	def __init__(self):   # 5.1.1_
		print('5.1.1_')
		self.lista_boa_vista_bank_json = 'lista_boa_vista_bank.json'
		self.lista_contas = [[], []]
		self.nome_agencia = 'Agência'
		self.nome_conta = 'Conta'
		self.nome_cliente = 'Cliente'
		self.classe_nome = Cliente.__name__
		self.dado_rg = 'RG'
		self.dado_cnpj = 'CNPJ'
		self.dado_variavel = None
		self.valor_dado_variavel = None
		self.opcao_conta = 0
		self.digito_conta = None
		self.conta_cadastrada = None
		self.tipo_conta = 'Tipo Conta'
		self.conta_corrente = 'Conta Corrente'
		self.conta_poupanca = 'Conta Poupança'
		self.conta_variavel = None
		self.tipo_pessoa = 'Tipo Pessoa'
		self.pessoa_fisica = 'Pessoa Física'
		self.pessoa_juridica = 'Pessoa Jurídica'
		self.pessoa_variavel = None
		self.senha = 'Senha'
		self.opcao = None

		self.mes = 'mês'
		# self.mes_extrato = None
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

		self.dado_nome = 'Nome'
		self.dado_sexo = 'Sexo'
		self.modulo_cliente = f'modulo_cliente'
		self.modulo_menu_cliente = f'modulo_menu_cliente'

	def cliente_autenticacao(self):   # 5.1.2_
		print('5.1.2_')

		from modulo_menu_cliente import Menu
		Menu.menu_autenticacao(self)


Cliente().cliente_autenticacao()
