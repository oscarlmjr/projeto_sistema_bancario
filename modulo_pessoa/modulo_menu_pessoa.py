import sys


class Menu:   # 4.2.0_
    print('4.2.0_')
    def menu_opcao(self, agencia, contas, lista_self):   # 4.2.1_
        print('4.2.1_')
        classe_nome = agencia['classe_nome']
        self_matriz = lista_self.get('self_matriz', )

        while True:

            print(f'\nBoa Vista Bank\n{classe_nome} {self.valor_agencia}\n{self.classe_nome}')
            print('Menu (0)\n')

            if self_matriz is not None:
                opcao = input('Listar (1) / Cadastrar (2) / Contas (3) / Agência (4) / Matriz (5) / Sair (6):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6':
                    print('Digite uma opção válida.\n')
                    continue
                # opcao = '1'
                # print(f'{opcao}')
            else:
                opcao = input('Listar (1) / Cadastrar (2) / Contas (3) / Agência (4) / Sair (5):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                    print('Digite uma opção válida.\n')
                    continue

            if opcao == '1':
                self.opcao = 'listar'
                from modulo_pessoa.modulo_menu_pessoa import Menu
                Menu.teste_dado_variavel(self, agencia, contas, lista_self)

            elif opcao == '2':
                self.opcao = 'cadastrar'
                from modulo_pessoa.modulo_menu_pessoa import Menu
                Menu.teste_dado_variavel(self, agencia, contas, lista_self)

            elif opcao == '3':
                self_contas = lista_self.get('self_contas', )
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self_contas, agencia, lista_self)

            elif opcao == '4':
                self_agencia = lista_self.get('self_agencia', )
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_opcao(self_agencia, lista_self)

            elif self_matriz is not None and opcao == '5':
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, agencia, lista_self)

            sys.exit('\nO sistema está sendo finalizado.\n')

    def listar_pessoas(self, agencia, contas, lista_self):   # 4.2.2_
        print('4.2.2_')

        from modulo_pessoa.modulo_lista_pessoa import Lista
        Lista.listar_variavel(self, agencia, contas, lista_self)

    def cadastrar_pessoas(self, agencia, contas, lista_self, pessoa_cadastrar=None):   # 4.2.3_
        print('4.2.3_')

        while True:

            dado_nome_variavel = input(f'\nDigite o {self.dado_nome}:\n')
            if dado_nome_variavel == '':
                print('\nDigite uma opção válida.')
                continue
            elif dado_nome_variavel == '0':
                break

            self.dado_nome_variavel = dado_nome_variavel

            if self.opcao_pessoa == 0:
                dado_sexo_variavel = input(f'\nDigite o {self.dado_sexo}:\nMasculino (m) Feminino (f)\n')
                if dado_sexo_variavel == '0':
                    break
                elif dado_sexo_variavel != 'm' and dado_sexo_variavel != 'f':
                        print('\nDigite uma opção válida.')
                        continue
                self.dado_sexo_variavel = dado_sexo_variavel

            while True:
                confirmacao = input('\nConfirma a criação da conta para os dados informados: Sim (1) / Não (2)\n')
                if confirmacao != '1' and confirmacao != '2':
                    print('\nDigite uma opção válida.\n')
                    continue
                elif confirmacao == '2':
                    break

                from modulo_pessoa.modulo_lista_pessoa import Lista
                Lista.cadastrar_pessoa(self, agencia, contas, lista_self, pessoa_cadastrar)

            if confirmacao == '0' or confirmacao == '2':
                break

        if pessoa_cadastrar is True:
            self_contas = lista_self.get('self_contas', )

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self_contas, agencia, lista_self)

        from modulo_pessoa.modulo_menu_pessoa import Menu
        Menu.menu_opcao(self, agencia, contas, lista_self)

    def teste_dado_variavel(self, agencia, contas, lista_self, pessoa_cadastrar=None):   # 4.2.4_
        print('4.2.4_')
        print('\nPessoa')

        if pessoa_cadastrar is not None:
            self.opcao = contas['opcao']

        while True:
            pessoa_variavel = input(f'\n{self.pessoa_fisica} (1) / {self.pessoa_juridica} (2):\n')
            if pessoa_variavel == '0':
                break
            if pessoa_variavel != '1' and pessoa_variavel != '2':
                print('\nDigite uma opção válida.')
                continue

            if pessoa_variavel == '1':
                valor_dado_variavel = input(f'\nDigite_ o {self.dado_rg}:\n')
                if valor_dado_variavel == '0':
                    break
                elif valor_dado_variavel == '':
                    print('\nDigite uma opção válida.')
                    continue
                self.opcao_pessoa = 0
                self.dado_variavel = self.dado_rg
                self.pessoa_variavel = self.pessoa_fisica
            else:
                valor_dado_variavel = input(f'\nDigite__ o {self.dado_cnpj}:\n')
                if valor_dado_variavel == '0':
                    break
                elif valor_dado_variavel == '':
                    print('\nDigite uma opção válida.')
                    continue
                dado_nome_variavel = input(f'\nDigite o {self.dado_nome}:\n')
                if dado_nome_variavel == '':
                    print('\nDigite uma opção válida.')
                    continue
                elif dado_nome_variavel == '0':
                    break
                self.opcao_pessoa = 1
                self.dado_variavel = self.dado_cnpj
                self.pessoa_variavel = self.pessoa_juridica
                self.dado_nome_variavel = dado_nome_variavel
            self.digito_pessoa = pessoa_variavel
            self.valor_dado_variavel = valor_dado_variavel

            if self.opcao == 'listar':
                from modulo_pessoa.modulo_menu_pessoa import Menu
                Menu.listar_pessoas(self, agencia, contas, lista_self)

            elif self.opcao == 'cadastrar':

                from modulo_pessoa.modulo_lista_pessoa import Lista
                Lista.listar_variavel(self, agencia, contas, lista_self, pessoa_cadastrar)

        if pessoa_cadastrar is True:
            self_contas = lista_self.get('self_contas', )

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self_contas, agencia, lista_self)

        from modulo_pessoa.modulo_menu_pessoa import Menu
        Menu.menu_opcao(self, agencia, contas, lista_self)
