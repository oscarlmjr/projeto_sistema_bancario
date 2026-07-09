
class Menu:   # _8.2.0

    def menu_opcao(self, agencia, lista_self):   # _8.2.1

        while True:

            print(f'\n{self.classe_nome}\n')

            opcao = input(f'Extrato (1) / Contas (2):\n')

            if opcao != '1' and opcao != '2':
                print('Digite uma opção válida.')
                continue 

            if opcao == '1':
                self.opcao = self.extrato
                print('Digite o mês desejado:\n')
                self.mes_extrato = input('(01) Jan (02) Fev (03) Mar (04) Abr (05) Mai (06) Jun \n'
                                    '(07) Jul (08) Ago (09) Set (10) Out (11) Nov (12) Dez / Contas (0)\n')   
                
                if self.mes_extrato == '0':
                    continue

            else:
                from modulo_contas.modulo_contas import Contas
                Contas(agencia).menu_opcao(agencia, lista_self)
                
            from modulo_conta_cliente.modulo_lista_conta_cliente import Lista
            Lista.lista_conta_cliente(self, agencia, lista_self)
            