import sys, json


class Menu:   # 2.2.0_
    print('2.2.0_')
    """
        Menu de autenticação.
        Caso não haja nenhum usuário cadastrado, o primeiro usuário será cadastrado
        sem processo de autenticação e com privilégio de administrador."""

    def menu_autenticacao(self, lista_self):   # 2.2.1_
        print('2.2.1_')
        print(f'\nBoa Vista Bank')
        print(f'{self.classe_nome} {self.valor_agencia}')
        print('Autenticação')
        print('Sair (0)\n')

        while True:
            valor_matricula = input(f'Digite a {self.matricula}:\n')
            # valor_matricula = '11111'
            # print(f'{self.matricula}: {valor_matricula}\n')
            if valor_matricula == '0':
                sys.exit('\nO sistema está sendo finalizado.\n')

            valor_senha = input(f'\nDigite a {self.senha}:\n')
            # valor_senha = '1204'
            # print(f'{self.senha}: {valor_senha}')
            if valor_senha == '0':
                sys.exit('\nO sistema está sendo finalizado.\n')

            if valor_matricula == '' or valor_senha == '':
                print('\nDigite sua matrícula e senha.\n')
                continue
            self.valor_matricula = valor_matricula
            self.valor_senha = valor_senha
            self.matriz_acesso_filial = None
            self.primeira_autenticacao = False

            try:
                with open(self.lista_acesso_json, 'r+', encoding='utf8') as arquivo:
                    self.lista_acesso = json.load(arquivo)
            except:
                with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

                if lista_self is not None:
                    self.opcao = 'cadastrar'
                    self.primeira_autenticacao = True
                else:
                    print('A autenticação está indisponível no momento.')
                    from modulo_agencia.modulo_menu_agencia import Menu
                    Menu.menu_autenticacao(self, lista_self)

                from modulo_agencia.modulo_lista_agencia import Lista
                Lista.lista_usuario(self, lista_self)

            from modulo_agencia.modulo_lista_agencia import Lista
            Lista.lista_autenticacao(self, lista_self)
    """
        O menu_opcao possui dois menus: um para administradores e usuários da agência Matriz
        e o outro menu para usuários das agências. Podendo cadastrar usuários (Cadastrar Usuário (1));
        e descadastrar usuários (Descadastrar Usuário (2)); acessar as contas bancárias das pessoas físicas 
        e jurídicas cadastradas (Contas (3)); usuários com permissão de administrador podem acessar o 
        menu da agência Matriz (Matriz (4)); e sair do sistema (Sair(4 ou 5))."""

    def menu_opcao(self, lista_self):   # 2.2.2_
        print('2.2.2_')
        self_matriz = lista_self.get('self_matriz', )
        print(f'\nBoa Vista Bank\n{self.classe_nome} {self.valor_agencia}')
        print('Menu (0)\n')

        while True:

            if self_matriz is not None:
                opcao = input('Cadastrar Usuário (1) / Descadastrar Usuário (2) / Contas (3) / Matriz (4) / Sair (5):\n')
                # opcao = '3'
                # print(f'{opcao}')
            else:
                opcao = input('Cadastrar Usuário (1) / Descadastrar Usuário (2) / Contas (3) / Sair (4):\n')

            if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                print('Digite uma opção válida.\n')
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

            sys.exit('\nO sistema está sendo finalizado.\n')

    def cadastrar_usuario(self, lista_self):   # 2.2.3_
        print('2.2.3_')
        print('\nCadastrar')

        while True:

            valor_matricula = input(f'\nDigite a_ {self.matricula}:\n')
            if valor_matricula == '0':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_opcao(self, lista_self)

            valor_senha = input(f'\nDigite a_ {self.senha}:\n')
            if valor_senha == '0':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_opcao(self, lista_self)

            if valor_matricula == '' or valor_senha == '':
                print('Digite uma matrícula e senha.\n')
                continue
            self.valor_matricula = valor_matricula
            self.valor_senha = valor_senha

            break

        from modulo_agencia.modulo_lista_agencia import Lista
        Lista.lista_usuario(self, lista_self)

    def descadastrar_usuario(self, lista_self):   # 2.2.4_
        print('2.2.4_')
        print('\nDescadastrar')
        self.opcao = 'descadastrar'

        while True:

            valor_matricula = input(f'\nDigite_ a {self.matricula}:\n')
            if valor_matricula == '0':
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_opcao(self, lista_self)

            if valor_matricula == '':
                print('\nDigite uma opção válida.')
                continue

            self_matriz = lista_self.get('self_matriz', )
            if self.valor_matricula_autenticada == valor_matricula and self_matriz is None:
                print('\nVocê não pode descadastrar a matrícula ativa na sessão.')
                continue

            self.valor_matricula = valor_matricula

            break

        from modulo_agencia.modulo_lista_agencia import Lista
        Lista.lista_usuario(self, lista_self)
