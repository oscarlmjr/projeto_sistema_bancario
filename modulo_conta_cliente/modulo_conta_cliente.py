
class ContaCliente:  
        
    def cliente_autenticacao(self, agencia, lista_self):   # _6.1.1        
        self.valor_senha_acesso = agencia['valor_senha_acesso']

        print(f'\nBoa Vista Bank')
        print(f'{self.classe_nome}\n')
        
        while True:

            print('Menu (1)\n')
            valor_senha = input(f'Digite a {self.senha}:\n')
                
            if valor_senha == '1':
                 from modulo_contas.modulo_menu_contas import Menu
                 Menu.menu_opcao(self, agencia, lista_self)

            elif valor_senha == self.valor_senha_acesso:
                from modulo_conta_cliente.modulo_menu_conta_cliente import Menu
                Menu.menu_opcao(self, agencia, lista_self)

            print('A senha está incorreta.\n')
            