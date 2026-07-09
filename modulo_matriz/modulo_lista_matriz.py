import json


class Lista:   # 1.3.0_
    print('1.3.0_')
    def acesso_filial(self, agencia, lista_self):   # 1.3.1_
        print('1.3.1_')

        try:
            with open(self.lista_boa_vista_bank_json, 'r+', encoding='utf8') as arquivo:
                self.lista_agencia = json.load(arquivo)
        except:
            with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

        if self.valor_agencia_filial in self.lista_agencia:

            with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

            self_matriz = lista_self.get('self_matriz', )

            if self_matriz is not None:
                if self.opcao == 'filial':

                    from modulo_agencia_matriz import Matriz
                    Matriz(self.valor_agencia_filial).menu_self(True)

                elif self.opcao == 'transferir':
                    self.valor_agencia_transferir = self.valor_agencia_filial

                    from modulo_contas.modulo_menu_contas import Menu
                    Menu.cadastrar_contas(self, agencia, lista_self)

            self.valor_agencia_transferir = self.valor_agencia_filial

            from modulo_contas.modulo_menu_contas import Menu
            Menu.cadastrar_contas(self, agencia, lista_self)
        else:
            print(f'\n{self.valor_agencia_filial} não é um número de agência válido.')

            self_matriz = lista_self.get('self_matriz', )

            if self_matriz is not None:

                while True:
                    confirmacao = input(f'\nDeseja cadastrar agência {self.valor_agencia_filial}:\nSim (1) / Não (2)\n')
                    # confirmacao = '1'
                    # print(confirmacao)
                    if confirmacao == '0' or confirmacao == '2':

                        with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
                            json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

                        if self_matriz is not None:

                            from modulo_matriz.modulo_menu_matriz import Menu
                            Menu.menu_opcao(self, agencia, lista_self)

                        self_contas = lista_self.get('self_contas', )

                        from modulo_contas.modulo_menu_contas import Menu
                        Menu.menu_opcao(self_contas, agencia, lista_self)

                    elif confirmacao != '1' and confirmacao != '2':
                        print('\nDigite uma opcão válida.\n')
                        continue
                    break

                from modulo_matriz.modulo_lista_matriz import Lista
                Lista.cadastrar_agencia(self, agencia, lista_self)

            with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self, agencia, lista_self)

    def cadastrar_agencia(self, agencia, lista_self):   # 1.3.2_
        print('1.3.2_')

        valor_agencia = int(self.lista_agencia[-1])
        valor_agencia += 1
        valor_agencia = str(valor_agencia)
        valor_agencia = valor_agencia.zfill(4)

        self.lista_agencia.append(valor_agencia)

        with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

        modulo_agencia_valor = f'modulo_agencia_{valor_agencia}.py'

        with open(modulo_agencia_valor, 'w+', encoding='utf8') as arquivo:
            arquivo.writelines(('class Agencia:\n', '    def __init__(self, valor_agencia):\n',
            '        self.valor_agencia = valor_agencia\n', '        self.classe_nome = "Agência"\n',
            '        self.lista_acesso_json = f"lista_acesso_{self.valor_agencia}.json"\n',
            '        self.lista_acesso = []\n', '        self.valor_matricula = None\n',
            '        self.matricula = "Matrícula"\n', '        self.valor_senha = None\n',
            '        self.senha = "Senha"\n', '        self.opcao = None\n', '        self.self_agencia = self\n\n',
            '    def menu_self(self, self_matriz, valor_agencia_filial):\n', '        self_agencia = self.self_agencia\n\n',
            '        if self_matriz is not None:\n', '            lista_self = {"self_matriz": self_matriz, "self_agencia": self_agencia}\n\n',
            '        else:\n\n', '            lista_self = {"self_agencia": self_agencia}\n\n',
            '        from modulo_contas.modulo_contas import Contas\n', '        Contas(self.__dict__).menu_self(lista_self, valor_agencia_filial)\n\n',
            '    def menu_opcao(self, lista_self):\n\n', '        from modulo_agencia.modulo_menu_agencia import Menu\n',
            '        Menu.menu_opcao(self, lista_self)\n', '\n', '\n', 'if __name__ == "__main__":\n',
            f'    Agencia("{valor_agencia}").menu_self(None, None)\n'
                                ))

        print(f'\nAgência {valor_agencia} foi criada.')
        print(f'{self.lista_agencia}\n')

        try:
            lista_conta_json = f'lista_conta_{valor_agencia}.json'
            lista_contas = [[], []]

            with open(lista_conta_json, 'r+', encoding='utf8') as arquivo:
                lista_contas = json.load(arquivo)
        except:
            with open(lista_conta_json, 'w+', encoding='utf8') as arquivo:
                json.dump(lista_contas, arquivo, ensure_ascii=False, indent=2)

            print(f'\nLista Conta {valor_agencia} foi criada.')
            print(lista_contas)

        try:
            lista_pessoa_json = f'lista_pessoa_{valor_agencia}.json'
            lista_pessoa = [[], []]

            with open(lista_pessoa_json, 'r+', encoding='utf8') as arquivo:
                lista_pessoa = json.load(arquivo)
        except:
            with open(lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
                json.dump(lista_pessoa, arquivo, ensure_ascii=False, indent=2)

            print(f'\nLista Pessoa {valor_agencia} foi criada.')
            print(lista_pessoa)

        self_matriz = lista_self.get('self_matriz', )

        if self_matriz is not None:

            if self.opcao == 'filial':

                from modulo_agencia_matriz import Matriz
                Matriz(self.valor_agencia_filial).menu_self(True)

            elif self.opcao == 'transferir':
                self.valor_agencia_transferir = self.valor_agencia_filial

                from modulo_contas.modulo_menu_contas import Menu
                Menu.cadastrar_contas(self, agencia, lista_self)

        from modulo_matriz.modulo_menu_matriz import Menu
        Menu.menu_opcao(self, agencia, lista_self)
