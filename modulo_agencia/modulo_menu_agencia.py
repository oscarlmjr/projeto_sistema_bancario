import sys, json


class Menu: 

    def menu_autenticacao(self, lista_self, valor_agencia_filial=None):   # _4.1.1
        
        while True:

            print(f'\nBoa Vista Bank')
            print(f'{self.classe_nome} {self.valor_agencia}')
            print('Autenticação')
            print('Sair (1)\n')
            
            self.valor_matricula_acesso = input(f'Digite a {self.matricula}:\n')
            if self.valor_matricula_acesso == '1':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.saida()
                    
            self.valor_senha_acesso = input(f'\nDigite a {self.senha}:\n')
            if self.valor_senha_acesso == '1':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.saida()

            if valor_agencia_filial is not None:
                try:
                    self.lista_acesso_json = f'lista_acesso_{valor_agencia_filial}.json'

                    with open(self.lista_acesso_json, 'r+', encoding='utf8'):
                        self.usuario_autenticado = True
                        
                except:
                    self.lista_acesso_json = f'lista_acesso_0001.json'
                    print('\nexcept')                

            from modulo_agencia.modulo_lista_agencia import Lista
            Lista.lista_autenticacao(self, lista_self, valor_agencia_filial)
            
            # self.valor_matricula_acesso = '11112'
            # self.valor_senha_acesso = '1205'
            
    def menu_opcao(self, lista_self):
        self_matriz = lista_self.get('self_matriz', )

        while True:

            print(f'\nBoa Vista Bank\n{self.classe_nome} {self.valor_agencia}\n')

            if self_matriz is not None:
                opcao = input('Cadastrar Usuário (1) / Descadastrar Usuário (2) / Contas (3) / Matriz (4) / Sair (5):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                    print('Digite uma opção válida.')
                    continue  
                              
            else:
                opcao = input('Cadastrar Usuário (1) / Descadastrar Usuário (2) / Contas (3) / Sair (4):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4':
                    print('Digite uma opção válida.')
                    continue  

            if opcao == '1':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.cadastrar_usuario(self, lista_self)

            elif opcao == '2':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.descadastrar_usuario(self, lista_self)

            elif opcao == '3': 
                from modulo_contas.modulo_contas import Contas
                Contas(self.__dict__).menu_opcao(self.__dict__, lista_self)
                
            elif self_matriz is not None and opcao == '4': 
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, self.__dict__, lista_self)
            
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.saida()

    def cadastrar_usuario(self, lista_self):
            
        valor_matricula = input(f'\nDigite a_ {self.matricula}:\n')
        if valor_matricula == '1':
            Menu.menu_opcao(self, lista_self)
        self.valor_matricula = valor_matricula

        valor_senha = input(f'\nDigite a_ {self.senha}:\n')
        if valor_senha == '1':
            Menu.menu_opcao(self, lista_self)
        self.valor_senha = valor_senha
                
        from modulo_agencia.modulo_lista_agencia import Lista
        Lista.lista_usuario(self, lista_self)

    def descadastrar_usuario(self, lista_self):
        self.opcao = 'descadastrar'

        self.valor_matricula = input(f'\nDigite_ a {self.matricula}:\n')
        
        from modulo_agencia.modulo_lista_agencia import Lista
        Lista.lista_usuario(self, lista_self)

    def saida():   # _4.1.5
        
        sys.exit('\nO sistema está sendo finalizado.\n')
