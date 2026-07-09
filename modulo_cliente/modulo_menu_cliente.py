import sys


print('5.2.0_')
class Menu:   # 5.2.1.0_
    print('5.2.1.0_')

    def menu_autenticacao(self):   # 5.2.1.1_
        print('5.2.1.1_')
        while True:

            print(f'\nBoa Vista Bank')
            print(f'{self.classe_nome}')

            self.valor_agencia = input(f'{self.dado_agencia}:\n')
            self.valor_conta = input(f'\n{self.dado_conta}:\n')
            self.valor_senha = input(f'\n{self.senha}:\n')

            if self.valor_conta[0] == '2':
                self.opcao_conta = 1
                self.dado_variavel = self.dado_cnpj

            from modulo_lista_cliente import Lista
            Lista.cliente_autenticacao(self)

    def menu_opcao(self):   # 5.2.1.2_
        print('5.2.1.2_')
        while True:

            print(f'\n{self.classe_nome.upper()}\n')

            opcao = input(f'Saldo (1) / Extrato (2) / Saque (3) / Depósito (4) / Sair (5):\n')

            if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                print('Digite uma opção válida.')
                continue 

            if opcao == '1':
                self.opcao = self.saldo

            elif opcao == '2':
                self.opcao = self.extrato
                print('Digite o mês desejado:\n')
                self.mes_extrato = input('(01) Jan (02) Fev (03) Mar (04) Abr (05) Mai (06) Jun \n'
                                    '(07) Jul (08) Ago (09) Set (10) Out (11) Nov (12) Dez \n')

            elif opcao == '3':
                self.opcao = self.saque
                self.valor_saque = int(input('Digite o valor:\n'))

            elif opcao == '4':
                self.opcao = self.deposito 
                self.valor_deposito = int(input('Digite o valor:\n'))

            else:
                print('\nObrigado, por utilizar nosso banco.')
                print('Sua seção está sendo encerrada.')

                Menu.saida()
                
            from modulo_lista_cliente import Lista
            Lista.secao_iniciada(self)

    def saida():   # 5.2.1.3_
        print('5.2.1.3_')

        sys.exit('\nO sistema está sendo finalizado.\n')
