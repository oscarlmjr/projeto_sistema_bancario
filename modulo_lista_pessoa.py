import json


class Lista: 

    def __init__(self, lista_menu_pessoa, lista_acao_pessoa):
        self.classe = lista_menu_pessoa['classe']
        self.classe_nome = lista_menu_pessoa['classe_nome']
        self.classe_opcao = lista_menu_pessoa['classe_opcao']
        self.lista_json_variavel = lista_menu_pessoa['lista_json_variavel']  
        self.lista_variavel = lista_menu_pessoa['lista_variavel']
        self.opcao = lista_acao_pessoa['opcao']
        self.dado = lista_acao_pessoa['dado']
        self.dado_2 = lista_acao_pessoa['dado_2']
        self.valor_dado = lista_acao_pessoa['valor_dado']
        self.valor_dado_2 = lista_acao_pessoa['valor_dado_2'] 
        self.n = lista_acao_pessoa['n']
        self.e = lista_acao_pessoa['e']
        self.f = lista_acao_pessoa['f']
        
        try:
            self.t = lista_acao_pessoa['t']
            self.tipo_variavel = lista_acao_pessoa['tipo_variavel']
            self.valor_variavel = lista_acao_pessoa['valor_variavel']
            self.dado_3 = lista_acao_pessoa['dado_3']    
            self.valor_dado_3 = lista_acao_pessoa['valor_dado_3'] 
            self.t = False
        except:
            self.t = lista_acao_pessoa['t']
            self.tipo_variavel = lista_menu_pessoa['tipo_variavel']
            self.tipo_variavel_1 = lista_menu_pessoa['tipo_variavel_1']
            self.valor_variavel =  lista_acao_pessoa['valor_variavel']
            
        Lista.listar_variavel(self, lista_acao_pessoa)

    def listar_variavel(self, lista_acao_pessoa):

        try:    
            with open(self.lista_json_variavel, 'r+', encoding='utf8') as arquivo:
                self.lista_variavel = json.load(arquivo)    
                if self.lista_variavel is None:
                    self.lista_variavel = [[], []]                    
        except:
            self.lista_variavel = [[], []] 
            with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)  
        
        while True:             
            
            for self.e, p in enumerate(self.lista_variavel[self.n]):
                for c, v in p.items():
                    if c == self.valor_dado_2:
                        self.f = False
                        break          
                if self.f == False:
                    break            
            break        
        
        if self.opcao == 'listar' and self.f is False: 
            print(f'\nlistar {self.dado_2} {self.valor_dado_2} possui cadastro.')
            print(self.lista_variavel[self.n][self.e][self.valor_dado_2], '\n')
        elif self.opcao == 'listar' and self.f is True: 
            print(f'\nlistar_ {self.dado_2} {self.valor_dado_2} não possui cadastro.')

        if self.opcao == 'listar' and self.t is False:
            
            from modulo_agencia import Agencia
            Agencia().contas_opcao()

        elif self.opcao == 'cadastrar' and self.f is False:
            print(f'\ncadastrar {self.dado_2} {self.valor_dado_2} possui cadastro.')
            print(self.lista_variavel[self.n][self.e][self.valor_dado_2], '\n')
            lista = self.lista_variavel[self.n][self.e][self.valor_dado_2]

            if self.t is False:
                
                from modulo_agencia import Agencia
                Agencia().contas_cadastrar(self.__dict__, lista)

        elif self.opcao == 'cadastrar' and self.f is True:
            print(f'\ncadastrar_ {self.dado_2} {self.valor_dado_2} não possue cadastro.')
            
            if self.t is False:
                
                direcionamento = input(f'\n{self.classe_nome}\n\nDeseja cadastrar Pessoa:\nSim (1) / Não (2):\n')
                
                if direcionamento == '1':
                    if self.dado_2 == 'RG':
                        self.valor_variavel = 'Pessoa Física'
                    else:
                        self.valor_variavel = 'Pessoa Jurídica'

                    from modulo_pessoa import Pessoa
                    Pessoa().listar_pessoas(self.opcao, self.valor_variavel)
                else:
                    from modulo_lista_pessoa import Lista
                    Lista.direcionamento(self)
            
            from modulo_lista_pessoa import Lista
            Lista.cadastrar_variavel(self)         
            
        elif self.opcao == 'descadastrar' and self.f is False:
            print(f'Descadastrando: {self.dado_2} {self.valor_dado_2}\n')
            from modulo_lista_pessoa import Lista
            Lista.descadastrar_variavel(self)
        elif self.opcao == 'descadastrar' and self.f is True:
            print(f'descadastrar {self.dado_2} {self.valor_dado_2} não possui cadastro.')  

        from modulo_pessoa import Pessoa
        Pessoa().opcao_menu()
        
    def cadastrar_variavel(self):

        if self.valor_variavel == self.tipo_variavel_1:
            lista = {self.dado_2: self.valor_dado_2, 
                    self.dado: self.valor_dado, self.tipo_variavel: self.valor_variavel}
            
            self.lista_variavel[0].append({lista.get(self.valor_dado_2, int(self.valor_dado_2)): lista})
        else: 
            lista = {self.dado_2: self.valor_dado_2, 
                    self.dado: self.valor_dado, self.tipo_variavel: self.valor_variavel}
            self.lista_variavel[1].append({lista.get(self.valor_dado_2, int(self.valor_dado_2)): lista})

        with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
            json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)

            print(f'\n{self.valor_dado_2}__ cadastrado com sucesso.\n')
            print(f'{self.lista_variavel[self.n][-1][int(self.valor_dado_2)]}\n')

        from modulo_lista_pessoa import Lista
        Lista.direcionamento(self)

    def descadastrar_variavel(self):

        while True:          
            confirmacao = input(f'Confirma exclusão de {self.valor_dado_2}?\n'
            f'{self.lista_variavel[self.n][self.e][self.valor_dado_2]}\n'
            f'\nSim (1) Não(2)\n')

            if confirmacao != '1' and confirmacao != '2':
                print('\nDigite uma opção válida.\n')
                continue
            elif confirmacao == '1':
                 
                del self.lista_variavel[self.n][self.e]
                print(f'\n{self.valor_dado_2} foi descadastrado\n')
                
                with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)
                
                from modulo_lista_pessoa import Lista
                Lista.direcionamento(self)
            
            else:
                return 
 
    def direcionamento(self):
        
        
        while True:
            direcionamento = input(f'\n{self.classe_nome}\n\np_ Contas (1) / Pessoa (2):\n')
            if direcionamento != '1' and direcionamento != '2':
                print('Digite uma opção válida.\n')
                continue
            if direcionamento == '1':
                from modulo_agencia import Agencia
                Agencia().contas_opcao()
            else:
                return self.classe().opcao_menu()
            