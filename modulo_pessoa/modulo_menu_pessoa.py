import sys


class Menu:

    def menu_opcao(self, agencia, contas, lista_self):         
        classe_nome = agencia['classe_nome']
        self_matriz = lista_self.get('self_matriz', )

        while True:

            print(f'\nBoa Vista Bank\n{classe_nome} {self.valor_agencia}\n{self.classe_nome}\n')
            
            if self_matriz is not None:
                opcao = input('Listar (1) / Cadastrar (2) / Descadastrar (3) / Contas (4) / Agência (5) / Matriz (6) / Sair (7):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7':
                    print('Digite uma opção válida.\n')
                    continue  
            else:
                opcao = input('Listar (1) / Cadastrar (2) / Descadastrar (3) / Contas (4) / Agência (5) / Sair (6):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6':
                    print('Digite uma opção válida.\n')
                    continue  
            
            if opcao == '1':
                self.opcao = 'Listar'
            elif opcao == '2':
                self.opcao = 'Cadastrar'
            elif opcao == '3':
                self.opcao = 'Descadastrar'
            elif opcao == '4': 
                agencia['valor_agencia'] = self.valor_agencia  

                from modulo_contas.modulo_contas import Contas
                Contas(agencia).menu_opcao(agencia, lista_self)
                
            elif opcao == '5':                   
                from modulo_agencia_matriz import Matriz
                Matriz(self.valor_agencia).menu_agencia(lista_self)
                
            elif self_matriz is not None and opcao == '6':
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, agencia, lista_self)
                
            elif opcao == '6' or  opcao == '7':
                from modulo_pessoa.modulo_menu_pessoa import Menu
                Menu.saida()                        

            print(self.opcao)
            pessoa_variavel = input(f'\n{self.pessoa_fisica} (1) / {self.pessoa_juridica} (2):\n')

            if pessoa_variavel != '1' and pessoa_variavel != '2':
                    print('\nDigite uma opção válida.')
                    continue    
                    
            if pessoa_variavel == '2':
                self.pessoa_variavel = self.pessoa_juridica
                self.dado_variavel = self.dado_cnpj
                self.opcao_pessoa = 1

            from modulo_pessoa.modulo_menu_pessoa import Menu
            Menu.menu_acao(self, agencia, contas, lista_self)
   
    def menu_acao(self, agencia, contas, lista_self): 
        
        conta_cadastrada = contas['conta_cadastrada']
        print(f'\nconta_cadastrada___ = {conta_cadastrada}')
        
        while True:            

            print('\nMenu (1)')
            if self.opcao == 'Listar':
                print(f'\n{self.opcao}')                    
                self.valor_dado_variavel = input(f'\nDigite o {self.dado_variavel}:\n')
                
            elif self.opcao == 'Cadastrar': 
                print(f'\n{self.opcao}')                    
                self.dado_nome_variavel = input(f'\nDigite o {self.dado_nome}:\n') 

                if self.dado_nome_variavel == '1':
                    Menu.menu_opcao(self, agencia, contas, lista_self)

                if self.pessoa_variavel == self.pessoa_fisica:
                    self.dado_sexo_variavel = input(f'\nDigite o {self.dado_sexo}:\nMasculino (m) Feminino (f)\n')

                    if self.dado_sexo_variavel != 'm' and self.dado_sexo_variavel != 'f':
                        print('\nDigite uma opção válida.')
                        continue                
                        
                if self.valor_dado_variavel is None:
                    self.valor_dado_variavel = input(f'\nDigite o {self.dado_variavel}:\n') 

            elif self.opcao == 'Descadastrar':            
                print(f'\n{self.opcao}')                    
                self.valor_dado_variavel = input(f'\nDigite o {self.dado_variavel}:\n')
            
            if self.valor_dado_variavel == '1':                
                Menu.menu_opcao(self, agencia, contas, lista_self)
            
            from modulo_pessoa.modulo_lista_pessoa import Lista
            Lista.listar_variavel(self, agencia, contas, lista_self)
        
    def saida():
    
        sys.exit('\nO sistema está sendo finalizado.\n')
        