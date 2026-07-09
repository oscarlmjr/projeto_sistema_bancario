import sys


class Menu:   # 5.2.0_
    print('5.2.0_')
    def menu_autenticacao(self):   # 5.2.1_
        print('5.2.1_')
        print(f'\nBoa Vista Bank')
        print(f'{self.classe_nome}')
        print('Sair (0)\n')

        while True:

            valor_agencia = input(f'{self.nome_agencia}:\n')
            # valor_agencia = '0001'
            print(valor_agencia)
            if valor_agencia == '0':
                break
            valor_conta_variavel = input(f'\n{self.nome_conta}:\n')
            # valor_conta_variavel = '11131'
            # print(valor_conta_variavel)
            if valor_conta_variavel == '0':
                break
            valor_senha = input(f'\n{self.senha}:\n')
            # valor_senha = '9205'
            # print(valor_senha)
            if valor_senha == '0':
                break

            elif valor_agencia == '' or valor_conta_variavel == '' or valor_senha == '':
                print('\nDigite uma opção válida.\n')
                continue
            if valor_conta_variavel[0] == '1':
                if valor_conta_variavel[-1] == '1':
                    self.digito_conta = '1'
                    self.conta_variavel = self.conta_corrente
                else:
                    self.digito_conta = '2'
                    self.conta_variavel = self.conta_poupanca
                self.opcao_conta = 0
            else:
                self.digito_conta = '1'
                self.opcao_conta = 1
                self.conta_variavel = self.conta_corrente
            self.valor_agencia = valor_agencia
            self.valor_conta_variavel = valor_conta_variavel
            self.valor_senha = valor_senha

            from modulo_lista_cliente import Lista
            Lista.cliente_autenticacao(self)

        print('\nObrigado, por utilizar nosso banco.')
        sys.exit('\nO sistema está sendo finalizado.\n')

    def menu_opcao(self):   # 5.2.2_
        print('5.2.2_')
        print('\nBoa Vista Bank')
        print(self.classe_nome)
        print(f'Agência {self.valor_agencia}')
        print(f'{self.conta_variavel} {self.valor_conta_variavel}')
        print('Menu (0)\n')

        while True:

            if self.classe_nome == 'Contas':
                from modulo_cliente.modulo_lista_cliente import Lista

                opcao = input(f'\nSaldo (1) / Extrato (2) / Saque (3) / Depósito (4) / Transferir (5) / Contas (6) / Sair (7):\n')
                # opcao = '2'
                # print(f'{opcao=}')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6' and opcao != '7':
                    print('\nDigite uma opção válida.\n')
                    continue
                elif opcao == '7':
                    sys.exit('\nO sistema está sendo finalizado.\n')

            else:
                from modulo_lista_cliente import Lista

                opcao = input(f'\nSaldo (1) / Extrato (2) / Saque (3) / Depósito (4) / Transferir (5) / Sair (6):\n')
                if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5' and opcao != '6':
                    print('\nDigite uma opção válida.\n')
                    continue
                elif opcao == '6':
                    print('\nObrigado, por utilizar nosso banco.')
                    sys.exit('Sua seção está sendo encerrada.\n')

            self.mes_extrato = '7'   # mês atual
            self.valor_saldo = self.dados_contas.get(self.saldo, )
            self.valor_credito = self.dados_contas.get(self.credito, )
            self.valor_debito = self.dados_contas.get(self.debito, )

            if opcao == '1':
                print('\nSaldo')
                print(f'\n{self.saldo}: R$ {self.valor_saldo},00\n')
                continue

            elif opcao == '2':
                print('\nExtrato')
                print('\nDigite o mês desejado:\n')
                mes_extrato = input('(01) Jan (02) Fev (03) Mar (04) Abr (05) Mai (06) Jun \n'
                                    '(07) Jul (08) Ago (09) Set (10) Out (11) Nov (12) Dez \n')
                if mes_extrato == '0':
                    continue
                self.mes_extrato = mes_extrato
                self.opcao = self.extrato

                Lista.extrato_opcao(self)
                continue

            elif opcao == '3':
                print('\nSaque')
                valor_saque = int(input('\nDigite o valor:\n'))
                if valor_saque == 0:
                    continue
                self.opcao = self.saque
                self.valor_saque = valor_saque

                Lista.saque_opcao(self)
                continue

            elif opcao == '4':
                print('\nDepósito')
                valor_deposito = int(input('\nDigite o valor:\n'))
                if valor_deposito == 0:
                    continue
                self.opcao = self.deposito
                self.valor_deposito = valor_deposito

                Lista.deposito_opcao(self)
                continue

            elif opcao == '5':
                print('\nTransferência')
                print('\nEssa opção está inativa no momento.\nDesculpe-nos o transtorno.\n')
                continue

            elif opcao == '6':
                self.valor_saldo = 0
                self.valor_debito = 0
                self.valor_credito = 0

                return

            break