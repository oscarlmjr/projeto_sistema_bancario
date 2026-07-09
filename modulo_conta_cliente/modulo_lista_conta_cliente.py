import json


print('6.3.0_')
class Lista:   # 6.3.1.0_
    print('6.3.1.0_')

    def lista_conta_cliente(self, agencia, lista_self):   # 6.3.1.1_
        print('6.3.1.1_')
        self.lista_cliente_json = f'lista_cliente_{self.valor_dado_variavel}.json'
        dados = False

        try:
            with open(self.lista_cliente_json, 'r+', encoding='utf8') as arquivo:
                self.lista_cliente = json.load(arquivo)

            for indice_cliente, conta_dados_cliente in enumerate( self.lista_cliente):
                for conta_cliente, self.dados_cliente in conta_dados_cliente.items(): 
                    if conta_cliente == self.valor_conta_variavel:
                        dados = True
                        break
                if dados is True:
                    break
        except:
            print(f'\nOpção "Extrato (1)" indisponível no momento.\n')
            from modulo_conta_cliente.modulo_menu_conta_cliente import Menu
            Menu.menu_opcao(self, agencia, lista_self)

        if self.opcao == self.extrato:
            Lista.extrato_opcao(self, agencia, lista_self)

    def extrato_opcao(self, agencia, lista_self):   # 6.3.1.2_
        print('6.3.1.2_')
        for extrato_mes in self.dados_cliente[self.extrato]:
            if extrato_mes.get('mês', ) == self.mes_extrato:
                print(f'\n{self.extrato}:\n')
                for opcao_valor in extrato_mes.get(self.mes_extrato, ):
                    print(f'{opcao_valor}')

                if len(extrato_mes.get(self.mes_extrato, )) == 1:
                    print(f'Não há movimentação nesse mês.\n')

                from modulo_conta_cliente.modulo_menu_conta_cliente import Menu
                Menu.menu_opcao(self, agencia, lista_self)

        print(f'Não há extrato para o mês selecionado.\n')

        from modulo_conta_cliente.modulo_menu_conta_cliente import Menu
        Menu.menu_opcao(self, agencia, lista_self)
