import sys


class Menu:   # _6.1.0

    def menu_opcao(self, agencia, lista_self):   # _6.1.1
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
            #     from modulo_agencia_matriz import Matriz
            #     Matriz(self.valor_agencia).menu_agencia(lista_self)            
                self_agencia = lista_self.get('self_agencia', )
                from modulo_agencia.modulo_menu_agencia import Menu
                Menu.menu_opcao(self_agencia, lista_self)

            elif opcao == '2': 
                agencia['valor_agencia'] = self.valor_agencia

                from modulo_contas.modulo_contas import Contas
                Contas(agencia).menu_opcao(agencia, lista_self)
                
            elif opcao == '3':
                print('\nMenu (1)')
                valor_agencia_filial = input('\nDigite o número da agência:\n')
                if valor_agencia_filial == '1':
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

    def saida():   # _6.1.2
        
        sys.exit('\nO sistema está sendo finalizado.\n')

        # try:
        #     sys.exit('\nO sistema está sendo finalizado.\n')

        # except SystemExit:
        #     print('O sistema está sendo finalizado.')
