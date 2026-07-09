import json, sys, os


class Lista:   # 2.3.0_
    print('2.3.0_')
    """
        A função lista_autenticacao possui 2 formas de autenticação:
        primeiro acesso (não possui nenhum usuário cadastrado): será cadastrado na
        lista_acesso_0001.json. Os usuários da agência matriz possuem permissão de administrador,
        entrarão no except do Lista.lista_autenticacao e serão direcionados para o 
        modulo_matriz.modulo_menu_matriz.Menu.menu_opcao;
        segundo acesso em diante: todos passarão por processo de autenticação de matrícula e senha.
        Usuários da agência matriz possuem permissão de administrador e serão direcionados para o 
        menu da agência matriz. Usuários de outras agências serão direcionados para o 
        modulo_menu_agencia, classe Menu, função menu_opcao com permissão de usuário de suas 
        respectivas agências"""

    def lista_autenticacao(self, lista_self):   # 2.3.1_
        print('2.3.1_')
        senha_autenticacao = False
        """
            self.usuario_autenticado é o usuário da agência matriz ou com perfil de 
            administrador autenticado através do menu da agência matriz.
            Solicita acesso ao menu de uma agência filial, definida na variável 
            valor_agencia_filial. O acesso será concedido aos usuários cadastrados
            nas listas de acesso de cada agência.
            Erro de autenticação será solicitada nova tentativa de autenticação.
            Erro de agência não cadastrada, será direcionado para a função lista_usuario.
            Na primeira autenticação o valor_agencia_filial é None gerando erro e entrando no except."""

        for dados_acesso in self.lista_acesso:
            for matricula_acesso, dados_matricula in dados_acesso.items():
                if matricula_acesso == self.valor_matricula:
                    if dados_matricula.get(self.senha, ) == self.valor_senha:
                        senha_autenticacao = True
                        break
                if senha_autenticacao is True:
                    break
            if senha_autenticacao is True:
                break

        with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

        if senha_autenticacao is True:
            self_matriz = lista_self.get('self_matriz', )
            self.valor_matricula_autenticada = self.valor_matricula
            self.valor_senha_autenticada = self.valor_senha

            print(f'\nUsuário_ {self.matricula} {self.valor_matricula} autenticado com sucesso.')

            if self_matriz is not None:

                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, self.__dict__, lista_self)

            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.menu_opcao(self, lista_self)

        print(f'\nA {self.senha} ou a {self.matricula}__ está errada\n')

        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_autenticacao(self, lista_self)

    def lista_usuario(self, lista_self):   # 2.3.2_
        print('2.3.2_')
        cadastro_usuario = False
        descadastro_usuario = False 
        """
            Na primeira autenticação será criada a lista_acesso_0001 definida na variável
            self.lista_acesso no modulo_agencia_0001, classe Agencia, função __init__.
            A lista_acesso_0001 depois de gerada não permite ficar sem pelo menos um usário."""

        try:
            with open(self.lista_acesso_json, 'r+', encoding='utf8') as arquivo:
                self.lista_acesso = json.load(arquivo)
        except:
            self.lista_acesso = []
            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)
            self.primeira_autenticacao = True

        for indice_lista, dados_lista in enumerate(self.lista_acesso):
            for matricula_lista, dados_usuario in dados_lista.items():
                if matricula_lista == self.valor_matricula:
                    if self.opcao == 'cadastrar':
                        cadastro_usuario = True
                        break
                    elif self.opcao == 'descadastrar':
                        descadastro_usuario = True
                        break
                if cadastro_usuario is True or descadastro_usuario is True:
                    break
            if cadastro_usuario is True or descadastro_usuario is True:
                break
        """
            Na primeira autenticação cadastro_usuario is False and self.opcao == 'cadastrar'
            self.lista_acesso cadastrará o primeiro usuário que terá perfil de administrador."""

        if cadastro_usuario is False and self.opcao == 'cadastrar':

            if self.primeira_autenticacao is True:
                self.valor_matricula_autenticada = self.valor_matricula
                self.valor_senha_autenticada = self.valor_senha

            self.lista_acesso.append({self.valor_matricula: {self.senha: self.valor_senha, self.matricula: self.valor_matricula}})

            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

            self_matriz = lista_self.get('self_matriz')
            """
                Na primeira autenticação: self_matriz is not None and self.valor_agencia == "0001" and 
                self.primeira_autenticacao is True"""

            if self_matriz is not None and self.valor_agencia == "0001" and self.primeira_autenticacao is True:
                self.primeira_autenticacao = False
                self.valor_senha_autenticada = self.valor_senha
                print(f'\nUsuário__ {self.matricula} {self.valor_matricula} cadastrado e autenticado com sucesso.\n')
                print(self.lista_acesso[-1])

                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, self.__dict__, lista_self)

            print(f'\nUsuário {self.matricula} {self.valor_matricula} cadastrado com sucesso.\n')
            print(self.lista_acesso[-1])

        elif cadastro_usuario is True and self.opcao == 'cadastrar':
            print(f'\nO usuário {self.matricula} {self.valor_matricula} já foi cadastrado.')

            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

        elif descadastro_usuario is False and self.opcao == 'descadastrar':
            print(f'\nNão existe usuário {self.matricula} {self.valor_matricula}.')

            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

        elif descadastro_usuario is True and self.opcao == 'descadastrar':
            encerrar = None
            self_matriz = lista_self.get('self_matriz')

            if self_matriz is not None and self.valor_matricula_autenticada == self.valor_matricula:

                print('\nSe descadastrar sua matrícula a seção será encerrada.')

                while True:
                    encerrar = input('Continuar Sim (1) Não (2):\n')
                    if encerrar != '1' and encerrar != '2':
                        print('Digite uma opção válida.\n')
                        continue

                    elif encerrar == '1' and len(self.lista_acesso) == 1:
                        self_matriz = lista_self.get('self_matriz')

                        os.remove(self.lista_acesso_json)

                        print(f'\n__{self.matricula} {self.valor_matricula} foi descadastrada.\n')

                        sys.exit('\nO sistema está sendo finalizado.\n')

                    elif encerrar == '2':
                        from modulo_agencia.modulo_menu_agencia import Menu
                        Menu.menu_opcao(self, lista_self) 

                    break

            del self.lista_acesso[indice_lista]

            print(f'\n{self.matricula} {self.valor_matricula} foi descadastrada.\n')
            print(self.lista_acesso)

            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

            if encerrar == '1':
                sys.exit('\nO sistema está sendo finalizado.\n')

        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_opcao(self, lista_self)
