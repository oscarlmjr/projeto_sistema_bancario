import sys, json


class Menu:
    
    def menu_opcao(self, agencia, lista_self):   # 
        classe_nome = agencia['classe_nome']
        self_matriz = lista_self.get('self_matriz', )
        
        while True:

            print(f'\nBoa Vista Bank\n{classe_nome} {self.valor_agencia}\n{self.classe_nome}\n')

            if self_matriz is not None:

                opcao = input('Listar (1) / Cadastrar (2) / Retornar ocorrências (3) / Transferir (4)'
                                f' / Descadastrar (5)\nPessoa (6) / Agência (7) / Matriz (8) / Sair (9):\n')            
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' \
                and opcao != '7' and opcao != '8' and opcao != '9':
                    print('Digite uma opção válida.')
                    continue  
            else:
                opcao = input('Listar (1) / Cadastrar (2) / Retornar ocorrências (3) / Transferir (4)'
                                f' / Descadastrar (5)\nPessoa (6) / Agência (7) / Sair (8):\n')
            
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' \
                and opcao != '7' and opcao != '8':
                    print('Digite uma opção válida.')
                    continue  

            if opcao == '1':
                self.opcao = 'Listar'
            elif opcao == '2':
                self.opcao = 'Cadastrar'
            elif opcao == '3':
                self.opcao = 'Ocorrencias'
            elif opcao == '4':
                self.opcao = 'Transferir'
            elif opcao == '5':
                self.opcao = 'Descadastrar'
            elif opcao == '6': 
                from modulo_pessoa.modulo_pessoa import Pessoa
                Pessoa(self.__dict__).menu_opcao(agencia, self.__dict__, lista_self)

            elif opcao == '7': 
                from modulo_agencia_matriz import Matriz
                Matriz(self.valor_agencia).menu_agencia(lista_self)
            
            elif self_matriz is not None and opcao == '8':
                from modulo_matriz.modulo_menu_matriz import Menu
                Menu.menu_opcao(self_matriz, agencia, lista_self)

            elif opcao == '8' or opcao == '9':
                from modulo_contas.modulo_menu_contas import Menu  
                Menu.saida()
            
            if self.opcao == 'Ocorrencias' or self.opcao == 'Transferir':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_acao(self, agencia, lista_self)
                
            digito_conta = input(f'\n{self.conta_corrente} (1) / {self.conta_poupanca} (2):\n')

            if digito_conta != '1' and digito_conta != '2':
                    print('\nDigite uma opção válida.')
                    continue
            
            if digito_conta == '2':
                self.digito_conta = '2'
                self.conta_variavel = self.conta_poupanca 

            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_acao(self, agencia, lista_self)
            
    def menu_acao(self, agencia, lista_self):       
            
        print('\nMenu (0)')

        if self.opcao == 'Listar':
            print(f'{self.opcao}')

            while True: 

                if self.conta_variavel is self.conta_poupanca: 
                        
                    self.valor_dado_variavel = input(f'\nDigite o {self.dado_variavel}:\n') 
                    if self.valor_dado_variavel == '0':
                        ...
                    else:
                        self.valor_conta_variavel = input(f'\n{self.nome_conta}:\n')
                else: 
                    from modulo_contas.modulo_menu_contas import Menu
                    Menu.teste_dado_variavel(self, agencia, lista_self)

                    if self.valor_dado_variavel == '0':
                        ...
                    else:
                        self.valor_conta_variavel = input(f'\n{self.nome_conta}:\n')                
                break

        elif self.opcao == 'Cadastrar':  
            print(f'{self.opcao}')
            
            while True:  
                if self.conta_variavel is self.conta_poupanca:
                    
                    self.valor_dado_variavel = input(f'\nDigite o {self.dado_variavel}:\n')
                    
                else:
                    from modulo_contas.modulo_menu_contas import Menu
                    Menu.teste_dado_variavel(self, agencia, lista_self) 

                confirmacao = input('\nConfirma a criação da conta para os dados informados: Sim (1) / Não (2)\n')
                
                if confirmacao != '1' and confirmacao != '2':
                    print('\nDigite uma opção válida.\n')
                    continue
                if confirmacao == '2':
                    self.valor_dado_variavel = '0'
                    break

                try:                
                    with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
                        self.lista_contas = json.load(arquivo)    
                        if self.lista_contas is None:
                            self.lista_contas = [[], []]                     
                except:
                    
                    with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
                        json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)  
                try:
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
                        self.valor_conta_variavel = conta_variavel.rjust(5, '1')

                    else:    
                        conta_variavel = int(conta_variavel[-1])
                        conta_variavel += 1
                        conta_variavel = str(conta_variavel)
                        self.valor_conta_variavel = '2' + conta_variavel.rjust(4, '1')
                except:
                    
                    if self.opcao_conta == 0:
                        self.valor_conta_variavel = '1111' + self.digito_conta
                    else:
                        self.valor_conta_variavel = '21111'
                        
                break                    

        elif self.opcao == 'Ocorrencias' or self.opcao == 'Transferir':                 
            print(f'{self.opcao}')
            
            from modulo_contas.modulo_menu_contas import Menu
            Menu.teste_dado_variavel(self, agencia, lista_self)

            if self.opcao == 'Transferir':                
                print('\nMenu (0)\n')

                while True:
                    agencia_transferir = input('Digite o número da agência para a qual deseja transferir:\n')  
                    
                    if agencia_transferir == self.valor_agencia:
                        print('Você não pode transferir para a mesma agência.')
                        continue
                    elif agencia_transferir == '0':

                        from modulo_contas.modulo_menu_contas import Menu
                        Menu.menu_opcao(self, agencia, lista_self)

                    self.agencia_transferir = agencia_transferir

                    try:
                        with open(self.lista_boa_vista_bank_json, 'r+', encoding='utf8') as arquivo:
                            self.lista_agencia = json.load(arquivo)    
                            if self.lista_agencia is None:
                                self.lista_agencia = ['0001']        

                        if self.agencia_transferir in self.lista_agencia:
                            break
                        else:                    
                            print(f'\n{self.agencia_transferir} não é um número de agência válido\n')
                    except:        
                        print(f'\nA opção "Transferir (4)" está indisponível no momento.\n')

                    break
                            
        elif self.opcao == 'Descadastrar':                
            print(f'{self.opcao}')
            
            while True:          

                self.valor_conta_variavel = input(f'\n{self.nome_conta}:\n')
                
                if self.valor_conta_variavel[0] == '2':
                    self.opcao_conta = 1

                break

        Menu.teste_valor_dado(self, agencia, lista_self)

    def teste_dado_variavel(self, agencia, lista_self):
         
         while True:          

            dado_valor = input(f'\n{self.dado_variavel} (1) {self.dado_cnpj} (2):\n')
            if dado_valor == '0':
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            if dado_valor != '1' and dado_valor != '2':
                print('\nDigite uma opção válida.\n')
                continue 
            self.dado_valor = dado_valor
            if self.dado_valor == '1':
                self.valor_dado_variavel = input(f'\nDigite o {self.dado_variavel}:\n')
            elif self.dado_valor == '2':
                self.dado_variavel = self.dado_cnpj
                self.opcao_conta = 1
                self.valor_dado_variavel = input(f'\nDigite o {self.dado_variavel}:\n')

            break

    def teste_valor_dado(self, agencia, lista_self):
        
        if self.valor_dado_variavel == '0' or self.dado_valor == '0':
            from modulo_contas.modulo_menu_contas import Menu
            Menu.menu_opcao(self, agencia, lista_self)
        
        from modulo_contas.modulo_lista_contas import Lista
        Lista.listar_acao(self, agencia, lista_self)
    
        
    def saida():
    
        sys.exit('\nO sistema está sendo finalizado.\n')
        