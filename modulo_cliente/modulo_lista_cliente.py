import json


print('5.3.0_')
class Lista:   # 5.3.1.0_
    print('5.3.1.0_')
    def cliente_autenticacao(self):   # 5.3.1.1_
        print('5.3.1.1_')
        self.lista_conta_json = f'lista_conta_{self.valor_agencia}.json'
        # self.lista_cliente_json = f'lista_cliente_{self.valor_dado_variavel}.json'

        with open(self.lista_boa_vista_bank_json, 'r+', encoding='utf8') as arquivo:
            lista_agencia = json.load(arquivo)

        if self.valor_agencia in lista_agencia:
           ...
        else:
            print(f'\n{self.dado_agencia}: {self.valor_agencia} está errada.')
            return

        if self.valor_conta[0] == '2':
            self.dado_variavel = self.dado_cnpj
            self.opcao_conta = 1

        senha = False
        conta = False

        with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
            self.lista_contas = json.load(arquivo) 

        for self.indice_conta, self.dados_lista_variavel in enumerate(self.lista_contas[self.opcao_conta]):
            for valor_conta, dados in self.dados_lista_variavel.items(): 

                if valor_conta == self.valor_conta: 
                    conta = True                           
                    if dados.get(self.senha, ) == self.valor_senha:
                        lista_cliente = []
                        senha = True  
                        self.valor_dado_variavel = dados.get(self.dado_variavel, )
                        lista_cliente.append(self.dados_lista_variavel)
                        break
                    if dados.get(self.senha, ) is None: 
                        print(f'\n{self.dado_conta}: {self.valor_conta} não está em atividade.')                        
                        return                            
                    print(f'\n{self.senha}: {self.valor_senha} está errada.')
                    return                            
            if senha == True:
                break
        if conta == False:
            print(f'\n{self.dado_conta}: {self.valor_conta} está errado.')
            return 

        try:
            self.lista_cliente_json = f'lista_cliente_{self.valor_dado_variavel}.json'
            sexo = 'o'

            with open(self.lista_cliente_json, 'r+', encoding='utf8') as arquivo:
                self.lista_cliente = json.load(arquivo)

            nova_conta = True
            for indice_cliente, conta_dados_cliente in enumerate( self.lista_cliente):
                for conta_cliente, dados_cliente in conta_dados_cliente.items(): 
                    if conta_cliente == self.valor_conta:
                        nova_conta = False
                        print(f'\n{dados_cliente[self.dado_nome]}')

                        if self.valor_conta[0] == '1' and dados_cliente[self.dado_sexo] == 'f':
                            sexo = 'a'
                            break
                if nova_conta is False:
                    break

            if nova_conta is True:
                self.lista_cliente.append(*lista_cliente)

                with open(self.lista_cliente_json, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_cliente, arquivo, ensure_ascii=False, indent=2)             

                print(f'\n{self.lista_cliente[-1][self.valor_conta][self.dado_nome]}, obrigado por abrir mais uma conta em nossa agência!')
                
                if self.valor_conta[0] == '1' and self.lista_cliente[-1][self.valor_conta][self.dado_sexo] == 'f':
                    sexo = 'a'

            print(f'Seja bem-vind{sexo}!\n')

        except:
            # primeira abertura de conta
            with open(self.lista_cliente_json, 'w+', encoding='utf8') as arquivo:
                json.dump(lista_cliente, arquivo, ensure_ascii=False, indent=2)             

            print(f'\n{lista_cliente[0][self.valor_conta][self.dado_nome]}, obrigado por abrir uma conta em nossa agência!')
            # sexo = 'o'

            if self.valor_conta[0] == '1' and lista_cliente[0][self.valor_conta][self.dado_sexo] == 'f':
                sexo = 'a'

            print(f'Seja bem-vind{sexo}!\n')

        from modulo_menu_cliente import Menu
        Menu.menu_opcao(self)

    def secao_iniciada(self):   # 5.3.1.2_
        print('5.3.1.2_')

        with open(self.lista_cliente_json, 'r+', encoding='utf8') as arquivo:
            self.lista_cliente = json.load(arquivo)

        for self.indice, conta_dados in enumerate(self.lista_cliente):
            for conta, self.dados in conta_dados.items(): 
                
                if conta == self.valor_conta:

                    if self.opcao == self.saldo:
                        print(f'\n{self.saldo}: R$ {self.dados.get(self.saldo, )},00')

                    elif self.opcao == self.extrato:
                        Lista.extrato_opcao(self)

                    elif self.opcao == self.saque:
                        
                        Lista.saque_opcao(self)
                        
                    elif self.opcao == self.deposito:

                        Lista.deposito_opcao(self)

                return

    def extrato_opcao(self):   # 5.3.1.3_
        print('5.3.1.3_')
        movimentacao = False

        for extrato_mes in self.dados[self.extrato]:
            if extrato_mes.get('mês', ) == self.mes_extrato:
                movimentacao = True
                print(f'\n{self.extrato}:\n')
                for opcao_valor in extrato_mes.get(self.mes_extrato, ):
                    print(f'{opcao_valor}')

                if len(extrato_mes.get(self.mes_extrato, )) == 1:
                    print(f'Não há movimentação nesse mês.\n')
                break

        if movimentacao is False:
            self.dados[self.extrato].append({'mês': self.mes_extrato, self.mes_extrato: [{self.saldo: self.valor_saldo}]})
            self.dados[self.extrato].sort(key=lambda item: item['mês'])

            with open(self.lista_cliente_json, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_cliente, arquivo, ensure_ascii=False, indent=2)

            for extrato_mes in self.dados[self.extrato]:
                if extrato_mes.get('mês', ) == self.mes_extrato:

                    print(f'\n{self.extrato}:\n')
                    for opcao_valor in extrato_mes.get(self.mes_extrato, ):
                        print(f'{opcao_valor}')

                    if len(extrato_mes.get(self.mes_extrato, )) == 1:
                        print(f'Não há movimentação nesse mês.\n')
                    break  
        return

    def saque_opcao(self):   # 5.3.1.4_
        print('5.3.1.4_')
        self.valor_saldo = self.dados.get(self.saldo, )

        if self.dados[self.tipo_conta] == self.conta_corrente and (self.valor_saldo - self.valor_saque) >= -100:
            self.valor_saldo = self.valor_saldo - self.valor_saque
            self.lista_cliente[self.indice][self.valor_conta][self.saldo] = self.valor_saldo

        elif self.dados[self.tipo_conta] == self.conta_poupanca and (self.valor_saldo - self.valor_saque) >= 0:
            self.valor_saldo = self.valor_saldo - self.valor_saque
            self.lista_cliente[self.indice][self.valor_conta][self.saldo] = self.valor_saldo

        else:
            print(f'\n{self.saldo} insuficiente na conta.\n') 
            return

        Lista.movimentacao_extrato(self, self.saque, self.valor_saque)

    def deposito_opcao(self):   # 5.3.1.5_
        print('5.3.1.5_')
        self.lista_cliente[self.indice][self.valor_conta][self.saldo] += self.valor_deposito

        Lista.movimentacao_extrato(self, self.deposito, self.valor_deposito)

    def movimentacao_extrato(self, opcao, valor_opcao):   # 5.3.1.6_
        print('5.3.1.6_')
        self.mes_extrato = '9'   # mês atual
        movimentacao = False

        for extrato_mes in self.dados[self.extrato]:

            if extrato_mes.get('mês', ) == self.mes_extrato:
                movimentacao = True
                self.valor_saldo = self.dados.get(self.saldo, )

                extrato_mes[self.mes_extrato].pop()
                
                extrato_mes.get(self.mes_extrato, ).append({opcao: valor_opcao})
                extrato_mes.get(self.mes_extrato, ).append({self.saldo: self.valor_saldo})
                continue

        if movimentacao is False:
            self.valor_saldo = self.dados.get(self.saldo, )
            self.dados[self.extrato].append({'mês': self.mes_extrato, self.mes_extrato: [{opcao: valor_opcao}, {self.saldo: self.valor_saldo}]})
            self.dados[self.extrato].sort(key=lambda item: item['mês'])

        if self.valor_saldo < 0:
            self.dados[self.debito] = self.valor_saldo
            self.dados[self.credito] = 0
        elif self.valor_saldo > 0:
            self.dados[self.debito] = 0
            self.dados[self.credito] = self.valor_saldo
        else:
            self.dados[self.debito] = 0
            self.dados[self.credito] = 0

        self.valor_debito = self.dados[self.debito]
        self.valor_credito = self.dados[self.credito]

        with open(self.lista_cliente_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_cliente, arquivo, ensure_ascii=False, indent=2) 

        print(f'\n{self.saldo}: R$ {self.dados.get(self.saldo, )},00') 

        Lista.movimentacao_conta(self)

    def movimentacao_conta(self):   # 5.3.1.7_
        print('5.3.1.7_')

        with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
            self.lista_cliente = json.load(arquivo)

            self.lista_cliente[self.opcao_conta][self.indice_conta][self.valor_conta][self.saldo] = self.valor_saldo
            self.lista_cliente[self.opcao_conta][self.indice_conta][self.valor_conta][self.debito] = self.valor_debito
            self.lista_cliente[self.opcao_conta][self.indice_conta][self.valor_conta][self.credito] = self.valor_credito

        with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_cliente, arquivo, ensure_ascii=False, indent=2)

        from modulo_menu_cliente import Menu
        Menu.menu_opcao(self)
