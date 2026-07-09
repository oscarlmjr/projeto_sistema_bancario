import json
# lista = ['a', 'b', 'c']

numero = '745'

numero = numero.zfill(4)

print(numero)

# if 'd' not in lista:
# # if 'd' is not lista:
#		 print('d')
# else:
#		 print('_')

# if 'a' in lista:
#		 print('a')
# opcao = 0
# indice = 0
# dado_valor = '1234'
# dado = 'rg'

# lista = [[{'1234': {'rg': '1234'}},{}],[]]

# print(lista[opcao][indice][dado_valor].get(dado))

# print(*lista[opcao][indice].keys())

# print(f'{bool([])=}')
# print(f'{bool([[], []])=}')

print()

# lista = [[[], []], []]
# lista = [[], []]
# print(f'1{bool(lista)}')
# print()

# lista = []
# print(f'2{bool(lista)}')
# print()

# # lista = [[]]
# # print(f'3{bool(lista)}')

# # for n, i in enumerate(lista):
# for n in lista:
#		 # print(bool(n))
#		 print(bool(n))
#		 # print(n, i, bool(i), type(i))

# print(bool(n))
# print(f'{i=}')

# # lista_pessoa = {'Senha1': '3898', 'Senha2': '5128', 'Histórico': [['0001', '3898'], ['0002', '5128'], [None]]}
# lista_pessoa = [{'a': '3', '3': {'Senha3': '5160'}}, {'a': '1', 'a1': {'Senha1': '3898'}}, {'a': '2', '2': {'Senha2': '5128'}}, ]
# # lista_pessoa = [[{'11111': {'Senha1': '3898', 'Senha2': '5128', 'Histórico': [['0001', '3898'], ['0002', '5128'], [None]]}}, {}], []]
# d = False
# for i, p in enumerate(lista_pessoa):
# 		# print(i, p)
# 		# print(type(i))
# 		print()
# 		for c, v in p.items():
# 				# print(c, v)
# 				print()
# 				if c == '2':
# 						# print(f'2 = {c, v}')
# 						d = True
# 						break
# 		if d == True:
# 				break

# print(lista_pessoa)
# p.get('2', ).update({'Senha2': '7288'})
# lista_pessoa.sort(key=lambda item: item['a'])
# print()
# print(p)
# print()
# print(lista_pessoa)

# print(p[i])
# print(lista_pessoa[0][0]['11111'])

# with open('lista_pessoa.json', 'w+', encoding='utf8') as arquivo:
#		 json.dump(lista_pessoa, arquivo, ensure_ascii=False, indent=2)


# with open('lista_pessoa.json', 'r+', encoding='utf8') as arquivo:
#		 lista_pessoa = json.load(arquivo)


# if lista_pessoa['Histórico'][-1][0] == None:
# if lista_pessoa['Histórico'][-1][0] == '0002':
		# print(lista_pessoa['Histórico'][-1][0])
		# print(lista_pessoa['Histórico'])

# for dados in lista_pessoa.get('Histórico', ):
#		 if dados == '0002':
				# print(dados)
		# for senha in dados:
		#		 print(senha)


# lista_pessoa = {'Senha': '3898', 'Conta Corrente': '11111', 'Agência': '0002', 'Tipo Conta': 'Conta Corrente', 'Saldo': 
#		 0, 'Débito': 0, 'Crédito': 0, 'Extrato': [], 'Histórico': ['0001', '0002'], 'RG': '1234', 'Nome': 'Oscar', 
#		 'Sexo': 'm', 'Tipo Pessoa': 'Pessoa Física'}

# print('')
# print(lista_pessoa)

# print(*lista_pessoa.items())

# if 'RG' in lista_pessoa:
#		 print(f'RG = {}')

# print(*lista_pessoa.keys())

# opcao_conta = 0
# opcao_pessoa = opcao_conta

# for indice_pessoa, dados_pessoa in enumerate(f'lista_pessoa_001.json'[opcao_pessoa]):
#		 for valor_dado_variavel, dados in dados_pessoa.items():
#		 if valor_dado_variavel == valor_dado_variavel:
#				 lista_pessoa[opcao_pessoa].append(dados_pessoa)
#				 break

# print(f'\nself.lista_pessoa = {lista_pessoa[opcao_pessoa][indice_pessoa]}\n')