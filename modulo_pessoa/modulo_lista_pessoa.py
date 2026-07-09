import json


print('4.3.0_')
class Lista:   # 4.3.1.0_ 
    print('4.3.1.0_')
    def listar_variavel(self, agencia, contas, lista_self):   # 4.3.1.1_
        print('4.3.1.1_')
        conta_cadastrada = contas['conta_cadastrada']
        pessoa_cadastrada = False

        if conta_cadastrada is False:
            self.opcao_conta = contas['opcao_conta']
            self.opcao_pessoa = self.opcao_conta
            self.opcao = contas['opcao']
            self.dado_variavel = contas['dado_variavel']
            self.valor_dado_variavel = contas['valor_dado_variavel']

        try:
            with open(self.lista_pessoa_json, 'r+', encoding='utf8') as arquivo:
                self.lista_pessoa = json.load(arquivo)
                if self.lista_pessoa is None:
                    self.lista_pessoa = [[], []]
            lista_pessoa = True  
        except:
            with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)
            lista_pessoa = None

        if lista_pessoa is True:

            while True:

                for self.indice_pessoa, dados_pessoa in enumerate(self.lista_pessoa[self.opcao_pessoa]):
                    for valor_dado_variavel, dados in dados_pessoa.items():
                        if valor_dado_variavel == self.valor_dado_variavel:
                            pessoa_cadastrada = True
                            break
                    if pessoa_cadastrada == True:
                        break
                break

        if self.opcao == 'Listar' and pessoa_cadastrada is True:
            print(f'\nlistar {self.dado_variavel} {self.valor_dado_variavel} possui cadastro.')
            print(self.lista_pessoa[self.opcao_pessoa][self.indice_pessoa][self.valor_dado_variavel], '\n')
        elif self.opcao == 'Listar' and pessoa_cadastrada is False:

            print(f'\nlistar_ {self.dado_variavel} {self.valor_dado_variavel} não possui cadastro.')

        if self.opcao == 'Listar' and conta_cadastrada is False:
            self.opcao_conta = 0
            self.opcao_pessoa = self.opcao_conta
            self.opcao = None
            self.dado_variavel = self.dado_rg
            self.valor_dado_variavel = None
            self_contas = lista_self.get('self_contas', )

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self_contas, agencia, lista_self)

        elif self.opcao == 'Cadastrar' and pessoa_cadastrada is True:
            print(f'\ncadastrar {self.dado_variavel} {self.valor_dado_variavel} possui cadastro.')
            print(self.lista_pessoa[self.opcao_pessoa][self.indice_pessoa][self.valor_dado_variavel], '\n')

            if conta_cadastrada is False:
                lista = self.lista_pessoa[self.opcao_pessoa][self.indice_pessoa][self.valor_dado_variavel]
                self_contas = lista_self.get('self_contas', )

                from modulo_contas.modulo_lista_contas import Lista
                Lista.cadastrar_conta(self_contas, agencia, lista, lista_self)

        elif self.opcao == 'Cadastrar' and pessoa_cadastrada is False:
            print(f'\ncadastrar_ {self.dado_variavel} {self.valor_dado_variavel} não possui cadastro.')

            if conta_cadastrada is False:

                while True:
                    direcionamento = input(f'\n{self.classe_nome}\n\nDeseja cadastrar Pessoa:\nSim (1) / Não (2):\n')
                    if direcionamento != '1' and direcionamento != '2':
                        print('\nDigite uma opção válida.')
                        continue

                    if direcionamento == '1':
                        contas.update(conta_cadastrada=None)

                        if self.dado_variavel == self.dado_cnpj:
                            self.pessoa_variavel = self.pessoa_juridica 
                            self.opcao_pessoa = 1

                        from modulo_pessoa.modulo_menu_pessoa import Menu
                        Menu.menu_acao(self, agencia, contas, lista_self)
                        
                    from modulo_pessoa.modulo_lista_pessoa import Lista
                    Lista.direcionamento(self, agencia, contas, lista_self)
                    break

            conta_cadastrada = False
            contas.update(conta_cadastrada=conta_cadastrada)

            from modulo_pessoa.modulo_lista_pessoa import Lista
            Lista.cadastrar_pessoa(self, agencia, contas, lista_self)

        elif self.opcao == 'Descadastrar' and pessoa_cadastrada is True:
            print(f'Descadastrando: {self.dado_variavel} {self.valor_dado_variavel}\n')

            from modulo_pessoa.modulo_lista_pessoa import Lista
            Lista.descadastrar_pessoa(self, agencia, contas, lista_self)

        elif self.opcao == 'Descadastrar' and pessoa_cadastrada is False:
            print(f'descadastrar {self.dado_variavel} {self.valor_dado_variavel} não possui cadastro.')

        contas['valor_agencia'] = self.valor_agencia

        from modulo_pessoa.modulo_pessoa import Pessoa
        Pessoa(contas).menu_opcao(agencia, contas, lista_self)

    def cadastrar_pessoa(self, agencia, contas, lista_self):   # 4.3.1.2_
        print('4.3.1.2_')
        conta_cadastrada = contas['conta_cadastrada']
        valor_conta_variavel = contas['valor_conta_variavel']
        conta_variavel = contas['conta_variavel']

        if self.pessoa_variavel == self.pessoa_fisica:
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

        if conta_cadastrada is False:

            while True:
                direcionamento = input(f'\n{self.classe_nome}\n\nDeseja cadastrar Conta:\nSim (1) / Não (2):\n')
                if direcionamento != '1' and direcionamento != '2':
                    print('\nDigite uma opção válida.')
                    continue

                if direcionamento == '1':   
                    self_contas = lista_self.get('self_contas', )
                    agencia.update(valor_conta_variavel=valor_conta_variavel)
                    agencia.update(conta_variavel=conta_variavel)
                    agencia.update(conta_cadastrada=conta_cadastrada)
                    agencia.update(opcao_conta=self.opcao_conta)

                    from modulo_contas.modulo_lista_contas import Lista
                    Lista.cadastrar_conta(self_contas, agencia, lista, lista_self)

                break

        from modulo_pessoa.modulo_lista_pessoa import Lista
        Lista.direcionamento(self, agencia, contas, lista_self)

    def descadastrar_pessoa(self, agencia, contas, lista_self):   # 4.3.1.3_
        print('4.3.1.3_')
        while True:
            confirmacao = input(f'Confirma exclusão de {self.valor_dado_variavel}?\n'
            f'{self.lista_pessoa[self.opcao_pessoa][self.indice_pessoa][self.valor_dado_variavel]}\n'
            f'\nSim (1) Não(2)\n')

            if confirmacao != '1' and confirmacao != '2':
                print('\nDigite uma opção válida.\n')
                continue
            elif confirmacao == '1':

                del self.lista_pessoa[self.opcao_pessoa][self.indice_pessoa]
                print(f'\n{self.valor_dado_variavel} foi descadastrado\n')

                with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)
                
                from modulo_pessoa.modulo_lista_pessoa import Lista
                Lista.direcionamento(self, agencia, contas, lista_self)

            else:
                return

    def direcionamento(self, agencia, contas, lista_self):   # 4.3.1.4_
        print('4.3.1.4_')
        while True:
            direcionamento = input(f'\n{self.classe_nome}\n\np_ Contas (1) / {self.classe_nome} (2):\n')
            if direcionamento != '1' and direcionamento != '2':
                print('Digite uma opção válida.\n')
                continue

            if direcionamento == '1':
                agencia['valor_agencia'] = self.valor_agencia

                from modulo_contas.modulo_contas import Contas
                Contas(agencia).menu_opcao(agencia, lista_self)
            else:
                contas['valor_agencia'] = self.valor_agencia

                from modulo_pessoa.modulo_pessoa import Pessoa
                Pessoa(contas).menu_opcao(agencia, contas, lista_self)
