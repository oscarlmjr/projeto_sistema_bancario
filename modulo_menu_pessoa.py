from modulo_lista_pessoa import Lista


class Menu:
        
    def menu_opcao(self, lista_menu_pessoa):
        classe_nome = lista_menu_pessoa['classe_nome']
        classe_listar = lista_menu_pessoa['classe_listar']
        tipo_variavel_1 = lista_menu_pessoa['tipo_variavel_1']
        tipo_variavel_2 = lista_menu_pessoa['tipo_variavel_2']

        while True:

            print(f'\n{classe_nome.upper()}\n')
            
            opcao = input('Listar (1) / Cadastrar (2) / Descadastrar (3):\nContas (4):\n')
            if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
                print('Digite uma opção válida.\n')
                continue  
            
            if opcao == '1':
                opcao = 'listar'
            elif opcao == '2':
                opcao = 'cadastrar'
            elif opcao == '3':
                opcao = 'descadastrar'
            else:
                from modulo_agencia import Agencia
                Agencia().contas_opcao()

            valor_variavel = input(f'\n{tipo_variavel_1} (1) / {tipo_variavel_2} (2)\n\nContas (3):\n')
            if valor_variavel != '1' and valor_variavel != '2' and valor_variavel != '3':
                    print('\nDigite uma opção válida.')
                    continue
            if valor_variavel == '1':
                valor_variavel = tipo_variavel_1
                return classe_listar(self, opcao, valor_variavel)
            elif valor_variavel == '2':
                valor_variavel = tipo_variavel_2 
                return classe_listar(self, opcao, valor_variavel) 
            else:
                from modulo_agencia import Agencia
                Agencia().contas_opcao()
   
    def menu_acao(self, lista_menu_pessoa, opcao, valor_variavel, dado, dado_2):
        classe = lista_menu_pessoa['classe']
        tipo_variavel_2 = lista_menu_pessoa['tipo_variavel_2']
        self.n = 0
        self.opcao = opcao
        self.valor_variavel = valor_variavel
        self.dado = dado
        self.dado_2 = dado_2
        self.valor_dado = None
        self.valor_dado_2 = None
        self.n = 0; self.e = 0; self.f = True; self.t = True
        
        while True:            

            print('\nMenu (1)\n')
            if opcao == 'listar':                    
                self.valor_dado_2 = input(f'Digite o {dado_2}:\n')
                # if self.valor_dado_2.isnumeric():
                    #     self.valor_dado_2 = int(self.valor_dado_2)    # int forçado
            elif opcao == 'cadastrar': 
                self.valor_dado = input(f'Digite o {dado}:\n') 
                if self.valor_dado == '1':
                    from modulo_pessoa import Pessoa
                    return Pessoa().opcao_menu()
                self.valor_dado_2 = input(f'\nDigite o {dado_2}:\n') 

            elif opcao == 'descadastrar':            
                self.valor_dado_2 = input(f'Digite o {dado_2}:\n')
            
            if self.valor_dado == '1' or self.valor_dado_2 == '1':
                
                from modulo_pessoa import Pessoa
                return Pessoa().opcao_menu()
            
            if self.valor_variavel == tipo_variavel_2:
                self.n = 1

            return Lista(lista_menu_pessoa, self.__dict__)
            