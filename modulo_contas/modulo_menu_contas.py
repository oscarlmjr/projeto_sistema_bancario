import sys, json


class Menu:   # 3.2.0_
    print('3.2.0_')
    """
        O menu_opcao possui dois menus: um para administradores e usuários da agência Matriz
        e o outro menu para usuários das agências. Podendo listar uma conta do cliente apartir do
        seu RG ou CNPJ, ou do número da conta corrente ou poupança (Cliente (1));
        cadastrar contas pessoa física ou jurídica (Cadastrar (2)); retornar todas as contas de cada cliente
        apartir do seu RG ou CNPJ (Retornar ocorrências (3)); transferir a conta, ou as contas de um cliente
        para outra agência (Transferir (4)); descadastrar uma conta (Descadastrar (5)); acessar o menu Pessoa
        onde as informações pessoais dos clientes estão cadastradas e podem ser alteradas (Pessoa (6));
        retornar para o menu da agência (Agência (7)); usuários com permissão de administrador podem acessar o 
        menu da agência Matriz (Matriz (8)); e sair do sistema (Sair(8 ou 9))."""
    def menu_opcao(self, agencia, lista_self):   # 3.2.1_
        print('3.2.1_')
        classe_nome = agencia['classe_nome']
        self_matriz = lista_self.get('self_matriz', )
        self.valor_conta_variavel = None

        print(f'\nBoa Vista Bank\n{classe_nome} {self.valor_agencia}\n{self.classe_nome}')
        print('Menu (0)\n')

        while True:

            if self_matriz is not None:
                opcao = input('Cliente (1) / Cadastrar (2) / Retornar ocorrências (3) / Transferir (4)'
                                f' / Inativar (5)\nPessoa (6) / Agência (7) / Matriz (8) / Sair (9):\n')
                # opcao = '1'
                # print(f'{opcao}')
            else:
                opcao = input('Cliente (1) / Cadastrar (2) / Retornar ocorrências (3) / Transferir (4)'
                                f' / Inativar (5)\nPessoa (6) / Agência (7) / Sair (8):\n')

            if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' \
            and opcao != '7' and opcao != '8' and opcao != '9':
                print('\nDigite uma opção válida.\n')
                continue

            if opcao == '1':
                self.opcao = 'listar'
                from modulo_contas.modulo_menu_contas import Menu
                Menu.listar_contas(self, agencia, lista_self)

            elif opcao == '2':
                self.opcao = 'cadastrar'
                
                from modulo_contas.modulo_menu_contas import Menu
                Menu.cadastrar_contas(self, agencia, lista_self)

            elif opcao == '3':
                self.opcao = 'ocorrencias'
                from modulo_contas.modulo_menu_contas import Menu
                Menu.ocorrencias_contas(self, agencia, lista_self)

            elif opcao == '4':
                self.opcao = 'transferir'
                from modulo_contas.modulo_menu_contas import Menu
                Menu.transferir_contas(self, agencia, lista_self)
                
            elif opcao == '5':
                self.opcao = 'inativar'
                from modulo_contas.modulo_menu_contas import Menu
                Menu.inativar_contas(self, agencia, lista_self)

            elif opcao == '6':
                self.conta_cadastrada = None 
                self_pessoa = lista_self.get('self_pessoa',)
                from modulo_pessoa.modulo_menu_pessoa import Menu
                Menu.menu_opcao(self_pessoa, agencia, self.__dict__, lista_self)

            elif opcao == '7':
                self_agencia = lista_self.get('self_agencia', )
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_opcao(self_agencia, lista_self)

            elif self_matriz is not None and opcao == '8':
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, agencia, lista_self)

            sys.exit('\nO sistema está sendo finalizado.\n')

    def listar_contas(self, agencia, lista_self):   # 3.2.2_
        print('3.2.2_')
        print('Cliente')

        while True:

            valor_conta_variavel = input(f'\n{self.nome_conta}:\n')
            # valor_conta_variavel = '11141'
            # print(valor_conta_variavel)
            if valor_conta_variavel == '0':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            elif valor_conta_variavel == '':
                print('\nDigite uma opção válida.')
                continue
            if valor_conta_variavel[0] == '1':
                if valor_conta_variavel[-1] == '1':
                    self.digito_conta = '1'
                    self.conta_variavel = self.conta_corrente
                else:
                    self.digito_conta = '2'
                    self.conta_variavel = self.conta_poupanca
                self.opcao_conta = 0
            else:
                self.opcao_conta = 1
                self.digito_conta = '1'
                self.conta_variavel = self.conta_corrente
            self.valor_conta_variavel = valor_conta_variavel

            break

        from modulo_contas.modulo_lista_contas import Lista
        Lista.listar_contas(self, agencia, lista_self)

    def cadastrar_contas(self, agencia, lista_self, lista=None):   # 3.2.3_
        print('3.2.3_')
        print('Cadastrar\n')

        if self.opcao == 'cadastrar':
            if lista is None:
                pessoa_cadastrar = True
                self_pessoa = lista_self.get('self_pessoa', )

                from modulo_pessoa.modulo_menu_pessoa import Menu
                Menu.teste_dado_variavel(self_pessoa, agencia, self.__dict__, lista_self, pessoa_cadastrar)

            if lista.get(self.tipo_pessoa, ) == self.pessoa_fisica:
                while True:
                    conta_variavel = input(f'\n{self.conta_corrente} (1) {self.conta_poupanca} (2):\n')

                    if conta_variavel == '0':
                        from modulo_contas.modulo_menu_contas import Menu
                        Menu.menu_opcao(self, agencia, lista_self)
                    elif conta_variavel == '':
                        print('\nDigite uma opção válida.')
                        continue

                    if conta_variavel == '1':
                        self.digito_conta = '1'
                        self.conta_variavel = self.conta_corrente
                    else:
                        self.digito_conta = '2'
                        self.conta_variavel = self.conta_poupanca
                    self.opcao_conta = 0

                    break
            else:
                print((f'\n{self.conta_corrente}\n'))
                self.digito_conta = '1'
                self.conta_variavel = self.conta_corrente
                self.opcao_conta = 1

        if self.opcao == 'transferir':

            self.lista_conta_json = f'lista_conta_{self.valor_agencia_transferir}.json'

        try:
            with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
                    self.lista_contas = json.load(arquivo)

            for valor_conta in self.lista_contas[self.opcao_conta]:
                for conta_numero in valor_conta.keys():

                    if self.opcao_conta == 1:
                        conta_variavel = conta_numero
                    else:
                        if conta_numero[-1] == self.digito_conta:
                            conta_variavel = conta_numero

            if self.opcao_conta == 0:
                conta_variavel = int(conta_variavel[-2])
                conta_variavel += 1
                conta_variavel = str(conta_variavel) + self.digito_conta
                valor_conta_variavel = conta_variavel.rjust(5, '1')

            else:
                conta_variavel = int(conta_variavel[-1])
                conta_variavel += 1
                conta_variavel = str(conta_variavel)
                valor_conta_variavel = '2' + conta_variavel.rjust(4, '1')
        except:

            if self.opcao_conta == 0:
                valor_conta_variavel = '1111' + self.digito_conta
            else:
                valor_conta_variavel = '21111'

        with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)

        self.lista_conta_json = f'lista_conta_{self.valor_agencia}.json'

        if self.opcao == 'transferir':
            self.valor_conta_transferir = valor_conta_variavel

            from modulo_contas.modulo_lista_contas import Lista
            Lista.listar_contas(self, agencia, lista_self)

        self.valor_conta_variavel = valor_conta_variavel

        from modulo_contas.modulo_lista_contas import Lista
        Lista.cadastrar_conta(self, agencia, lista_self, lista)

    def ocorrencias_contas(self, agencia, lista_self):   # 3.2.4_
        print('3.2.4_')
        print('Retornar Ocorrências')

        while True:
            dado_valor = input(f'\n{self.dado_rg} (1) {self.dado_cnpj} (2):\n')
            if dado_valor == '0':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            elif dado_valor != '1' and dado_valor != '2':
                print('\nDigite_ uma opção válida.\n')
                continue

            if dado_valor == '1':
                self.opcao_conta = 0
                self.dado_variavel = self.dado_rg
                valor_dado_variavel = input(f'\nDigite o {self.dado_rg}:\n')
            else:
                self.opcao_conta = 1
                self.dado_variavel = self.dado_cnpj
                valor_dado_variavel = input(f'\nDigite o {self.dado_cnpj}:\n')

            if valor_dado_variavel == '0':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            elif valor_dado_variavel == '':
                print('\nDigite uma opção válida.')
                continue

            break

        self.valor_dado_variavel = valor_dado_variavel

        from modulo_contas.modulo_lista_contas import Lista
        Lista.listar_contas(self, agencia, lista_self)

    def transferir_contas(self, agencia, lista_self):   # 3.2.5_
        print('3.2.5_')
        valor_agencia = agencia['valor_agencia']
        print('Transferir')

        while True:

            valor_conta_variavel = input(f'\n{self.nome_conta}:\n')
            # valor_conta_variavel = '11111'
            # print(f'{valor_conta_variavel}')
            if valor_conta_variavel == '0':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            elif valor_conta_variavel == '':
                print('\nDigite uma opção válida.')
                continue

            if valor_conta_variavel[0] == '1':
                self.opcao_conta = 0
                self.dado_variavel = self.dado_rg
                self.pessoa_variavel = self.pessoa_fisica
                if valor_conta_variavel[-1] == '1':
                    self.conta_variavel = self.conta_corrente
                    self.digito_conta = '1'
                else:
                    self.conta_variavel = self.conta_poupanca
                    self.digito_conta = '2'
            else:
                self.opcao_conta = 1
                self.dado_variavel = self.dado_cnpj
                self.pessoa_variavel = self.pessoa_juridica
                self.conta_variavel = self.conta_corrente
                self.digito_conta = '1'

            self.valor_conta_variavel = valor_conta_variavel
            break

        while True:

            valor_agencia_filial = input('\nDigite o número da agência para a qual deseja transferir:\n')
            # valor_agencia_filial = '0002'
            # print(f'{valor_agencia_filial}')
            if valor_agencia_filial == '':
                print('Digite uma opção válida.\n')
                continue

            elif valor_agencia_filial == '0':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            elif valor_agencia_filial == valor_agencia:
                print('\nVocê não pode transferir para a mesma agência.\n')
                continue
            break

        self.valor_agencia_filial = valor_agencia_filial

        from modulo_matriz.modulo_lista_matriz import Lista
        Lista.acesso_filial(self, agencia, lista_self)

    def inativar_contas(self, agencia, lista_self):   # 3.2.6_
        print('3.2.6_')
        print('Inativar')

        while True:

            valor_conta_variavel = input(f'\n{self.nome_conta}:\n')
            if valor_conta_variavel == '0':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            elif valor_conta_variavel == '':
                print('\nDigite uma opção válida.')
                continue

            if valor_conta_variavel[0] == '1':
                self.opcao_conta = 0
                self.dado_variavel = self.dado_rg
                self.pessoa_variavel = self.pessoa_fisica
                if valor_conta_variavel[-1] == '1':
                    self.conta_variavel = self.conta_corrente
                else:
                    self.conta_variavel = self.conta_poupanca
            else:
                self.opcao_conta = 1
                self.dado_variavel = self.dado_cnpj
                self.pessoa_variavel = self.pessoa_juridica
                self.conta_variavel = self.conta_corrente

            self.valor_conta_variavel = valor_conta_variavel

            from modulo_contas.modulo_lista_contas import Lista
            Lista.listar_contas(self, agencia, lista_self)
