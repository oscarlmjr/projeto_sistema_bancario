import json

print('1.3.0_')
class Lista:   # 1.3.1.0_
    print('1.3.1.0_')
    def acesso_filial(self, agencia, lista_self):   # 1.3.1.1_
        print('1.3.1.1_')
        try:
            with open(self.lista_boa_vista_bank_json, 'r+', encoding='utf8') as arquivo:
                self.lista_agencia = json.load(arquivo)
                if self.lista_agencia is None:
                    self.lista_agencia = ['0001']

        except: 
            with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

            print(f'\nA opção "Filial (3)" está indisponível no momento.')

            from modulo_matriz.modulo_menu_matriz import Menu
            Menu.menu_opcao(self, agencia, lista_self)

        if self.valor_agencia_filial in self.lista_agencia:
            self_agencia = lista_self.get('self_agencia', )

            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.menu_autenticacao(self_agencia, lista_self, self.valor_agencia_filial)

        print(f'\n{self.valor_agencia_filial} não é um número de agência válido.')

        from modulo_matriz.modulo_menu_matriz import Menu
        Menu.menu_opcao(self, agencia, lista_self)

    def cadastrar_agencia(self, agencia, lista_self):   # 1.3.1.2_
        print('1.3.1.2_')
        try:
            with open(self.lista_boa_vista_bank_json, 'r+', encoding='utf8') as arquivo:
                self.lista_agencia = json.load(arquivo)
                if self.lista_agencia is None:
                    self.lista_agencia = ['0001']
        except:
            with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

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
            '        self.lista_acesso = []\n', '        self.lista_transferencia_json = "lista_transferencia.json"\n',
            '        self.lista_transferencia = []\n', '        self.valor_matricula = None\n',
            '        self.matricula = "Matrícula"\n', '        self.valor_senha = None\n',
            '        self.senha = "Senha"\n', '        self.opcao = "cadastrar"\n', 
            '        self.usuario_autenticado = None\n\n', '        self.modulo_menu_matriz = "modulo_menu_matriz"\n',
            '        self.modulo_menu_agencia = "modulo_menu_agencia"\n', '        self.modulo_lista_agencia = "modulo_lista_agencia"\n',
            '        self.modulo_contas = "modulo_contas"\n\n', '        self.self_agencia = self\n\n',
            '    def menu_self(self, self_matriz):\n', '        self_agencia = self.self_agencia\n\n',
            '        if self_matriz is not None:\n', '            lista_self = {"self_matriz": self_matriz, "self_agencia": self_agencia}\n\n',
            '        else:\n', '            lista_self = {"self_agencia": self_agencia}\n\n',
            '        from modulo_contas.modulo_contas import Contas\n', '        Contas(self.__dict__).menu_self(lista_self)\n\n',
            '    def menu_opcao(self, lista_self):\n\n', '        from modulo_agencia.modulo_menu_agencia import Menu\n',
            '        Menu.menu_opcao(self, lista_self)\n', '\n', '\n', 'if __name__ == "__main__":\n',
            f'    Agencia("{valor_agencia}").menu_self(None)\n'
                                ))

        print(f'\nAgência {valor_agencia} foi criada.')
        print(self.lista_agencia)

        from modulo_matriz.modulo_menu_matriz import Menu
        Menu.menu_opcao(self, agencia, lista_self)
