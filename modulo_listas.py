import json


class Lista:
    
    def __init__(self, lista_menu):
        self.lista_menu = lista_menu
        self.lista_json_variavel = lista_menu['lista_json_variavel']        
        self.lista_json_variavel_2 = lista_menu['lista_json_variavel_2']
        self.classe = lista_menu['classe']
        self.classe_nome = lista_menu['classe_nome']
        self.classe_funcao = lista_menu['classe_funcao']
        self.lista_variavel = lista_menu['lista_variavel']
        self.tipo_variavel = lista_menu['tipo_variavel']
        self.tipo_variavel_1 = lista_menu['tipo_variavel_1']
        self.tipo_variavel_2 = lista_menu['tipo_variavel_2']
        
        try:    
            with open(self.lista_json_variavel, 'r+', encoding='utf8') as arquivo:
                self.lista_variavel = json.load(arquivo)    
                if self.lista_variavel is None:
                    self.lista_variavel = [[], []]                    
        except:
            self.lista_variavel = [[], []]
            with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)

    def listar_variavel(self, lista_acao, n=0, e=0, 
        dado_busca=None, dado_busca_2=None):
        self.lista_acao = lista_acao
        self.opcao = lista_acao['opcao']
        self.valor_variavel = lista_acao['valor_variavel']
        self.dado = lista_acao['dado']
        self.dado_2 = lista_acao['dado_2']
        self.dado_3 = lista_acao['dado_3']
        self.valor_dado = lista_acao['valor_dado']
        self.valor_dado_2 = lista_acao['valor_dado_2']
        self.valor_dado_3 = lista_acao['valor_dado_3']
        self.n = n; self.e = e
        self.dado_busca = dado_busca
        self.dado_busca_2 = dado_busca_2  
        self.l = True; f = True; t = True; i = True

        if self.dado_3 is False:
            self.dado_busca = self.valor_dado_2
            if self.valor_variavel == self.tipo_variavel_2:
                self.n = 1
        elif self.dado_3 is True:
            self.dado_busca = self.valor_dado
            self.dado_busca_2 = self.valor_dado_2
        elif self.dado_3 is not False and self.dado_3 is not True:
            if self.valor_dado_2 is None:   # CNPJ
                self.n = 1
                self.dado_busca = self.valor_dado
                self.dado_busca_2 = self.valor_dado_3
            else:
                self.dado_busca = self.valor_dado
                self.dado_busca_2 = self.valor_dado_2 

        while True: 
            
            if self.dado_busca == self.dado_busca_2:
                try:    
                    with open(self.lista_json_variavel_2, 'r+', encoding='utf8') as arquivo:
                        self.lista_variavel = json.load(arquivo)    
                        if self.lista_variavel is None:
                            self.lista_variavel = [[], []]                    
                except:
                    self.lista_variavel = [[], []]
                    with open(self.lista_json_variavel_2, 'w+', encoding='utf8') as arquivo:
                        json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)
                self.l = False  
            for self.e, p in enumerate(self.lista_variavel[self.n]):
                for c, v in p.items():
                    if self.opcao == 'ocorrencias':
                        if v.get(self.dado, ) == self.dado_busca:
                            if c[0] == '2'and self.valor_variavel == self.tipo_variavel_1 or c[-1] == '1' and self.valor_variavel == self.tipo_variavel_1:
                                print(f'\nv = {v}')
                                i = False   
                                continue
                            elif c[0] == '1' and self.valor_variavel == self.tipo_variavel_2 and c[-1] == '2' and self.valor_variavel == self.tipo_variavel_2:
                                print(f'\n{v}')
                                i = False
                                continue
                    if c == self.dado_busca:
                        f = False
                        break          
                if f == False:
                    break
            if f == False or t == False:
                break   
            if self.dado_busca_2 is not None:
                t = False
                if self.valor_dado_2 is True:
                    self.n = 1
                    continue
                self.dado_busca = self.dado_busca_2
            elif self.dado_busca_2 is None:                
                break
        
        if self.opcao == 'listar' and f is False: 
            if self.valor_dado_3 is False:
                print(f'\nlistar_ {self.dado_busca} possui cadastro.')
                print(self.lista_variavel[self.n][self.e][self.dado_busca], '\n')
                return self.classe()
            elif self.dado_busca != self.dado_busca_2:                    
                print(f'\nlistar_2 {self.dado_busca} possui cadastro.')
                print(self.lista_variavel[self.n][self.e][self.dado_busca], '\n')
                return  self.classe() 
            print(f'\nlistar_1 {self.dado_busca} possui cadastro e {self.valor_dado} não possui cadastro. \n')
            # sdv log(3): (3): Conta Corrente/RG - OK / CNPJ - fail 
            print(self.lista_variavel[self.n][self.e][self.dado_busca], '\n')
            return  self.classe()                   
        elif self.opcao == 'listar' and f is True:            
            if self.valor_dado_3 is False:
                print(f'\nlistar_ {self.dado_busca} não possui cadastro.')
                return self.classe() 
            print(f'\nlistar_3 {self.valor_dado} e {self.dado_busca} não possuem cadastro.')
            return self.classe()                

        elif self.opcao == 'cadastrar' and f is False:
            if self.valor_dado_3 is False:
                print(f'\ncadastrar_ {self.dado_busca} já possui cadastro.')
                print(self.lista_variavel[self.n][self.e][self.dado_busca], '\n')
                return self.classe()
            elif self.dado_busca != self.dado_busca_2:                    
                print(f'\ncadastrar_2 {self.dado_busca} já possui cadastro.')
                print(self.lista_variavel[self.n][self.e][self.dado_busca], '\n')
                return  self.classe() 
            print(f'\ncadastrar_1 {self.dado_busca} possui cadastro e {self.valor_dado} não possui cadastro. \n')
            print(self.lista_variavel[self.n][self.e][self.dado_busca], '\n')
            Lista.cadastrar_variavel(self)
            return self.classe()
        elif self.opcao == 'cadastrar' and f is True:
            if self.valor_dado_3 is False:
                print(f'\ncadastrar {self.dado_busca} não possue cadastro.')
                Lista.cadastrar_variavel(self)
                return self.classe()
            print(f'\ncadastrar_2 {self.valor_dado} e {self.dado_busca} não possuem cadastro.')
                        
            direcionamento = input(f'\n{self.classe_nome}\n\nDeseja cadastrar Pessoa:\nSim (1) / Não (2):\n')
            if direcionamento == '1':
               from modulo_pessoa import Pessoa
               Pessoa()
            elif direcionamento == '2':
                return self.classe()
            return self.classe()
            
        elif self.opcao == 'descadastrar' and f is False:
            print(f'Descadastrando: {self.dado_busca}\n')
            Lista.descadastrar_variavel(self)        
            return self.classe()
        elif self.opcao == 'descadastrar' and f is True:
            print(f'descadastrar {self.dado_busca} não possui cadastro.')   
            return self.classe() 
        
        elif self.opcao == 'ocorrencias' and i is False:
            print(f'\nTodas as ocorrências encontradas para {self.dado_busca}.') 
            return self.classe()
        elif self.opcao == 'ocorrencias' and i is True:
            print(f'\n{self.dado_busca} não possui nenhuma ocorrência.') 
            return self.classe()
        
    def cadastrar_variavel(self):
        lista_variavel_2 = {}

        if self.l is True:            
            if self.valor_variavel == self.tipo_variavel_1:
                lista = {self.dado_2: self.valor_dado_2, 
                        self.dado: self.valor_dado, self.tipo_variavel: self.valor_variavel}
                
                self.lista_variavel[0].append({lista.get(self.dado_busca, int(self.dado_busca)): lista})
            else: 
                lista = {self.dado_2: self.valor_dado_2, 
                        self.dado: self.valor_dado, self.tipo_variavel: self.valor_variavel}
                self.lista_variavel[1].append({lista.get(self.dado_busca, int(self.dado_busca)): lista})

            with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)
                print(f'\n{self.valor_dado_2} cadastrado com sucesso.\n')
                print(f'{self.lista_variavel[self.n][-1][int(self.valor_dado_2)]}\n')

            direcionamento = input(f'\n{self.classe_nome}\n\nc_ Contas (1) / Pessoa (2):\n')
            if direcionamento == '1':
                from modulo_contas import Contas
                Contas()
            elif direcionamento == '2':
                # import modulo_pessoa
                return self.lista_variavel, self.classe()
            else:
                return self.lista_variavel, self.classe() 

        elif self.l is False:
            lista = {self.dado: self.valor_dado, 
                    self.tipo_variavel: self.valor_variavel}  
                       
            lista_variavel_2 = self.lista_variavel[self.n][self.e]   
            lista_variavel_2[self.dado_busca_2].update(lista)

            with open(self.lista_json_variavel, 'r+', encoding='utf8') as arquivo:
                self.lista_variavel = json.load(arquivo)    
                if self.lista_variavel is None:
                    self.lista_variavel = [[], []]

            for chave, valor in lista_variavel_2.items():
                
                self.lista_variavel[self.n].append({lista_variavel_2[chave].get(self.dado, ): lista_variavel_2[chave]})

            with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)            
                print(f'{self.valor_dado}_ cadastrado com sucesso.\n')
                print(f'{self.lista_variavel[self.n][-1][self.valor_dado]}\n')

        direcionamento = input(f'\n{self.classe_nome}\n\nc_2 Contas (1) / Pessoa (2):\n')
        if direcionamento == '1':
            return self.lista_variavel, self.classe()
        elif direcionamento == '2':
            from modulo_pessoa import Pessoa
            Pessoa()
        return self.lista_variavel    
            
    def descadastrar_variavel(self):

        while True:          

            confirmacao = input(f'Confirma exclusão de {self.dado_busca}?\n'
            f'{self.lista_variavel[self.n][self.e][self.dado_busca]}\n'
            f'\nSim (1) Não(2)\n')

            if confirmacao != '1' and confirmacao != '2':
                print('\nDigite uma opção válida.\n')
                continue
            elif confirmacao == '1':

                with open(self.lista_json_variavel, 'r+', encoding='utf8') as arquivo:
                    self.lista_variavel = json.load(arquivo)    
                    if self.lista_variavel is None:
                        self.lista_variavel = [[], []]
                 
                del self.lista_variavel[self.n][self.e]
                print(f'\n{self.dado_busca} foi descadastrado\n')
                
                with open(self.lista_json_variavel, 'w+', encoding='utf8') as arquivo:
                    json.dump(self.lista_variavel, arquivo, ensure_ascii=False, indent=2)

                direcionamento = input(f'\n{self.classe_nome}\n\nd_ Contas (1) / Pessoa (2):\n')
                if direcionamento == '1':
                    print('1')
                    from modulo_contas import Contas
                    Contas()
                elif direcionamento == '2':
                    print('2')
                    from modulo_pessoa import Pessoa
                    Pessoa()
                else:
                    return self.lista_variavel, self.classe()
            
            else:
                return self.lista_variavel, self.classe()
