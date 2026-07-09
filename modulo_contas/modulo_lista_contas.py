import json, copy


class Lista:   # _2.3.1
    
    def listar_acao(self, agencia, lista_self):        
        self.conta_cadastrada = False
        lista_conta = []  
        lista_temporaria = []      
        conta_fisica = []  
        conta_juridica = []  
        pessoa_fisica = []  
        pessoa_juridica = []  
        dados_pessoa = {}

        try:    
            with open(self.lista_transferencia_json, 'r+', encoding='utf8') as arquivo:
                self.lista_temporaria = json.load(arquivo)    
                if self.lista_temporaria is None:
                    self.lista_temporaria = []  
        except:
            ...

        if len(self.lista_temporaria) > 0:

            for dados_agencia in self.lista_temporaria:
                for agencia_transferir, dados_transferir in dados_agencia.items():

                    if self.valor_agencia == agencia_transferir:
                        
                        if dados_transferir.get(self.conta_corrente, ) is not None:
                            conta_corrente = dados_transferir.get(self.conta_corrente, ) 

                            if conta_corrente[0] == '2':
                                conta_juridica.append({conta_corrente: dados_transferir})
                            else:
                                conta_fisica.append({conta_corrente: dados_transferir})   

                        elif dados_transferir.get(self.conta_poupanca, ) is not None:
                            conta_poupanca = dados_transferir.get(self.conta_poupanca, )                                                
                            conta_fisica.append({conta_poupanca: dados_transferir})
                    else:
                        lista_temporaria.append(dados_agencia)

            self.lista_temporaria = lista_temporaria

            with open(self.lista_transferencia_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_temporaria, arquivo, ensure_ascii=False, indent=2)

        try:    
            with open(self.lista_pessoa_json, 'r+', encoding='utf8') as arquivo:
                self.lista_pessoa = json.load(arquivo)    
                if self.lista_pessoa is None:
                    self.lista_pessoa = [[], []]  
        except:
            ...

        if len(conta_fisica) > 0:
            for dados_conta in conta_fisica:
                for conta, dados in dados_conta.items():
                    dados_pessoa.update(RG=dados.get("RG", ), Nome=dados.get("Nome", ), Sexo=dados.get("Sexo", ))
                    dados_pessoa.setdefault("Tipo Pessoa", dados.get("Tipo Pessoa", ))
                pessoa_fisica.append({dados.get("RG", ): dados_pessoa}) 

            for dados_pessoa in pessoa_fisica:
                if dados_pessoa in self.lista_pessoa[0]: 
                    continue
                else:
                    self.lista_pessoa[0].append(dados_pessoa)
            dados_pessoa = {}

        if len(conta_juridica) > 0:
            for dados_conta in conta_juridica:
                for conta, dados in dados_conta.items():
                    dados_pessoa.update(CNPJ=dados.get("CNPJ", ), Nome=dados.get("Nome", ))
                    dados_pessoa.setdefault("Tipo Pessoa", dados.get("Tipo Pessoa", ))
                pessoa_juridica.append({dados.get("CNPJ", ): dados_pessoa})

            for dados_pessoa in pessoa_juridica:
                if dados_pessoa in self.lista_pessoa[1]:
                    continue
                else:
                    self.lista_pessoa[1].append(dados_pessoa)
            
        with open(self.lista_pessoa_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_pessoa, arquivo, ensure_ascii=False, indent=2)
            
        
        try:                
            with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
                self.lista_contas = json.load(arquivo)    
                if self.lista_contas is None:
                    self.lista_contas = [[], []]         
        except:  
            ...
            
        if len(conta_fisica) > 0:
            for dados_conta in conta_fisica:
                self.lista_contas[0].append(dados_conta)

        if len(conta_juridica) > 0:
            for dados_conta in conta_juridica:
                self.lista_contas[1].append(dados_conta)
        
        with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)
                
        if len(self.lista_contas) > 0:
            while True:                      
                
                for self.indice_conta, dados_conta in enumerate(self.lista_contas[self.opcao_conta]):
                    for valor_conta_variavel, dados in dados_conta.items():         

                        if self.opcao == 'Ocorrencias' or self.opcao == 'Transferir':
                            if dados.get(self.dado_variavel, ) == self.valor_dado_variavel:
                                self.conta_transferir = True

                                if valor_conta_variavel[0] == '2' or valor_conta_variavel[-1] == '1':
                                    print(f'\nv = {dados}')
                                elif valor_conta_variavel[0] == '1' and valor_conta_variavel[-1] == '2':
                                    print(f'\nv_ = {dados}')

                                if self.opcao == 'Transferir': 
                                    self.lista_transferencia.append({self.agencia_transferir: dados})

                                    lista_historico = copy.deepcopy(dados[self.historico])
                                    lista_historico.append(self.agencia_transferir)
                                    dados_conta_temporario = {valor_conta_variavel: {self.historico: lista_historico}}
                                    lista_conta.append(dados_conta_temporario)
                                    
                            elif self.opcao == 'Transferir':
                                lista_conta.append(dados_conta)

                        elif valor_conta_variavel == self.valor_conta_variavel:
                            self.conta_cadastrada = True                            
                            break          
                    if self.conta_cadastrada is True:
                        break
                if self.opcao == 'Transferir' and self.conta_transferir is True:
                    
                    self.lista_contas[self.opcao_conta] = lista_conta        
                    with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
                        json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)                                 
                break  
        
        if self.opcao == 'Listar' and self.conta_cadastrada is True:
            print(f'\nlistar_ {self.valor_conta_variavel} possue cadastro.')
            print(self.lista_contas[self.opcao_conta][self.indice_conta][self.valor_conta_variavel], '\n') 

            consulta_extrato = input('Consultar o extrato do cliente: Sim (1) Não (2)\n')  
            if consulta_extrato != '1' and consulta_extrato != '2':
                print('\nDigite uma opção válida.\n')

            elif consulta_extrato == '1':
                
                from modulo_conta_cliente.modulo_conta_cliente import ContaCliente
                ContaCliente.cliente_autenticacao(self, agencia, lista_self)
                
        elif self.opcao == 'Listar' and self.conta_cadastrada is False:
            print(f'\nlistar_2 {self.valor_conta_variavel} não possui cadastro')
            self.opcao_pessoa = self.opcao_conta
            self_pessoa = lista_self.get('self_pessoa', )

            from modulo_pessoa.modulo_lista_pessoa import Lista
            Lista.listar_variavel(self_pessoa, agencia, self.__dict__, lista_self)

        elif self.opcao == 'Cadastrar':
            print(f'\ncadastrar_2 {self.nome_conta} {self.valor_conta_variavel} não possui cadastro.')
            self.opcao_pessoa = self.opcao_conta
            self_pessoa = lista_self.get('self_pessoa', )
            
            from modulo_pessoa.modulo_lista_pessoa import Lista
            Lista.listar_variavel(self_pessoa, agencia, self.__dict__, lista_self)

        elif self.opcao == 'Ocorrencias' and self.conta_transferir is True or self.opcao == 'Transferir' and self.conta_transferir is True:
            print(f'\nTodas as ocorrências encontradas para {self.valor_dado_variavel}.')
            if self.opcao == 'Transferir':
                print(f'\nTransferindo\n')
                
                from modulo_contas.modulo_lista_contas import Lista
                Lista.transferir_variavel(self, agencia, lista_self)
                
        elif self.opcao == 'Ocorrencias' and self.conta_transferir is False or self.opcao == 'Transferir' and self.conta_transferir is False:
            print(f'\n{self.valor_dado_variavel} não possui nenhuma ocorrência.')
        
        elif self.opcao == 'Descadastrar' and self.conta_cadastrada is True:
            print(f'Descadastrando: {self.valor_conta_variavel}\n')

            from modulo_contas.modulo_lista_contas import Lista
            Lista.descadastrar_conta(self, agencia, lista_self)  

        elif self.opcao == 'Descadastrar' and self.conta_cadastrada is False:
            print(f'descadastrar {self.valor_conta_variavel} não possui cadastro.')  
        agencia['valor_agencia'] = self.valor_agencia

        from modulo_contas.modulo_contas import Contas
        Contas(agencia).menu_opcao(agencia, lista_self)   
        
    def cadastrar_conta(self, agencia, lista, lista_self):   # _2.3.2
        self.valor_conta_variavel = agencia['valor_conta_variavel'] 
        self.conta_variavel = agencia['conta_variavel'] 
        self.opcao_conta = agencia['opcao_conta'] 
        self.valor_agencia = agencia['valor_agencia']   
        classe_nome = agencia['classe_nome']   

        from random import randint

        self.valor_senha = str(randint(0000, 9999))

        lista_cadastrar = {self.senha: self.valor_senha, self.conta_variavel: self.valor_conta_variavel, 
                           classe_nome: self.valor_agencia, self.tipo_conta: self.conta_variavel,
                           self.saldo: self.valor_saldo, self.debito: self.valor_debito, self.credito: self.valor_credito, 
                           self.extrato: self.valor_extrato, self.historico: self.lista_historico}  

        for chave, valor in lista.items():
            lista_cadastrar[chave] = valor

        lista_cadastrar = {self.valor_conta_variavel: lista_cadastrar}

        with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
                self.lista_contas = json.load(arquivo)  

        self.lista_contas[self.opcao_conta].append(lista_cadastrar)

        with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2) 

            print(f'{self.conta_variavel} {self.valor_conta_variavel}_ cadastrado com sucesso_.\n')
            print(f'{self.lista_contas[self.opcao_conta][-1][self.valor_conta_variavel]}\n')
        agencia['valor_agencia'] = self.valor_agencia

        from modulo_contas.modulo_contas import Contas
        Contas(agencia).menu_opcao(agencia, lista_self)
        
    def transferir_variavel(self, agencia, lista_self):   # _2.3.3
        classe_nome = agencia['classe_nome']

        for dados_lista in self.lista_transferencia:
            for agencia_transferir, dados_conta in dados_lista.items():
                dados_temporarios = dados_conta
                dados_temporarios[classe_nome] = self.agencia_transferir
                dados_temporarios[self.historico].append(self.agencia_transferir)
            self.lista_temporaria.append({agencia_transferir: dados_temporarios})

        with open(self.lista_transferencia_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_temporaria, arquivo, ensure_ascii=False, indent=2)
        agencia['valor_agencia'] = self.valor_agencia

        from modulo_contas.modulo_contas import Contas
        Contas(agencia).menu_opcao(agencia, lista_self)
        
    def descadastrar_conta(self, agencia, lista_self):   # _2.3.4

        while True:          

            confirmacao = input(f'Confirma exclusão de {self.valor_conta_variavel}?\n'
            f'{self.lista_contas[self.opcao_conta][self.indice_conta][self.valor_conta_variavel]}\n'
            f'\nSim (1) Não(2)\n')

            if confirmacao != '1' and confirmacao != '2':
                print('\nDigite uma opção válida.\n')
                continue
            elif confirmacao == '1':

                with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
                    self.lista_contas = json.load(arquivo)    
                    if self.lista_contas is None:
                        self.lista_contas = [[], []]
                 
                del self.lista_contas[self.opcao_conta][self.indice_conta]
                print(f'\n{self.valor_conta_variavel} foi descadastrado\n')
                
                with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2)
            agencia['valor_agencia'] = self.valor_agencia

            from modulo_contas.modulo_contas import Contas
            Contas(agencia).menu_opcao(agencia, lista_self)
