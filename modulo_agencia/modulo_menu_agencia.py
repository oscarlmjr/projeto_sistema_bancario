import sys, json

print('2.2.0_')
class Menu:   # 2.2.1.0_
    print('2.2.1.0_')
    """
        Menu de autenticação.
        Caso não haja nenhum usuário cadastrado, o primeiro usuário será cadastrado
        sem processo de autenticação e com privilégio de administrador."""
    def menu_autenticacao(self, lista_self, valor_agencia_filial=None):   # 2.2.1.1_
        print('2.2.1.1_')

        while True:

            print(f'\nBoa Vista Bank')
            print(f'{self.classe_nome} {self.valor_agencia}')
            print('Autenticação')
            print('Sair (1)\n')

            self.valor_matricula_acesso = input(f'Digite a {self.matricula}:\n')
            # self.valor_matricula_acesso = '11111'
            print(f'{self.matricula}: {self.valor_matricula_acesso}\n')
            if self.valor_matricula_acesso == '1':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.saida()

            self.valor_senha_acesso = input(f'\nDigite a {self.senha}:\n')
            # self.valor_senha_acesso = '1204'
            print(f'{self.senha}: {self.valor_senha_acesso}')
            if self.valor_senha_acesso == '1':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.saida()

            if self.valor_matricula_acesso == '' or self.valor_senha_acesso == '':
                print('\nDigite sua matrícula e senha.\n')
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_autenticacao(self, lista_self, valor_agencia_filial)

            if valor_agencia_filial is not None:
                try:
                    self.lista_acesso_json = f'lista_acesso_{valor_agencia_filial}.json'   # >>>

                    with open(self.lista_acesso_json, 'r+', encoding='utf8'):
                        self.usuario_autenticado = True

                except:
                    ...

            from modulo_agencia.modulo_lista_agencia import Lista
            Lista.lista_autenticacao(self, lista_self, valor_agencia_filial)
    """
        O menu_opcao possui dois menus: um para administradores e usuários da agência Matriz
        e o outro menu para usuários das agências. Podendo cadastrar usuários (Cadastrar Usuário (1));
        e descadastrar usuários (Descadastrar Usuário (2)); acessar as contas bancárias das pessoas físicas 
        e jurídicas cadastradas (Contas (3)); usuários com permissão de administrador podem acessar o 
        menu da agência Matriz (Matriz (4)); e sair do sistema (Sair(4 ou 5))."""
    def menu_opcao(self, lista_self):   # 2.2.1.2_
        print('2.2.1.2_')
        self_matriz = lista_self.get('self_matriz', )

        while True:

            print(f'\nBoa Vista Bank\n{self.classe_nome} {self.valor_agencia}\n')

            if self_matriz is not None:
                opcao = input('Cadastrar Usuário (1) / Descadastrar Usuário (2) / Contas (3) / Matriz (4) / Sair (5):\n')
            else:
                opcao = input('Cadastrar Usuário (1) / Descadastrar Usuário (2) / Contas (3) / Sair (4):\n')
 
            if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                print('Digite uma opção válida.')
                continue

            if opcao == '1':
                self.opcao = 'cadastrar'
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.cadastrar_usuario(self, lista_self)

            elif opcao == '2':
                self.opcao = 'descadastrar'
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.descadastrar_usuario(self, lista_self)

            elif opcao == '3':
                self_contas = lista_self.get('self_contas', )
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self_contas, self.__dict__, lista_self)

            elif self_matriz is not None and opcao == '4': 
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, self.__dict__, lista_self)
            
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.saida()

    def cadastrar_usuario(self, lista_self):   # 2.2.1.3_
        print('2.2.1.3_')
        print('\nCadastrar')
        print("'1' para retornar ao Menu")

        valor_matricula = input(f'\nDigite a_ {self.matricula}:\n')
        if valor_matricula == '1':
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.menu_opcao(self, lista_self)
        self.valor_matricula = valor_matricula

        valor_senha = input(f'\nDigite a_ {self.senha}:\n')
        if valor_senha == '1':
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.menu_opcao(self, lista_self)
        self.valor_senha = valor_senha

        if self.valor_matricula == '' or self.valor_senha == '':
            print('Digite uma matrícula e senha.\n')
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.cadastrar_usuario(self, lista_self)

        from modulo_agencia.modulo_lista_agencia import Lista
        Lista.lista_usuario(self, lista_self)

    def descadastrar_usuario(self, lista_self):   # 2.2.1.4_
        print('2.2.1.4_')
        print('\nDescadastrar')
        print("'1' para retornar ao Menu")
        self.opcao = 'descadastrar'

        self.valor_matricula = input(f'\nDigite_ a {self.matricula}:\n')
        if self.valor_matricula == '1':
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.menu_opcao(self, lista_self)

        if self.valor_matricula == '':
            print('Digite uma matrícula.\n')
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.descadastrar_usuario(self, lista_self)

        from modulo_agencia.modulo_lista_agencia import Lista
        Lista.lista_usuario(self, lista_self)

    def saida():   # 2.2.1.5_
        print('2.2.1.5_')

        sys.exit('\nO sistema está sendo finalizado.\n')
