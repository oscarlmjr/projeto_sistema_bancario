import json


class Lista:   # 5.3.0_
    print('5.3.0_')
    def cliente_autenticacao(self):   # 5.3.1_
        print('5.3.1_')

        try:
            with open(self.lista_boa_vista_bank_json, 'r+', encoding='utf8') as arquivo:
                self.lista_agencia = json.load(arquivo)

        except FileNotFoundError as error:
           print(f'\n{error.__class__.__name__}\n')
           return

        if self.valor_agencia not in self.lista_agencia:
            print(f'\n{self.nome_agencia} {self.valor_agencia} está errada.\n')
            return

        try:
            self.lista_conta_json = f'lista_conta_{self.valor_agencia}.json'

            with open(self.lista_conta_json, 'r+', encoding='utf8') as arquivo:
                self.lista_contas = json.load(arquivo)
        except FileNotFoundError as error:

            print(f'\n{error.__class__.__name__}\n')
            return

        conta = False
        senha = None

        for indice_conta, dados_variavel in enumerate(self.lista_contas[self.opcao_conta]):
            for valor_conta, dados_contas in dados_variavel.items(): 

                if valor_conta == self.valor_conta_variavel:
                    conta = True
                    if dados_contas.get(self.historico, )[-1][0] == None:
                        print(f'\n{self.conta_variavel} {self.valor_conta_variavel} está inativa.\n')
                        return
                    elif dados_contas.get(self.historico, )[-1][0] != self.valor_agencia:
                        print(f'\n_{self.conta_variavel} {self.valor_conta_variavel} não pertence a essa agência.\n')
                        return
                    if dados_contas.get(self.senha, ) == self.valor_senha:
                        senha = True
                    else:
                        senha = False
                    break
                if conta is True or senha is not None:
                    break
            if conta is True or senha is not None:
                break

        if conta == False or senha == False:
            print(f'\nA senha ou a conta está errada.\n')
            return

        sexo = 'o'
        if self.valor_conta_variavel[0] == '1' and dados_contas[self.dado_sexo] == 'f':
            sexo = 'a'
        print(f'\nOlá, {dados_contas[self.dado_nome]}, Seja bem-vind{sexo}!\n')

        self.indice_conta = indice_conta
        self.dados_contas = dados_contas

        with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

        from modulo_menu_cliente import Menu
        Menu.menu_opcao(self)

    def extrato_opcao(self):   # 5.3.2_
        print('5.3.2_')

        Lista.movimentacao_extrato(self)

    def saque_opcao(self):   # 5.3.3_
        print('5.3.3_')

        if self.dados_contas[self.tipo_conta] == self.conta_corrente and (self.valor_saldo - self.valor_saque) >= -100:
            self.valor_saldo = self.valor_saldo - self.valor_saque

        elif self.dados_contas[self.tipo_conta] == self.conta_poupanca and (self.valor_saldo - self.valor_saque) >= 0:
            self.valor_saldo = self.valor_saldo - self.valor_saque

        else:
            print(f'\n{self.saldo} insuficiente na conta.\n')
            return

        Lista.movimentacao_extrato(self)

    def deposito_opcao(self):   # 5.3.4_
        print('5.3.4_')

        self.valor_saldo += self.valor_deposito

        Lista.movimentacao_extrato(self)

    def movimentacao_extrato(self):   # 5.3.5_
        print('5.3.5_')
        movimentacao = False

        if self.opcao == self.saque or self.opcao == self.deposito:

            if self.valor_saldo < 0:
                self.valor_debito = self.valor_saldo
                self.valor_credito = 0
            elif self.valor_saldo > 0:
                self.valor_debito = 0
                self.valor_credito = self.valor_saldo
            else:
                self.valor_debito = 0
                self.valor_credito = 0

            self.dados_contas.update({self.saldo: self.valor_saldo})
            self.dados_contas.update({self.debito: self.valor_debito})
            self.dados_contas.update({self.credito: self.valor_credito})

        for indice_mes, extrato_mes in enumerate(self.dados_contas[self.extrato]):
            for mes_extrato, extrato in extrato_mes.items():
                if mes_extrato == self.mes_extrato:
                    if self.opcao == self.extrato:
                        print(f'\n{self.saldo}: R$ {self.valor_saldo},00\n')
                        print(f'{extrato}\n')
                        return

                    movimentacao = True

                    extrato_mes.get(mes_extrato).update({self.saldo: self.valor_saldo})
                    extrato_mes.get(mes_extrato).update({self.credito: self.valor_credito})
                    extrato_mes.get(mes_extrato).update({self.debito: self.valor_debito})
                    extrato_mes.get(mes_extrato).update({self.saque: self.valor_saque})
                    extrato_mes.get(mes_extrato).update({self.deposito: self.valor_deposito})
                    break

        if movimentacao is False:
            self.valor_saldo = 0
            self.valor_debito = 0
            self.valor_credito = 0 
            self.valor_saque = 0
            self.valor_deposito = 0
            indice_mes = -1
            print(f'\nNão há movimentação nesse mês.')

            self.dados_contas[self.extrato].append({self.mes: self.mes_extrato, self.mes_extrato: 
                                                    {self.mes: self.mes_extrato, self.saldo: self.valor_saldo,
                                                     self.credito: self.valor_credito, self.debito: self.valor_debito,
                                                     self.saque: self.valor_saque, self.deposito: self.valor_deposito}})

            self.dados_contas[self.extrato].sort(key=lambda item: item[self.mes])

        print(f'\n{self.saldo}: R$ {self.valor_saldo},00\n')
        print(f'{self.dados_contas[self.extrato][indice_mes].get(self.mes_extrato, )}\n')

        with open(self.lista_conta_json, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_contas, arquivo, ensure_ascii=False, indent=2) 

        return
