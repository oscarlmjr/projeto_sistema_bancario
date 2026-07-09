class Pessoa:
    def __init__(self):
        self.lista_json_variavel = 'lista_pessoa.json'
        self.classe = Pessoa
        self.classe_nome = Pessoa.__name__
        self.classe_listar = Pessoa.listar_pessoas
        self.classe_opcao = Pessoa.opcao_menu
        self.lista_variavel = [[], []]
        self.tipo_variavel = 'Tipo Pessoa'
        self.tipo_variavel_1 = 'Pessoa Física'
        self.tipo_variavel_2 = 'Pessoa Jurídica'
        
    def opcao_menu(self):

        from modulo_menu_pessoa import Menu
        Menu.menu_opcao(self, self.__dict__)
                   
    def listar_menu(self, lista_acao_pessoa):
        
        from modulo_lista_pessoa import Lista
        Lista(self.__dict__, lista_acao_pessoa)

    def listar_pessoas(self, opcao, valor_variavel):

        if valor_variavel == self.tipo_variavel_1:
            PessoaFisica(self.__dict__, opcao, valor_variavel)
        PessoaJuridica(self.__dict__, opcao, valor_variavel)


class PessoaFisica:
      
    def __init__(self, lista_menu_pessoa, opcao, valor_variavel): 

        from modulo_menu_pessoa import Menu
        return Menu.menu_acao(self, lista_menu_pessoa, opcao, valor_variavel, 'Nome', 'RG')
    

class PessoaJuridica:    
    
    def __init__(self, lista_menu_pessoa, opcao, valor_variavel):

        from modulo_menu_pessoa import Menu
        return Menu.menu_acao(self, lista_menu_pessoa, opcao, valor_variavel, 'Nome', 'CNPJ')
    
  
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
