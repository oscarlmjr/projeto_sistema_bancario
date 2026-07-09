# a = '12121'
# # a = '21111'

# # print(f'a[-2] = {a[-2]}')    

# if a[-1] == '1':
#       print(f'a[-1] = {a[-1]}')    
    

# for n in a:
#     if n == '1':
#         print(f'n = {n}')
#         break
#     print(f'n_ = {n}')    

##################


a = [[{'11111': {'RG': '1234', 'Nome': 'Oscar', 'conta': '11111', 'Tipo Pessoa': 'Pessoa Física'}}, 
      {'11121': {'RG': '2345', 'Nome': 'Gabriel', 'conta': '11121', 'Tipo Pessoa': 'Pessoa Física'}}], 
      [{'21111': {'CNPJ': '12345', 'Nome': 'BV Code', 'conta': '21111', 'Tipo Pessoa': 'Pessoa Jurídica'}}]]

# print(a[0][-1][2345])
n = 0
dado = 'RG'
dado_2 = '2345'

# while True:
for e, p in enumerate(a[n]):
      print(f'e, p = {e, p}\n')

for c, v in p.items():
      print(f'c, v = {c, v}\n')

      if v.get(dado, ) == dado_2:
            # print(f'p = {p[c]}\n')
            print(f'v = {v}\n')
            # print(f'p = {p[c][dado]}\n')
            break


##################

# dado_busca_2 = 'dado_busca_2'
# valor_dado_2 = True
# dado_busca = None

# while True:
#     if dado_busca == dado_busca_2:    
#         print(dado_busca)
#         break
#     if dado_busca_2 is not None:
#         if valor_dado_2 is True:
#             print('valor_dado_2')
#             dado_busca = dado_busca_2
#             continue
#         dado_busca = dado_busca_2
#         print('dado_busca')
    
#     break

##################

# valor_dado = '212345'

# for n in valor_dado:
#     if n == '2':
#         valor_dado_2 = True
#         break
# #     else:
#     print('valor_dado_2')
#     valor_dado_2 = False
#     break
# print(valor_dado_2)

##################

# a = '12345'

# if '1' in a:
#     print(True)

##################


# a = ()
# a = (2,)

# print(a, type(a))
# print(a == None)
# print(a == True)
# print(a == False)
# print(len(a))
# print('')
# print('' == None)
# print('' != None)
# print(len(''))

##################

# print(enumerate(range(4, 10)))

# for _ in range(4, 10):
#     print(_)

# for _ in enumerate(range(4, 10)):
#     print(_)

##################


# lista_pessoas = [[{'1234': {'RG': '1234', 'Nome': 'Oscar', 'Tipo Pessoa': 'Pessoa Física', 
#                   'Número da Conta': '11111', 'Tipo Conta': 'Conta Corrente'}}], []]
# lista = [[], []]

# numero = "numero"
# numero_conta = 'Número da Conta'
# n = 0
# e = 0


# for chave, valor in lista_pessoas[0][0].items():
#     # print(chave, valor)
#         lista[n].append({lista_pessoas[n][e][chave].get(numero_conta, ): lista_pessoas[n][e][chave]})

# print(lista_pessoas)



# lista_2 = {"nome": lista["nome"], "numero": lista["numero"], "tipo_conta": lista["tipo_conta"]}

# print(lista_2)


##################

# a = {1: '1'}

# print(a)
# print(*a.keys(), type(*a.keys()))


##################

# class T():
    
#     def __init__(self, lista_r): 
#         self.lista_r = lista_r
#         print(f'\nT.__init__()')
#         print(f'self.lista_r {self.lista_r}\n')

#         # def n():            
#         #     def interna(lista_r):
#         #         self.lista_r = lista_r   
#         #         print(f'def interna()')
#         #         print(f'self.lista_r = {self.lista_r}\n')

#         #     return interna

#         # b = n()
#         # b(lista_r)        
#         T.a(self)        
#         T.b(self)        
        
#     def a(self):
#         self.param3 = 'param3'
#         self.param4 = 'param4'
#         print(f'def a()')
#         print(f'self.lista_r = {self.lista_r}\n')

#     def b(self):
#         self.param5 = 'param5'
#         self.param6 = 'param6'     
#         lista_b = self.__dict__
#         print(f'def b()')
#         print(f'lista_b = {lista_b}\n')
#         print(f'self.lista_r = {self.lista_r}\n')
        

# class R:
#     def __init__(self):      
#         print(f'R.__init__()')

#     def c(self):        
#         self.param = 'param'
#         self.param2 = 'param2'
#         self.paramn = R    
#         lista_r = self.__dict__
#         print(f'def c()')
#         print(f'lista_r = {lista_r}\n')
#         T(lista_r)

# R().c()


#######################


# def a():
#     print(f'def a()\n')

#     def interna(n, c):
#         print(f'n, c = {n, c}\n')

#     return interna

# b = a()
# b('n', 'c')


##########################


# class T():
    
#     def __init__(self, lista_r): 
#         nome_lista_r = lista_r
#         print(f'\nT.__init__()')
#         print(f'lista_r {lista_r}\n')

#         # def n():
#         #     def interna(lista_r):
#         #         print(f'def interna()')
#         #         self.lista_r = lista_r   
#         #         print(f'self.lista_r = {self.lista_r}\n')

#         #     return interna

#         # b = n()
#         # b(lista_r)
#         T.a(self, nome_lista_r)
        
#     def a(self, nome_lista_r):
#     # def a(self):
#         self.param3 = 'param3'
#         self.param4 = 'param4'
#         lista_t = self.__dict__
#         print(f'def a()')
#         # b(nome_lista_r)
#         print(f'nome_lista_r = {nome_lista_r}\n')
#         print(f'lista_t = {lista_t}\n')
#         T.b(self)

#     def b(self):        
#         self.param5 = 'param5'
#         self.param6 = 'param6'
#         lista_b = self.__dict__
#         print(f'def b()')
#         print(f'lista_b = {lista_b}\n')
        

# class R:
#     def __init__(self):      
#         print(f'R.__init__()')

#     def c(self):        
#         self.param = 'param'
#         self.param2 = 'param2'
#         self.paramn = R    
#         lista_r = self.__dict__
#         print(f'def b()\n')
#         print(f'lista_r = {lista_r}\n')
#         T(lista_r)

# R().c()


        # lista_a = self.__dict__
        # print(f'\n{lista_a}\n')
        # print(f'{self.__dict__}\n')        
        # T.b(self, self.lista_t)
        # T.b(self, T.__dict__)
        # T.b(self, self.__dict__)
        # T.b(self, T.__init__.__dict__)
        # T.b(self, self.__init__.__dict__)
        # lista_t = T.__dict__
        # lista_t = self.__dict__
        # lista__init = self.__init__.__dict__
        # lista_t__init = T.__init__.__dict__
        # print(f'a() variavel {param}')
        # print(f'lista_t = T.__dict__ {lista_t}')
        # print(f'lista_t = self.__dict__ {lista_t}')
        # print(f'lista__init = self.__init__.__dict__ {lista__init}')
        # print(f'lista__init = T.__init__.__dict__ {lista_t__init}')
        # print(f'lista = self.__dict__ {lista}')


#######################


# class T():
#     # def __init__(self, param=None, param2=None):
#     def __init__(self):
#         # self.param = param
#         # self.param2 = param2
#         # print(self.param, self.param2)
#         # print(self.param.__name__)
#         # variavel = input(f'digite {self.param} (1), {self.param2} (2)\n')
#         variavel = input(f'digite 1\n')
#         if variavel == '1':
#             # t('qualquer', 'coisa')
#             print(f'variavel = {variavel}')
#             print()
#             T.a(self, T)
#             # T()
#             # T().a
#             # T.a
#             # T
#             # T.__init__
#             print('fim do if')
#         else:
#             variavel = self.param2

#     def a(self, param):
#         self.param = param
        
#         print(f'a() variavel {param}')
#         return self.param()


# T()


########################

# class Lista:
#     def __init__(self, lista, classe_nome, funcao_listar):
#         self.lista = lista
#         self.classe_nome = classe_nome
#         self.funcao_listar = funcao_listar

#     def listar_variavel(self):
#         self.classe_nome = Lista.__name__
#         self.funcao_listar = Lista.listar_variavel.__name__

#         print(Lista.__name__, type(Lista))
#         print()
#         print(self.classe_nome)
#         print()
#         print(Lista.listar_variavel.__name__, type(Lista.listar_variavel))
#         print()
#         print(self.funcao_listar)
#         print()
#         print(self.lista)
#         print()
#         print(self.lista['tipo_pessoa'])
#         # print(lista)
        

# class PessoaFisica:
#     def __init__(self, nome, rg, acao, tipo_pessoa='Pessoa Física'):
#         self.nome = nome
#         self.rg = rg
#         self.acao = acao
#         self.tipo_pessoa = tipo_pessoa        
#         # lista = self.__dict__
#         Lista(self.__dict__, None, None).listar_variavel()  
#         # Lista.listar_variavel(self, lista)

# nome = 'Oscar'
# rg = '1234'
# acao = 'cadastrar'

# PessoaFisica(nome, rg, acao)


#####################

# lista_pessoas = [[{"Oscar": {"nome": "Oscar", 
# "idade": 45, "tipo_pessoa": "Pessoa Física"}}, {"Gabriel": {"nome": "Gabriel", 
# "idade": 15, "tipo_pessoa": "Pessoa Física"}}], 
# [{"BV Code": {"nome": "BV Code", 
# "cnpj": 123123, "tipo_pessoa": "Pessoa Jurídica"}}]]

# # # lista_contas = [[{"12345": {"numero": "12345", "tipo_conta": "Conta Corrente"}}, 
# # #                  {"67890": {"numero": "67890", "tipo_conta": "Conta Corrente"}}], 
# # #                  [{"11220": {"numero": "11220", "tipo_conta": "Conta Corrente"}}]]

# # # lista = {"Oscar": {"nome": "Oscar", "numero": "12345", "tipo_conta": "Conta Corrente"}}
# lista = {"12345": {"numero": "12345", "tipo_conta": "Conta Corrente"}}
# # # # numero = "12345"

# # # lista_pessoas[0][0].setdefault(keys(), )

# # # print(lista_pessoas[0][0])
# # # print()
# # # print(lista_pessoas[0])
# # print()
# numero = "numero"
# n = 0
# e = 0


# for chave, valor in lista_pessoas[0][0].items():
#     # print(chave, valor)
#     print()
#     print(lista_pessoas[0][0][chave].get('idade', ))
# print()

# lista_contas[n][e] = {lista_contas[n][e][numero].get('numero', 'numero'): lista_contas[n][e][numero]}
# # print(lista_contas)


# # print(*lista_pessoas[0][0].keys())
# # print()
# # print(*lista_pessoas[0][0].values())
# print()
# # print({lista_pessoas[0][0] : lista_pessoas[0][0].values()})
# print()


# a = lista_pessoas[0][0].keys()
# print(lista_pessoas[0][0][a])
# a = [_ for _ in lista_pessoas[0][0].keys()]
# print(a)
# print()
# print(*a)
# # a = lista_pessoas[0][0].keys()
# # print(*a)
# # print()
# # a = lista_pessoas[0][0].values()
# # print(*a)
# # print()
# # print(lista_pessoas[0][0]['Oscar'])
# # print()
# print(*lista_pessoas[0][0].keys())
# print()
# print(lista_pessoas[0][0][[_ for _ in a]])
# print()
# print(*[_ for _ in lista_pessoas[0][0].keys()], type(*[_ for _ in lista_pessoas[0][0].keys()]))
# print()
# print([_ for _ in lista_pessoas[0][0].keys()], type([_ for _ in lista_pessoas[0][0].keys()]))
# print()
# print(lista_pessoas[0][0][*[_ for _ in lista_pessoas[0][0].keys()]])
# print([n for n in range(5)])
# print()
# print(*lista_pessoas[0][0]['Oscar'])
# print()
# print(lista_pessoas[0][0]['Oscar'])
# print()
# print()
# # lista = lista_pessoas[0][0]['Oscar'].get('nome', )
# # print({lista_pessoas[0][0]['Oscar'].get('tipo_pessoa', ) : lista_pessoas[0][0]['Oscar']})
# lista = {lista_pessoas[0][0]['Oscar'].get('tipo_pessoa', ) : lista_pessoas[0][0]['Oscar']}
# print(lista)
# lista = {lista_pessoas[0][0]['Oscar'].get('Oscar').get('tipo_pessoa') : lista_pessoas[0][0]['Oscar'].get('Oscar')}
# print(lista)


#####################

# print(lista.get("12345", lista[0].get("tipo_conta", ) : lista.get("numero", )))
# print(lista.get("12345", "12345"))
# print()
# lista = {lista.get('nome', 'nome'): lista}
# print(lista)
# print()
# print(lista.get("12345", ))
# print(lista.get("12345").get("tipo_conta", ))
# print(lista.get("1234", 'Não encontrado'))

# lista = {lista.get("12345").get("tipo_conta", ): lista.get("12345")}
# print(lista)

# lista_contas = [[{"12345": {"numero": "12345", "tipo_conta": "Conta Corrente"}}, 
#                  {"67890": {"numero": "67890", "tipo_conta": "Conta Corrente"}}], 
#                  [{"11220": {"numero": "11220", "tipo_conta": "Conta Corrente"}}]]

# n = 0; e = 0; f = True            
# while True:
#     for e, l in enumerate(lista_contas[n]):
#         for c, v in l.items():
#             if c == '13561131':
#                 print(f'\n{v}')
#                 f = False
#                 break                 
#                 # print(l.get(numero, numero))
#         if f == False:
#             break 
#     if f is True and n + 1 < len(lista_contas):
#         n += 1  
#     else:
#         break

# print(f'\nn, e = {n, e}\n')
# print(f'\nlista_contas[n][e] = {lista_contas[n][e]}\n')
# print()

# lista_contas[n][e] = {lista_contas[n][e][numero].get('numero', 'numero'): lista_contas[n][e][numero]}
# print(lista_contas)

# if lista['tipo_conta'] == 'Conta Corrente':
#     lista_contas[0].append({lista.get('numero', 'numero'): lista})
# else:
#     lista_contas[1].append({lista.get('numero', 'numero'): lista})


#####################

# c = 0; l = 0
# while True:
#     for dados in lista_pessoas[l]:
#         if dados.get(nome) is None:
#             c += 1
#         else:
#             dados.get(nome, lista_contas[l][c][nome].update(lista))
#             break
#     l += 1        
#     c = 0
#     if l == len(lista_pessoas):
#         break

# lista_contas[0][0] = {lista_contas[0][0][nome].get('numero', 'numero'): lista_contas[0][0][nome]}
# print(lista_contas)
# print()            
                
# if lista['tipo_pessoa'] == 'Pessoa Física':
#     lista_pessoas[0].append({lista.get('nome', 'nome'): lista})
# else:
#     lista_pessoas[1].append({lista.get('nome', 'nome'): lista})
# print(lista_pessoas)


#####################

# print(lista)
# # print()
# # print(lista[0][0])
# print()

# for e, l in enumerate(lista[0]):
#     print(e, l)
#     print()

# c, v, i = lista.items()

# print(c, v, i)

# del lista[0][0]

# print(lista)
# print(lista.get('casa', ))

# if lista.get('casa', ) is None:
#     print('Não existe')
# print()

# for l, e in enumerate(lista):
#     print(l, e)
#     print()
