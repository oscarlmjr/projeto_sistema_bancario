import json


class Lista:

    def __init__(self, lista_menu_contas, lista_acao_contas, lista=None):    
        self.t = lista_acao_contas['t']  
        self.opcao = lista_acao_contas['opcao']      
        if self.t is False or self.opcao == 'transferir' or self.opcao == 'ocorrencias':
            self.agencia = lista_menu_contas['agencia']
            self.lista_transferencia = lista_menu_contas['lista_transferencia']
            self.lista_json_transferencia = lista_menu_contas['lista_json_transferencia']
            self.saldo = lista_menu_contas['saldo']
            self.valor_saldo = lista_menu_contas['valor_saldo']
            self.extrato = lista_menu_contas['extrato']
            self.valor_extrato = lista_menu_contas['valor_extrato']
            self.debito = lista_menu_contas['debito']
            self.valor_debito =lista_menu_contas['valor_debito']
            self.credito = lista_menu_contas['credito']
            self.valor_credito = lista_menu_contas['valor_credito'] 

        self.numero_agencia = lista_menu_contas['numero_agencia']
        self.classe = lista_menu_contas['classe']
        self.classe_nome = lista_menu_contas['classe_nome']
        self.classe_funcao = lista_menu_contas['classe_funcao']        
        self.tipo_variavel = lista_menu_contas['tipo_variavel']
        self.lista_json_variavel = lista_menu_contas['lista_json_variavel']           
        self.lista_variavel = lista_menu_contas['lista_variavel']
        self.valor_variavel = lista_acao_contas['valor_variavel']
        self.dado = lista_acao_contas['dado']
        self.dado_2 = lista_acao_contas['dado_2']
        self.dado_3 = lista_acao_contas['dado_3']
        self.valor_dado = lista_acao_contas['valor_dado']
        self.valor_dado_2 = lista_acao_contas['valor_dado_2']
        self.valor_dado_3 = lista_acao_contas['valor_dado_3']
        self.n = lista_acao_contas['n']
        self.e = lista_acao_contas['e']
        self.f = lista_acao_contas['f']

        Lista.listar_variavel(self, lista_menu_contas, lista)

    def listar_variavel(self, lista_menu_contas, lista):

        if self.opcao == 'transferir': 
            lista_variavel = []

        try:    
            with open(self.lista_json_variavel, 'r+', encoding='utf8') as arquivo:
                self.lista_variavel = json.load(arquivo)    
                if self.lista_variavel is None:
                    self.lista_variavel = [[], []]                    
        except:
            self.lista_variavel = [[], []]    # (?)
            with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)

        if self.t is False:
            Lista.cadastrar_variavel(self, lista)
        
        while True:             
            
            for self.e, p in enumerate(self.lista_variavel[self.n]):
                for c, v in p.items():                                                     
                    if self.opcao == 'ocorrencias' or self.opcao == 'transferir':                              
                        if v.get(self.dado, ) == self.valor_dado:
                            if c[0] == '2' or c[-1] == '1':
                                print(f'\nv = {v}')
                            elif c[0] == '1' and c[-1] == '2':
                                print(f'\nv_ = {v}')
                            self.t = False
                            if self.opcao == 'transferir':
                                self.lista_transferencia.append(p)
                                self.t = False
                        elif self.opcao == 'transferir':
                            lista_variavel.append(p)
                                                                                                      
                    elif v.get(self.dado, ) == self.valor_dado:
                        self.f = False
                        break          
                if self.f == False:
                    break
            if self.opcao == 'transferir' and self.t is False:
                self.lista_variavel[self.n] = lista_variavel                                                              
                with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)                                 
            break  
        
        if self.opcao == 'listar' and self.f is False:
            print(f'\nlistar_ {self.valor_dado} possue cadastro.')
            print(self.lista_variavel[self.n][self.e][self.numero_agencia], '\n')         
        elif self.opcao == 'listar' and self.f is True:
            print(f'\nlistar_2 {self.valor_dado} não possui cadastro')            
            
            from modulo_pessoa import Pessoa
            Pessoa().listar_menu(self.__dict__)

        elif self.opcao == 'cadastrar' and self.f is False:                
            print(f'\ncadastrar_ {self.dado} {self.valor_dado} já possui cadastro.\n')
            print(self.lista_variavel[self.n][self.e][self.numero_agencia], '\n')
        elif self.opcao == 'cadastrar' and self.f is True:
            print(f'\ncadastrar_2 {self.dado} {self.valor_dado} não possui cadastro.')

            import modulo_pessoa
            modulo_pessoa.Pessoa().listar_menu(self.__dict__)

        elif self.opcao == 'ocorrencias' and self.t is False or self.opcao == 'transferir' and self.t is False:
            print(f'\nTodas as ocorrências encontradas para {self.valor_dado}.')
            if self.opcao == 'transferir':
                print(f'\nTransferindo\n')
                import modulo_lista_contas
                modulo_lista_contas.Lista.transferir_variavel(self)

        elif self.opcao == 'ocorrencias' and self.t is True or self.opcao == 'transferir' and self.t is True:
            print(f'\n{self.valor_dado} não possui nenhuma ocorrência.')
        
        elif self.opcao == 'descadastrar' and self.f is False:
            print(f'Descadastrando: {self.valor_dado}\n')
            import modulo_lista_contas
            modulo_lista_contas.Lista.descadastrar_variavel(self)  
        elif self.opcao == 'descadastrar' and self.f is True:
            print(f'descadastrar {self.valor_dado} não possui cadastro.')   
        
        from modulo_agencia import Agencia
        return Agencia().contas_opcao()
        
        
    def cadastrar_variavel(self, lista):

        lista_cadastrar = {self.dado: self.valor_dado, 
                           self.agencia: self.numero_agencia, self.tipo_variavel: self.valor_variavel,
                           self.saldo: self.valor_saldo, self.extrato: self.valor_extrato, 
                           self.debito: self.valor_debito, self.credito: self.valor_credito}  

        for chave, valor in lista.items():
            lista_cadastrar[chave] = valor

        lista_cadastrar = {self.numero_agencia: lista_cadastrar}

        self.lista_variavel[self.n].append(lista_cadastrar)

        with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2) 

            print(f'{self.valor_variavel} {self.valor_dado}_ cadastrado com sucesso_.\n')
            print(f'{self.lista_variavel[self.n][-1][self.numero_agencia]}\n')

        Lista.direcionamento(self) 
            
    def transferir_variavel(self):  
        
        try:    
            with open(self.lista_json_transferencia, 'r+', encoding='utf8') as arquivo:
                lista_transferencia = json.load(arquivo)    
                if lista_transferencia is None:
                    lista_transferencia = []                    
        except:
            lista_transferencia = [] 
            with open(self.lista_json_transferencia, 'w+', encoding='utf8') as arquivo:
                json.dump(lista_transferencia, arquivo, ensure_ascii=False, indent=2)
     
        for _ in self.lista_transferencia:
           lista_transferencia.append(_)

        with open(self.lista_json_transferencia, 'w+', encoding='utf8') as arquivo:
            json.dump(lista_transferencia, arquivo, ensure_ascii=False, indent=2)

    def descadastrar_variavel(self):

        while True:          

            confirmacao = input(f'Confirma exclusão de {self.valor_dado}?\n'
            f'{self.lista_variavel[self.n][self.e][self.numero_agencia]}\n'
            f'\nSim (1) Não(2)\n')

            if confirmacao != '1' and confirmacao != '2':
                print('\nDigite uma opção válida.\n')
                continue
            elif confirmacao == '1':

                with open(self.lista_json_variavel, 'r+', encoding='utf8') as arquivo:
                    self.lista_variavel = json.load(arquivo)    
                    if self.lista_variavel is None:
                        self.lista_variavel = [[], []]
                 
                del self.lista_variavel[self.n][self.e]
                print(f'\n{self.valor_dado} foi descadastrado\n')
                
                with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)

                Lista.direcionamento(self)
            
            else:
                import modulo_agencia
                modulo_agencia.Agencia().contas_opcao()

    def direcionamento(self):
        
        while True:
            direcionamento = input(f'\n{self.classe_nome}\n\nc_ Contas (1) / Pessoa (2):\n')
            if direcionamento != '1' and direcionamento != '2':
                print('Digite uma opção válida.\n')
                continue
            if direcionamento == '1':
                import modulo_agencia
                modulo_agencia.Agencia().contas_opcao()
            else:
                import modulo_pessoa
                modulo_pessoa.Pessoa().opcao_menu()
                