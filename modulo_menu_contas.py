class Menu:
        
    def menu_opcao(self, lista_menu_contas):
        classe_nome = lista_menu_contas['classe_nome']
        classe_funcao = lista_menu_contas['classe_funcao']
        tipo_variavel_1 = lista_menu_contas['tipo_variavel_1']
        tipo_variavel_2 = lista_menu_contas['tipo_variavel_2']

        while True:

            print(f'\n{classe_nome.upper()}\n')

            opcao = input('Listar (1) / Cadastrar (2) / Retornar ocorrências (3)\n'
                            f'Transferir (4) / Descadastrar (5)\nPessoa (6):\n')
            if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6':
                print('Digite uma opção válida.')
                continue  

            if opcao == '1':
                opcao = 'listar'
            elif opcao == '2':
                opcao = 'cadastrar'
            elif opcao == '3':
                opcao = 'ocorrencias'
                return classe_funcao(self, opcao, tipo_variavel_1)
            elif opcao == '4':
                opcao = 'transferir'
                return classe_funcao(self, opcao, tipo_variavel_1)
            elif opcao == '5':
                opcao = 'descadastrar'
            else:
                from modulo_pessoa import Pessoa
                Pessoa().opcao_menu()

            valor_variavel = input(f'\n{tipo_variavel_1} (1) / {tipo_variavel_2} (2)\\nPessoa (3):\n')
            if valor_variavel != '1' and valor_variavel != '2' and valor_variavel != '3':
                    print('\nDigite uma opção válida.')
                    continue
            if valor_variavel == '1':
                valor_variavel = tipo_variavel_1
                return classe_funcao(self, opcao, valor_variavel)
            elif valor_variavel == '2':
                valor_variavel = tipo_variavel_2 
                return classe_funcao(self, opcao, valor_variavel)
            else:
                from modulo_pessoa import Pessoa
                Pessoa().opcao_menu()
   
    def menu_acao(self, lista_menu_contas, opcao, valor_variavel, dado, dado_2, dado_3, 
                  valor_dado=None, valor_dado_2=None, valor_dado_3=None):
        classe = lista_menu_contas['classe']
        self.opcao = opcao
        self.dado = dado
        self.dado_2 = dado_2
        self.dado_3 = dado_3
        self.valor_dado = valor_dado
        self.valor_dado_2 = valor_dado_2
        self.valor_dado_3 = valor_dado_3
        self.valor_variavel = valor_variavel
        self.tipo_variavel_1 = lista_menu_contas['tipo_variavel_1']
        self.tipo_variavel_2 = lista_menu_contas['tipo_variavel_2']
        self.n = 0; self.e = 0; self.f = True; self.t = True
        
        while True:            
            
            print('\nMenu (1)')
            if opcao == 'listar':
                
                if dado_3 is True: 
                      
                    self.valor_dado_2 = input(f'\nDigite o {dado_2}:\n') 
                    if self.valor_dado_2 == '1':
                        from modulo_agencia import Agencia
                        return Agencia().contas_opcao()
                    self.valor_dado = input(f'\nDigite o {dado}:\n')
                else:                              
                    dado_valor = input(f'\n{dado_2} (1) {dado_3} (2):\n')
                    if dado_valor != '1' and dado_valor != '2':
                        print('\nDigite uma opção válida.\n')
                        continue 
                    if dado_valor == '1':
                        self.valor_dado_2 = input(f'\nDigite o {dado_2}:\n')
                    elif dado_valor == '2':
                        self.valor_dado_3 = input(f'\nDigite o {dado_3}:\n') 

                    if self.valor_dado_2 == '1' or  self.valor_dado_3 == '1':
                        from modulo_agencia import Agencia
                        return Agencia().contas_opcao()

                    self.valor_dado = input(f'\nDigite_ o {dado}:\n')
                    # if self.valor_dado_2.isnumeric():
                        #     self.valor_dado_2 = int(self.valor_dado_2)    # int forçado
                        #     if self.valor_dado_2 == 1:
                        #         return self.classe_nome()
            elif opcao == 'cadastrar':  
                
                if dado_3 is True:
                    self.valor_dado_2 = input(f'\nDigite o {dado_2}:\n')

                    if self.valor_dado_2 == '1':
                        from modulo_agencia import Agencia
                        return Agencia().contas_opcao()
                    
                    self.valor_dado = input(f'\nDigite o {dado}:\n')
                    
                elif dado_3 is not True and dado_3 is not False:
                    dado_valor = input(f'\n{dado_2} (1) {dado_3} (2):\n')
                    if dado_valor != '1' and dado_valor != '2':
                        print('\nDigite uma opção válida.\n')
                        continue 
                    if dado_valor == '1':
                        self.valor_dado_2 = input(f'\nDigite o {dado_2}:\n')
                    elif dado_valor == '2':
                        self.valor_dado_3 = input(f'\nDigite o {dado_3}:\n') 

                    if self.valor_dado_2 == '1' or  self.valor_dado_3 == '1':
                        from modulo_agencia import Agencia
                        return Agencia().contas_opcao()
                    
                    self.valor_dado = input(f'\nDigite o {dado}:\n')                    

            elif opcao == 'ocorrencias' or opcao == 'transferir':                 
                dado_valor = input(f'\n{dado_2} (1) {dado_3} (2):\n')
                if dado_valor != '1' and dado_valor != '2':
                    print('\nDigite uma opção válida.\n')
                    continue
                if dado_valor == '1':
                    self.valor_dado = input(f'\nDigite o {dado_2}:\n')
                    self.dado = dado_2
                elif dado_valor == '2':
                    self.valor_dado = input(f'\nDigite o {dado_3}:\n')
                    self.dado = dado_3
                    self.valor_dado_3 = True
            
            elif opcao == 'descadastrar':                
                self.valor_dado = input(f'\nDigite o {dado}:\n')
                if self.valor_dado[0] == '2':
                    self.valor_dado_3 = True
                
            if  self.valor_variavel == self.tipo_variavel_1:
                if self.valor_dado[0] == '1' and self.valor_dado[-1] == '2':
                    print(f'\n{self.valor_dado} não é um número de {self.valor_variavel}.')
                    print(f'Por favor, digite um número de {self.valor_variavel} válido.')
                    self.valor_dado = '1' 
                elif self.valor_dado[0] == '2' and self.valor_dado_2 is not None:
                    print(f'\n{self.valor_dado} não é um número de {self.valor_variavel} de Pessoa Física.')
                    print(f'Por favor, digite um número de {self.valor_variavel} de Pessoa Física válido.')
                    self.valor_dado = '1'
            elif self.valor_variavel == self.tipo_variavel_2:
                if self.valor_dado[0] == '2' or self.valor_dado[-1] == '1':
                    print(f'\n{self.valor_dado} não é um número de {self.valor_variavel}.')
                    print(f'Por favor, digite um número de {self.valor_variavel} válido.')
                    self.valor_dado = '1' 

            def teste_valor_dado(self):

                if self.valor_dado == '1' or self.valor_dado_2 == '1' or self.valor_dado_3 == '1':
                    from modulo_agencia import Agencia
                    return Agencia().contas_opcao()  
                
                if self.valor_dado_3 is not None:   # CNPJ
                    self.n = 1
                    self.dado_2 = self.dado_3
                    self.valor_dado_2 = self.valor_dado_3                   
       
                from modulo_lista_contas import Lista
                return Lista(lista_menu_contas, self.__dict__) 

            return teste_valor_dado(self)  
        