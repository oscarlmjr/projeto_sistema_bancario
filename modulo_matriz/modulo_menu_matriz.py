import json, sys


class Menu:   # 1.2.0_
    print('1.2.0_')
    def menu_opcao(self, agencia, lista_self):   # 1.2.1_
        print('1.2.1_')
        classe_nome = agencia['classe_nome']
        """
            Usuários com permissão de administrador podem acessar o menu da agência 0001 (Agência (1));
            acessar as contas bancárias das pessoas físicas e jurídicas cadastradas (Contas (2));
            acessar qualquer agência filial (Filial(3)); cadastrar novas agências (Cadastrar agência (4)) e
            sair do sistema (Sair(5))."""
        
        print(f'\nBoa Vista Bank\n{self.classe_nome}')
        print(f'{classe_nome} {self.valor_agencia}')
        print('Menu (0)')
                    
        while True:

            opcao = input('\nAgência (1) / Contas (2) / Filial (3) / Cadastrar agência (4) / Sair (5):\n')
            # opcao = '2'
            # print(f'{opcao}')
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
                self.opcao = 'filial'

                while True:
                    valor_agencia_filial = input('\nDigite o número da agência:\n')
                    # valor_agencia_filial = '0002'
                    # print(f'{valor_agencia_filial}')
                    if valor_agencia_filial == '':
                        print('Digite uma opção válida.\n')
                        continue
                    elif valor_agencia_filial == '0':
                        break
                    elif valor_agencia_filial == self.valor_agencia:
                        print(f'\nVocê já está na agencia {self.valor_agencia}.\n')
                        continue

                    self.valor_agencia_filial = valor_agencia_filial

                    from modulo_matriz.modulo_lista_matriz import Lista
                    Lista.acesso_filial(self, agencia, lista_self)

            elif opcao == '4':
                self.opcao = 'cadastrar'

                while True:

                    confirmacao = input('\nConfirma cadastrar nova agência: Sim (1) / Não (2)\n')

                    if confirmacao == '0':
                        break
                    elif confirmacao != '1' and confirmacao != '2':
                        print('\nDigite uma opcão válida.\n')
                        continue
                    elif confirmacao == '1':
                        try:
                            with open(self.lista_boa_vista_bank_json, 'r+', encoding='utf8') as arquivo:
                                self.lista_agencia = json.load(arquivo)
                        except:
                            with open(self.lista_boa_vista_bank_json, 'w+', encoding='utf8') as arquivo:
                                json.dump(self.lista_agencia, arquivo, ensure_ascii=False, indent=2)

                        self.valor_agencia_filial = None

                        from modulo_matriz.modulo_lista_matriz import Lista
                        Lista.cadastrar_agencia(self, agencia, lista_self)
                    break

            elif opcao == '5':
                sys.exit('\nO sistema está sendo finalizado.\n')

                # try:
                #     sys.exit('\nO sistema está sendo finalizado.\n')

                # except SystemExit:
                #     print('O sistema está sendo finalizado._')
