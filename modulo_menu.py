from modulo_listas import Lista


class Menu:
    def __init__(self): 
        ...
        
    def menu_opcao(self, lista_menu):
        classe_nome = lista_menu['classe_nome']
        classe_funcao = lista_menu['classe_funcao']
        tipo_variavel_1 = lista_menu['tipo_variavel_1']
        tipo_variavel_2 = lista_menu['tipo_variavel_2']

        while True:

            print(f'\n{classe_nome.upper()}\n')

            if classe_nome == 'Pessoa':
                opcao = input('Listar (1) / Cadastrar (2) / Descadastrar (3):\nContas (4):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
                    print('Digite uma opção válida.\n')
                    continue  
                if opcao == '4':
                    opcao = '6'
            else:
                opcao = input('Listar (1) / Cadastrar (2)\nRetornar ocorrências (3) / Descadastrar (4)'
                              f'\nPessoa (5):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                    print('Digite uma opção válida.')
                    continue  
                if opcao == '3':
                    opcao = '4'
                elif opcao == '4':
                    opcao = '3'            

            if opcao == '1':
                opcao = 'listar'
            elif opcao == '2':
                opcao = 'cadastrar'
            elif opcao == '3':
                opcao = 'descadastrar'
            elif opcao == '4':
                opcao = 'ocorrencias'
            elif opcao == '5':
                from modulo_pessoa import Pessoa
                Pessoa()
            else:
                from modulo_contas import Contas
                Contas()

            valor_variavel = input(f'\n{tipo_variavel_1} (1) / {tipo_variavel_2} (2)\n\nContas (3)  /  Pessoa (4):\n')
            if valor_variavel != '1' and valor_variavel != '2' and valor_variavel != '3' and valor_variavel != '4':
                    print('\nDigite uma opção válida.')
                    continue
            if valor_variavel == '1':
                valor_variavel = tipo_variavel_1
                return classe_funcao(self, opcao, valor_variavel)
            elif valor_variavel == '2':
                valor_variavel = tipo_variavel_2 
                return classe_funcao(self, opcao, valor_variavel) 
            elif valor_variavel == '3':
                from modulo_contas import Contas, __init__
                Contas.__init__(self)
            elif valor_variavel == '4':
                from modulo_pessoa import Pessoa, __init__
                Pessoa.__init__(self)
   
    def menu_acao(self, lista_menu, opcao, valor_variavel, tipo_variavel_1, tipo_variavel_2, dado, dado_2, dado_3, 
                  valor_dado=None, valor_dado_2=None, valor_dado_3=None):
        classe = lista_menu['classe']
        self.opcao = opcao
        self.valor_variavel = valor_variavel
        self.tipo_variavel_1 = tipo_variavel_1
        self.tipo_variavel_2 = tipo_variavel_2
        self.dado = dado
        self.dado_2 = dado_2
        self.dado_3 = dado_3
        self.valor_dado = valor_dado
        self.valor_dado_2 = valor_dado_2
        self.valor_dado_3 = valor_dado_3
        
        while True:            
            
            if opcao == 'listar':
                if dado_3 is False:                    
                    self.valor_dado_2 = input(f'\nMenu (1)\nDigite o {dado_2}:\n')
                    if self.valor_dado_2 == '1':
                        return classe()
                    self.valor_dado_3 = dado_3   
                elif dado_3 is True:                    
                    self.valor_dado = input(f'\nMenu (1)\nDigite o {dado}:\n')  
                    if self.valor_dado == '1':
                        return classe()
                    self.valor_dado_2 = input(f'\nMenu (1)\nDigite o {dado_2}:\n')  
                    if self.valor_dado_2 == '1':
                        return classe()
                    self.valor_dado_3 = dado_3  
                else:                   
                    self.valor_dado = input(f'\nMenu (1)\nDigite_ o {dado}:\n')  
                    if self.valor_dado == '1':
                        return classe()
                    
                    dado_valor = input(f'\n{dado_2} (1) {dado_3} (2):\n')
                    if dado_valor != '1' and dado_valor != '2':
                        print('\nDigite uma opção válida.\n')
                        continue 
                    if dado_valor == '1':
                        self.valor_dado_2 = input(f'\nMenu (1)\nDigite o {dado_2}:\n')  
                        if self.valor_dado_2 == '1':
                            return classe()
                        self.valor_dado_3 = dado_3 
                    elif dado_valor == '2':
                        self.valor_dado_3 = input(f'\nMenu (1)\nDigite o {dado_3}:\n')  
                        if self.valor_dado_3 == '1':
                            return classe()
                    
                    if self.valor_dado[0] == '1' and self.valor_variavel == self.tipo_variavel_1 and self.valor_dado[-1] == '2':
                        print(f'\n{self.valor_dado} não é um número de {self.valor_variavel}.')
                        print(f'Por favor, digite um número de {self.valor_variavel} válido.')
                        continue
                    elif self.valor_dado[0] != '2' and self.valor_dado_3 != dado_3:
                        print(f'\n{self.valor_dado} não é um número de {valor_variavel} de Pessoa Jurídica.')
                        print(f'Por favor, digite um número de {valor_variavel} de Pessoa Jurídica válido.')
                        continue

                return Lista(lista_menu).listar_variavel(self.__dict__)                    
                    # if self.valor_dado_2.isnumeric():
                        #     self.valor_dado_2 = int(self.valor_dado_2)    # int forçado
                        #     if self.valor_dado_2 == 1:
                        #         return self.classe_nome()
            elif opcao == 'cadastrar':                
                if dado_3 is False:
                    self.valor_dado = input(f'\nMenu (1)\nDigite o {dado}:\n')  
                    if self.valor_dado == '1':
                        return classe()
                    self.valor_dado_2 = input(f'\nMenu (1)\nDigite o {dado_2}:\n')  
                    if self.valor_dado_2 == '1':
                        return classe()
                    self.valor_dado_3 = dado_3
                elif dado_3 is True:
                    self.valor_dado = input(f'\nMenu (1)\nDigite o {dado}:\n')  
                    if self.valor_dado == '1':
                        return classe()
                    self.valor_dado_2 = input(f'\nMenu (1)\nDigite o {dado_2}:\n')  
                    if self.valor_dado_2 == '1':
                        return classe()
                    self.valor_dado_3 = dado_3
                elif dado_3 is not True and dado_3 is not False:
                    dado_valor = input(f'\n{dado_2} (1) {dado_3} (2):\n')
                    if dado_valor != '1' and dado_valor != '2':
                        print('\nDigite uma opção válida.\n')
                        continue 
                    if dado_valor == '1':
                        self.valor_dado_2 = input(f'\nMenu (1)\nDigite o {dado_2}:\n')  
                        if self.valor_dado_2 == '1':
                            return classe()
                        self.valor_dado_3 = dado_3 
                    elif dado_valor == '2':
                        self.valor_dado_3 = input(f'\nMenu (1)\nDigite o {dado_3}:\n')  
                        if self.valor_dado_3 == '1':
                            return classe()
                    self.valor_dado = input(f'\nMenu (1)\nDigite o {dado}:\n')  
                    if self.valor_dado == '1':
                        return classe()   
                    
                    if self.valor_dado[0] == '1' and self.valor_variavel == self.tipo_variavel_1 and self.valor_dado[-1] == '2':
                        print(f'\n{self.valor_dado} não é um número de {self.valor_variavel}.')
                        print(f'\nPor favor, digite um número de {self.valor_variavel} válido.')
                        continue
                    elif self.valor_dado[0] != '2' and self.valor_dado_3 != dado_3:
                        print(f'\n{self.valor_dado} não é um número de {valor_variavel} de Pessoa Jurídica.')
                        print(f'Por favor, digite um número de {valor_variavel} de Pessoa Jurídica válido.')
                        continue
                return Lista(lista_menu).listar_variavel(self.__dict__) 

            elif opcao == 'descadastrar':                
                if dado_3 is False:                
                    self.valor_dado_2 = input(f'\nMenu (1)\nDigite o {dado_2}:\n')
                    if self.valor_dado_2 == '1':
                        return classe()
                else:
                    self.valor_dado = input(f'\nMenu (1)\nDigite o {dado}:\n')
                    if self.valor_dado == '1':
                        return classe()
                    for n in self.valor_dado:
                        if n == '1':
                            self.valor_dado_2 = True
                            break
                    if self.valor_dado[0] == '1' and self.valor_variavel == self.tipo_variavel_1 and self.valor_dado[-1] != '1':
                            print(f'\n{self.valor_dado} não é um número de {self.valor_variavel}.')
                            print(f'\nPor favor, digite um número de {self.valor_variavel} válido.')
                            continue
                    elif self.valor_dado[0] == '1' and self.valor_variavel == self.tipo_variavel_2 and self.valor_dado[-1] == '1':
                            print(f'\n{self.valor_dado} não é um número de {self.valor_variavel}.')
                            print(f'\nPor favor, digite um número de {self.valor_variavel} válido.')
                            continue
                    elif self.valor_dado[0] != '1' and self.valor_variavel == self.tipo_variavel_2:
                        print(f'\n{self.valor_dado} não é um número de {self.valor_variavel}.')
                        print(f'Por favor, digite um número de {self.valor_variavel} válido.')
                        continue
                return Lista(lista_menu).listar_variavel(self.__dict__)
            
            elif opcao == 'ocorrencias': 
                if dado_3 is True:                    
                    self.valor_dado = input(f'\nMenu (1)\nDigite o {dado_2}:\n')  
                    if self.valor_dado == '1':
                        return classe() 
                    self.dado = dado_2
                elif dado_3 is not True and dado_3 is not False: 
                    dado_valor = input(f'\n{dado_2} (1) {dado_3} (2):\n')
                    if dado_valor != '1' and dado_valor != '2':
                        print('\nDigite uma opção válida.\n')
                        continue 
                    if dado_valor == '1':
                        self.valor_dado = input(f'\nMenu (1)\nDigite o {dado_2}:\n')  
                        if self.valor_dado == '1':
                            return classe()
                        self.dado = dado_2
                        self.valor_dado_2 = True
                    elif dado_valor == '2':
                        self.valor_dado = input(f'\nMenu (1)\nDigite o {dado_3}:\n')  
                        if self.valor_dado == '1':
                            return classe()
                        self.dado = dado_3
                return Lista(lista_menu).listar_variavel(self.__dict__)
