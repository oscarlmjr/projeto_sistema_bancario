import json, copy


class Lista:   # 3.3.0_
	print('3.3.0_')
	def listar_contas(self, agencia, lista_self):   # 3.3.1_
		print('3.3.1_')
		conta_cadastrada = False
		transferencia = False
		inativar = False
		ocorrencias = False

		try:
			with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
				self.lista_contas = json.load(arquivo)
		except:
			...

		while True:

			for indice_conta, dados_conta in enumerate(self.lista_contas[self.opcao_conta]):
				for valor_conta_variavel, dados in dados_conta.items():

					if valor_conta_variavel == self.valor_conta_variavel:
						if dados.get(self.historico, )[-1][0] == None:
							conta_cadastrada = None
							transferencia = None
							inativar = None
							break
						if dados.get(self.historico, )[-1][0] != self.valor_agencia:
							print(f'\n_{self.conta_variavel} {self.valor_conta_variavel} transferida para agência {dados.get(self.historico, )[-1][0]}.')

							from modulo_contas.modulo_menu_contas import Menu
							Menu.menu_opcao(self, agencia, lista_self)

						if self.opcao == 'listar':
							conta_cadastrada = True
							self.indice_conta = indice_conta
							self.dados_contas = dados

						elif self.opcao == 'transferir':
							transferencia = True
							print(f'\nv_ = {dados}')
							print(f'{self.valor_agencia=}')
							dados.get(self.historico, ).append([self.valor_agencia_transferir, self.valor_conta_transferir])
							dados_transferir = copy.deepcopy(dados)
							dados_transferir[self.conta_variavel] = self.valor_conta_transferir
							dados_transferir.update(Agência=self.valor_agencia_transferir)

							self.conta_transferir = {self.valor_conta_transferir: dados_transferir}
							self.valor_dado_variavel = dados.get(self.dado_variavel, )

							with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
								json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)

							from modulo_contas.modulo_lista_contas import Lista
							Lista.transferir_conta(self, agencia, lista_self)

						elif self.opcao == 'inativar':
							inativar = True
							dados.get(self.historico, ).append([None])
							break

					elif dados.get(self.dado_variavel, ) == self.valor_dado_variavel:
						ocorrencias = True
						if self.opcao == 'ocorrencias':
							print(f'\nv = {dados}')

					if transferencia is  not False or inativar is not False or conta_cadastrada is not False:
						break
				if transferencia is  not False or inativar is not False or conta_cadastrada is not False:
					break
			if transferencia is  not False or inativar is not False or conta_cadastrada is not False:
				break
			break

		with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
			json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)

		if self.opcao == 'listar':

			if conta_cadastrada is True:
				print(f'\ncliente_ {self.nome_conta} {self.valor_conta_variavel} possui cadastro.')
				print(self.lista_contas[self.opcao_conta][self.indice_conta][self.valor_conta_variavel], '\n')

				from modulo_cliente.modulo_menu_cliente import Menu
				Menu.menu_opcao(self)

			elif conta_cadastrada is False:
				print(f'\ncliente_2 {self.nome_conta} {self.valor_conta_variavel} não possui cadastro')

			elif conta_cadastrada is None:
				print(f'_\n{self.conta_variavel} {self.valor_conta_variavel} está inativa.')
				print(f'\nINATIVA ##### INATIVA ##### INATIVA\n\n{dados}\n\nINATIVA ##### \
						INATIVA ##### INATIVA\n')

		elif self.opcao == 'ocorrencias':
			if ocorrencias is True:
				print(f'\nTodas as ocorrências encontradas para {self.dado_variavel} {self.valor_dado_variavel}.')
			else:
				print(f'\n{self.dado_variavel} {self.valor_dado_variavel} não possui ocorrência.')

		elif self.opcao == 'transferir':

			if transferencia is False:
				print(f'\n{self.conta_variavel} {self.valor_conta_variavel} não possui ocorrência.')

			else:
				print(f'\n{self.conta_variavel} {self.valor_conta_variavel} está inativa.')

		elif self.opcao == 'inativar':
			if inativar is True:
				print(f'\n_{self.conta_variavel} {self.valor_conta_variavel} está sendo inativada.')
				print(f'\nINATIVA ##### INATIVA ##### INATIVA\n\n{dados}\n\nINATIVA ##### INATIVA ##### INATIVA\n')

			elif inativar is False:
				print(f'\n_{self.conta_variavel} {self.valor_conta_variavel} não está cadastrada.')

			elif inativar is None:
				print(f'\n{self.conta_variavel} {self.valor_conta_variavel} está inativa.')

		from modulo_contas.modulo_menu_contas import Menu
		Menu.menu_opcao(self, agencia, lista_self)

	def cadastrar_conta(self, agencia, lista_self, lista):   # 3.3.2_
		print('3.3.2_')
		valor_agencia = agencia['valor_agencia']
		classe_nome = agencia['classe_nome']

		import secrets

		valor_senha = str(secrets.randbelow(1000))
		self.valor_senha = valor_senha.zfill(4)

		lista_cadastrar = {self.senha: self.valor_senha, self.conta_variavel: self.valor_conta_variavel,
						   classe_nome: valor_agencia, self.tipo_conta: self.conta_variavel,
						   self.saldo: self.valor_saldo, self.debito: self.valor_debito, self.credito: self.valor_credito,
						   self.extrato: self.valor_extrato, self.historico: [[self.valor_agencia, self.valor_conta_variavel]]}

		for chave, valor in lista.items():
			lista_cadastrar[chave] = valor

		lista_cadastrar = {self.valor_conta_variavel: lista_cadastrar}

		self.lista_contas[self.opcao_conta].append(lista_cadastrar)

		with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
			json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)

			print(f'{self.conta_variavel} {self.valor_conta_variavel}_ cadastrado com sucesso_.\n')
			print(f'{self.lista_contas[self.opcao_conta][-1][self.valor_conta_variavel]}\n')

		from modulo_contas.modulo_menu_contas import Menu
		Menu.menu_opcao(self, agencia, lista_self)

	def transferir_conta(self, agencia, lista_self):   # 3.3.3_
		print('3.3.3_')
		print('Transferindo')

		self.lista_conta_json = f'lista_conta_{self.valor_agencia_transferir}.json'

		try:
			with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
				self.lista_contas = json.load(arquivo)
		except:
			with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
				json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)

		self.lista_contas[self.opcao_conta].append(self.conta_transferir)

		print(f'\nlista_conta_{self.valor_agencia_transferir}:\n{self.lista_contas[self.opcao_conta][-1]}\n')

		with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
			json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)

		self.lista_conta_json = f'lista_conta_{self.valor_agencia}.json'

		pessoa_transferir = True
		self_pessoa = lista_self.get('self_pessoa')

		from modulo_pessoa.modulo_lista_pessoa import Lista
		Lista.listar_variavel(self_pessoa, agencia, self.__dict__, lista_self, None, pessoa_transferir)
