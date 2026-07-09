import json, sys, os


class Lista:   # _5.2.0

    """
        A função lista_autenticacao possui 2 formas de autenticação:
        primeiro acesso (não possui nenhum usuário cadastrado): será cadastrado na
        lista_acesso_0001.json. Os usuários da agência matriz possuem permissão de administrador
        e serão direcionados para o modulo_agencia_matriz, classe Matriz, função menu_agencia.
        Segundo acesso em diante: todos passarão por processo de autenticação de matrícula e senha,
        usuários da agência matriz serão direcionados para o menu da agência matriz, citado acima.
        usuários de outras agências serão direcionados para o modulo_menu_agencia, classe Menu, 
        função menu_opcao com permissão de usuário de suas respectivas agências"""

    def lista_autenticacao(self, lista_self, valor_agencia_filial):   # _5.2.1
        self_matriz = lista_self.get('self_matriz', )
        senha_autenticacao = False
        matricula_autenticacao = False

        """
            self.usuario_autenticado é o usuário da agência matriz ou com perfil de 
            administrador que já foi autenticado e através do menu da agência matriz,
            solicita acesso ao menu de uma agência filial, definida na variável 
            valor_agencia_filial. O acesso será concedido aos usuários cadastrados
            nas listas de acesso de cada agência.
            Erro de autenticação será solicitada nova tentativa de autenticação.
            Erro de agência não cadastrada, será direcionado para a função lista_usuario.
            Na primeira autenticação o valor_agencia_filial é None gerando erro e entrando no except."""
            
        try:
            if self.usuario_autenticado is True:
                self.lista_acesso_json = f'lista_acesso_{valor_agencia_filial}.json'

            with open(self.lista_acesso_json, 'r+', encoding='utf8') as arquivo:
                lista_acesso = json.load(arquivo)
                
            for dados_acesso in lista_acesso:                    
                for matricula_acesso, dados_matricula in dados_acesso.items():                        
                    if matricula_acesso == self.valor_matricula_acesso:
                        matricula_autenticacao = True
                        if dados_matricula.get(self.senha, ) == self.valor_senha_acesso:
                            senha_autenticacao = True
                            break
                        else:
                            print(f'{self.senha} {self.valor_senha_acesso}_ está errada')
                    if senha_autenticacao is True:
                        break
                if senha_autenticacao is True:
                    break  
        except:
            
            if self_matriz is not None:  
                self.valor_matricula = self.valor_matricula_acesso
                self.valor_senha = self.valor_senha_acesso                
                Lista.lista_usuario(self, lista_self)  
        
        if senha_autenticacao is True:

            if self_matriz is not None:

                if self.usuario_autenticado is True:
                        
                    print(f'\nUsuário_ {self.matricula} {self.valor_matricula_acesso} autenticado com sucesso.')
                    from modulo_agencia_matriz import Matriz
                    Matriz(valor_agencia_filial).menu_agencia(lista_self) 

                elif valor_agencia_filial is not None:
                    Lista.lista_usuario(self, lista_self, valor_agencia_filial)
                                
                print(f'\nUsuário_ {self.matricula} {self.valor_matricula_acesso} autenticado com sucesso.')
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, self.__dict__, lista_self) 
            
            print(f'\nUsuário_ {self.matricula} {self.valor_matricula_acesso} autenticado com sucesso.')
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.menu_opcao(self, lista_self)

        if matricula_autenticacao == False:
            print(f'{self.matricula} {self.valor_matricula_acesso}__ está errada')
        
        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_autenticacao(self, lista_self, valor_agencia_filial)
    
    def lista_usuario(self, lista_self, valor_agencia_filial=None):   # _5.2.2
        cadastro_usuario = False
        descadastro_usuario = False

        """
            Na primeira autenticação o valor_agencia_filial é None gerando erro e entrando no except."""
                
        try:
            if valor_agencia_filial is not None:
                self.lista_acesso_json = f'lista_acesso_{valor_agencia_filial}.json'                
                self.valor_matricula = self.valor_matricula_acesso
                self.valor_senha = self.valor_senha_acesso   

            with open(self.lista_acesso_json, 'r+', encoding='utf8') as arquivo:
                self.lista_acesso = json.load(arquivo)   

            lista_acesso = True
            
        except:
            
            """
                Na primeira autenticação será criada a lista_acesso_0001 definida na variável
                self.lista_acesso no modulo_agencia_0001, classe Agencia, função __init__.
                A lista_acesso_0001 depois de gerada não permite ficar sem pelo menos um usário."""
            
            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)
                
            lista_acesso = None
            
        if lista_acesso is True:
            
            for indice_lista, dados_lista in enumerate(self.lista_acesso):
                for matricula_lista, dados_usuario in dados_lista.items():
                    if matricula_lista == self.valor_matricula:
                        if self.opcao == 'cadastrar':
                            cadastro_usuario = True
                            print(f'\nO usuário {self.matricula} {self.valor_matricula} já foi cadastrado.')
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
            print('\nCadastrar')
            
            self.lista_acesso.append({self.valor_matricula: {self.senha: self.valor_senha, self.matricula: self.valor_matricula}})

            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

            self_matriz = lista_self.get('self_matriz')

            """
                Na primeira autenticação: self_matriz is not None and len(self.lista_acesso) == 1"""
            if self_matriz is not None and len(self.lista_acesso) == 1:  
                print(f'\nUsuário__ {self.matricula} {self.valor_matricula} cadastrado e autenticado com sucesso.\n')
                print(self.lista_acesso[-1])

                if valor_agencia_filial is not None:                        
                    """
                        Na primeira autenticação: valor_agencia_filial is None.
                        Primeira autenticação concluída e direcionando para o modulo_menu_matriz, Classe Menu,
                        função menu_opcao"""
                    
                    from modulo_agencia_matriz import Matriz
                    Matriz(valor_agencia_filial).menu_agencia(lista_self)
                
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, self.__dict__, lista_self)
                                
            print(f'\nUsuário {self.matricula} {self.valor_matricula} cadastrado com sucesso.\n')
            print(self.lista_acesso[-1])
        
        elif descadastro_usuario is False and self.opcao == 'descadastrar':
            print(f'\nNão existe usuário {self.matricula} {self.valor_matricula}.')

        elif descadastro_usuario is True and self.opcao == 'descadastrar':
            encerrar = None

            if self.valor_matricula == self.valor_matricula_acesso:

                print('\nSe descadastrar sua matrícula a seção será encerrada.')
                
                while True:
                    encerrar = input('Continuar Sim (1) Não (2):\n')
                    if encerrar != '1' and encerrar != '2':
                        print('Digite uma opção válida.')
                        continue    

                    elif encerrar == '1' and len(self.lista_acesso) == 1:
                        self_matriz = lista_self.get('self_matriz')

                        os.remove(self.lista_acesso_json)

                        print(f'__{self.matricula} {self.valor_matricula} foi descadastrado.')
                        print(self.lista_acesso)

                        from modulo_agencia_matriz import Matriz
                        Matriz(self_matriz.valor_agencia).menu_self() 

                    elif encerrar == '2':
                        from modulo_agencia.modulo_menu_agencia import Menu
                        Menu.menu_opcao(self, lista_self) 
                        
                    break
                
            del self.lista_acesso[indice_lista]
            print(f'{self.matricula} {self.valor_matricula} foi descadastrado.')
            print(self.lista_acesso)                
            
            with open(self.lista_acesso_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_acesso, arquivo, ensure_ascii=False, indent=2)

            if encerrar == '1':
                self_matriz = lista_self.get('self_matriz')
                
                from modulo_agencia_matriz import Matriz
                Matriz(self_matriz.valor_agencia).menu_self()
                # sys.exit('\nO sistema está sendo finalizado.\n')
        
        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_opcao(self, lista_self)  
        