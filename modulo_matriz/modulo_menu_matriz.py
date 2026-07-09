import sys

print('1.2.0_')
class Menu:   # 1.2.1.0_
    print('1.2.1.0_')
    def menu_opcao(self, agencia, lista_self):   # 1.2.1.1_
        print('1.2.1.1_')
        classe_nome = agencia['classe_nome']
        """
            Usuários com permissão de administrador podem acessar o menu da agência 0001 (Agência (1));
            acessar as contas bancárias das pessoas físicas e jurídicas cadastradas (Contas (2));
            acessar qualquer agência filial (Filial(3)); cadastrar novas agências (Cadastrar agência (4)) e
            sair do sistema (Sair(5))."""
        while True:

            print(f'\nBoa Vista Bank\n{self.classe_nome}')
            print(f'{classe_nome} {self.valor_agencia}\n')
                        
            opcao = input('Agência (1) / Contas (2) / Filial (3) / Cadastrar agência (4) / Sair (5):\n')

            if opcao != '1' and opcao != '2' and opcao != '3' and opcao != '4' and opcao != '5':
                print('Digite uma opção válida.')
                continue

            if opcao == '1':
                self_agencia = lista_self.get('self_agencia', )
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_opcao(self_agencia, lista_self)

            elif opcao == '2':
                self_contas = lista_self.get('self_contas', )
                from modulo_contas.modulo_menu_contas import Menu
                Menu.menu_opcao(self_contas, agencia, lista_self)

            elif opcao == '3':
                print('\nMenu (1)')
                valor_agencia_filial = input('\nDigite o número da agência:\n')
                if valor_agencia_filial == '1':
                    continue
                if valor_agencia_filial == '':
                    print('Digite uma opção válida.')
                    continue
                elif valor_agencia_filial == self.valor_agencia:
                    print(f'Você já está na agencia {self.valor_agencia}.')
                    continue

                self.valor_agencia_filial = valor_agencia_filial

                from modulo_matriz.modulo_lista_matriz import Lista
                Lista.acesso_filial(self, agencia, lista_self)

            elif opcao == '4':

                confirmacao = input('\nConfirma cadastrar nova agência: Sim (1) / Não (2)\n')

                if confirmacao != '1' and confirmacao != '2':
                    print('Digite uma opcão válida.')
                    continue
                if confirmacao == '1':
                    from modulo_matriz.modulo_lista_matriz import Lista
                    Lista.cadastrar_agencia(self, agencia, lista_self)

                continue

            from modulo_matriz.modulo_menu_matriz import Menu
            Menu.saida()

    def saida():   # 1.2.1.2_
        print('1.2.1.2_')
        sys.exit('\nO sistema está sendo finalizado.\n')

        # try:
        #     sys.exit('\nO sistema está sendo finalizado.\n')

        # except SystemExit:
        #     print('O sistema está sendo finalizado.')
