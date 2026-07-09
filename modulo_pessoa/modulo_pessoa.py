
class Pessoa: 

    def __init__(self, contas): 
        self.valor_agencia = contas['valor_agencia']
        self.lista_pessoa_json = f'lista_pessoa_{self.valor_agencia}.json'          
        self.lista_pessoa = [[], []]

        self.tipo_pessoa = 'Tipo Pessoa'
        self.pessoa_fisica = 'Pessoa Física'
        self.pessoa_juridica = 'Pessoa Jurídica'
        self.pessoa_variavel = self.pessoa_fisica             
        self.classe_nome = Pessoa.__name__
        self.dado_nome = 'Nome'
        self.dado_sexo = 'Sexo'
        self.valor_dado_variavel = None
        self.dado_rg = 'RG'
        self.dado_cnpj = 'CNPJ'         
        self.dado_variavel = self.dado_rg
        self.opcao_conta = 0
        self.opcao_pessoa = self.opcao_conta
        self.opcao = None

        self.modulo_menu_pessoa = 'modulo_menu_pessoa'
        
        self.self_pessoa = self   

    def menu_self(self, lista_self):        
        self_pessoa = self.self_pessoa
        lista_self.update({'self_pessoa': self_pessoa})
        self_agencia = lista_self.get('self_agencia', )

        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_autenticacao(self_agencia, lista_self)     

    def menu_opcao(self, agencia, contas, lista_self):

        from modulo_pessoa.modulo_menu_pessoa import Menu
        Menu.menu_opcao(self, agencia, contas, lista_self)
        
    def listar_variavel(self, agencia, contas, lista_self):

        from modulo_pessoa.modulo_lista_pessoa import Lista
        Lista.listar_variavel(self, agencia, contas, lista_self) 
        
  
########################
       
    # @property
    # def nome(self):
    #     return self._nome
    # @nome.setter
    # def nome(self, valor):
    #     self._nome = valor
    
    # @property
    # def rg(self):
    #     return self._rg
    # @cnpj.setter
    # def rg(self, valor):
    #     self._rg = valor

    # @property
    # def nome(self):
    #     return self._nome
    # @nome.setter
    # def nome(self, valor):
    #     self._nome = valor
    
    # @property
    # def cnpj(self):
    #     return self._cnpj
    # @cnpj.setter
    # def cnpj(self, valor):
    #     self._cnpj = valor
