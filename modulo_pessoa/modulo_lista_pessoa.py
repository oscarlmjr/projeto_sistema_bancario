import json


class Lista:   # 4.3.0_ 
    print('4.3.0_')
    def listar_variavel(self, agencia, contas, lista_self, pessoa_cadastrar=None, pessoa_transferir=None):   # 4.3.1_
        print('4.3.1_')
        print(f'\n{self.classe_nome}')
        pessoa_cadastrada = None
        nome_cadastrado = None
        dado_variavel = self.dado_variavel
        if pessoa_transferir is True:
            self.valor_agencia_transferir = contas['valor_agencia_transferir']
            valor_dado_variavel = contas['valor_dado_variavel']
            opcao = contas['opcao']
            opcao_pessoa = contas['opcao_conta']
        else:
            dado_nome_variavel = self.dado_nome_variavel
            valor_dado_variavel = self.valor_dado_variavel
            opcao = self.opcao
            opcao_pessoa = self.opcao_pessoa

        try:
            with open(self.lista_pessoa_json, 'r+', encoding='utf8') as arquivo:
                self.lista_pessoa = json.load(arquivo)
        except:
            with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)

        while True:

            for indice_pessoa, dados_pessoa in enumerate(self.lista_pessoa[opcao_pessoa]):
                for valor_dado, dados in dados_pessoa.items():
                    if valor_dado == valor_dado_variavel:
                        pessoa_cadastrada = True
                        break
                    elif opcao_pessoa == 1 and dados.get(self.dado_nome, ) == dado_nome_variavel:
                        pessoa_cadastrada = True
                        nome_cadastrado = True
                        break
                if pessoa_cadastrada == True:
                    break
            if pessoa_cadastrada == True:
                break
            pessoa_cadastrada = False
            break

        with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)

        if opcao == 'listar':
            if pessoa_cadastrada is True:
                if nome_cadastrado is True:
                    print(f'\nlistar__ {dado_nome_variavel} possui cadastro: {dado_variavel} {valor_dado}.')

                else:
                    print(f'\nlistar {dado_variavel} {valor_dado_variavel} possui cadastro.')
                print(self.lista_pessoa[opcao_pessoa][indice_pessoa][valor_dado], '\n')

            elif pessoa_cadastrada is False:
                print(f'\nlistar_ {dado_variavel} {valor_dado_variavel} não possui cadastro.')

        elif opcao == 'cadastrar':
            if pessoa_cadastrada is True:
                if nome_cadastrado is True:
                    print(f'\ncadastrar {dado_nome_variavel} possui cadastro: {dado_variavel} {valor_dado}.')
                    print(self.lista_pessoa[opcao_pessoa][indice_pessoa][valor_dado], '\n')

                else:
                    print(f'\ncadastrar {dado_variavel} {valor_dado_variavel} possui cadastro.')
                    print(self.lista_pessoa[opcao_pessoa][indice_pessoa][valor_dado_variavel], '\n')

                    if pessoa_cadastrar is True:

                        lista = self.lista_pessoa[opcao_pessoa][indice_pessoa][valor_dado_variavel]
                        self_contas = lista_self.get('self_contas', )

                        from modulo_contas.modulo_menu_contas import Menu
                        Menu.cadastrar_contas(self_contas, agencia, lista_self, lista)

                    from modulo_pessoa.modulo_menu_pessoa import Menu
                    Menu.menu_opcao(self, agencia, contas, lista_self)

            elif pessoa_cadastrada is False:
                print(f'\ncadastrar_ {dado_variavel} {valor_dado_variavel} não possui cadastro.')
                
                if pessoa_cadastrar is True:
                    while True:
                        direcionamento = input(f'\nDeseja cadastrar Pessoa:\nSim (1) / Não (2):\n')
                        if direcionamento != '1' and direcionamento != '2':
                            print('\nDigite uma opção válida.')
                            continue
                        elif direcionamento == '1':
                            break

                        self_contas = lista_self.get('self_contas', )

                        from modulo_contas.modulo_menu_contas import Menu
                        Menu.menu_opcao(self_contas, agencia, lista_self)

                if opcao_pessoa == 1:
                    from modulo_pessoa.modulo_lista_pessoa import Lista
                    Lista.cadastrar_pessoa(self, agencia, contas, lista_self, pessoa_cadastrar)

                from modulo_pessoa.modulo_menu_pessoa import Menu
                Menu.cadastrar_pessoas(self, agencia, contas, lista_self, pessoa_cadastrar)

        elif opcao == 'transferir':
            self.indice_pessoa = indice_pessoa
            self.opcao_pessoa = opcao_pessoa
            self.valor_dado_variavel = valor_dado_variavel
            self.lista_pessoa_transferir = self.lista_pessoa[opcao_pessoa][indice_pessoa]

            from modulo_pessoa.modulo_lista_pessoa import Lista
            Lista.cadastrar_pessoa(self, agencia, contas, lista_self, None, pessoa_transferir)

        if pessoa_cadastrar is True:
            self_contas = lista_self.get('self_contas', )

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self_contas, agencia, lista_self)

        from modulo_pessoa.modulo_menu_pessoa import Menu
        Menu.menu_opcao(self, agencia, contas, lista_self)

    def cadastrar_pessoa(self, agencia, contas, lista_self, pessoa_cadastrar=None, pessoa_transferir=None):   # 4.3.2_
        print('4.3.2_')

        if pessoa_transferir is True:
            self.lista_pessoa_json = f'lista_pessoa_{self.valor_agencia_transferir}.json'

        try:
            with open(self.lista_pessoa_json, 'r+', encoding='utf8') as arquivo:
                self.lista_pessoa = json.load(arquivo)
        except:
            self.lista_pessoa = [[], []]
            with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)

        if pessoa_transferir is True:

            for dados_pessoa in self.lista_pessoa[self.opcao_pessoa]:
                for valor_dado, dados in dados_pessoa.items():
                    if valor_dado == self.valor_dado_variavel:
                        self.lista_pessoa_json = f'lista_pessoa_{self.valor_agencia}.json'
                        self_contas = lista_self.get('self_contas')

                        from modulo_contas.modulo_menu_contas import Menu
                        Menu.menu_opcao(self_contas, agencia, lista_self)

            parada = input('\n4PARADA')
            self.lista_pessoa[self.opcao_pessoa].append(self.lista_pessoa_transferir)

            print(f'\n{self.lista_pessoa_json}:')
            print('\nCadastrando Pessoa.')
            print(f'\n{self.lista_pessoa_transferir}\n')

            with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)

            self.lista_pessoa_json = f'lista_pessoa_{self.valor_agencia}.json'
            self_contas = lista_self.get('self_contas')

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self_contas, agencia, lista_self)

        if self.opcao_pessoa == 0:
            lista = {self.dado_variavel: self.valor_dado_variavel, self.dado_nome: self.dado_nome_variavel,
                     self.dado_sexo: self.dado_sexo_variavel, self.tipo_pessoa: self.pessoa_variavel}

            self.lista_pessoa[0].append({lista.get(self.valor_dado_variavel, int(self.valor_dado_variavel)): lista})
        else: 
            lista = {self.dado_variavel: self.valor_dado_variavel, 
                    self.dado_nome: self.dado_nome_variavel, self.tipo_pessoa: self.pessoa_variavel}
            self.lista_pessoa[1].append({lista.get(self.valor_dado_variavel, int(self.valor_dado_variavel)): lista})

        with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)

        print(f'\n{self.dado_variavel} {self.valor_dado_variavel}__ cadastrado com sucesso.\n')

        # int forçado (?)
        print(f'{self.lista_pessoa[self.opcao_pessoa][-1][int(self.valor_dado_variavel)]}\n')
        # print(f'{self.lista_pessoa[self.opcao_pessoa][-1][self.valor_dado_variavel]}\n')   # ERROR

        if pessoa_cadastrar is True:
            self_contas = lista_self.get('self_contas', )

            while True:

                confirmacao = input(f'\nDeseja cadastrar a Conta:\nSim (1) Não (2)\n')
                if confirmacao != '1' and confirmacao != '2':
                    print('\nDigite uma opção válida.')
                    continue
                if confirmacao == '1':

                    from modulo_contas.modulo_menu_contas import Menu
                    Menu.cadastrar_contas(self_contas, agencia, lista_self, lista)
                break

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self_contas, agencia, lista_self)

        from modulo_pessoa.modulo_menu_pessoa import Menu
        Menu.menu_opcao(self, agencia, contas, lista_self)