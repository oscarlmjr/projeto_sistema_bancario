from modulo_menu import Menu


class Pessoa:
    def __init__(self):
        self.lista_json_variavel = 'lista_pessoa.json'
        self.lista_json_variavel_2 = None
        self.classe = Pessoa
        self.classe_nome = Pessoa.__name__
        self.classe_funcao = Pessoa.listar_pessoas
        self.lista_variavel = [[], []]
        self.tipo_variavel = 'Tipo Pessoa'
        self.tipo_variavel_1 = 'Pessoa Física'
        self.tipo_variavel_2 = 'Pessoa Jurídica'
        
        Menu.menu_opcao(self, self.__dict__)
                   
    def listar_pessoas(self, opcao, valor_variavel):

        if valor_variavel == self.tipo_variavel_1:

            return PessoaFisica(self.__dict__, opcao, valor_variavel, self.tipo_variavel_1, self.tipo_variavel_2)
        PessoaJuridica(self.__dict__, opcao, valor_variavel, self.tipo_variavel_1, self.tipo_variavel_2)


class PessoaFisica:
      
    def __init__(self, lista_menu, opcao, valor_variavel, tipo_variavel_1, tipo_variavel_2):  
        
        return Menu.menu_acao(self, lista_menu, opcao, valor_variavel, 
        tipo_variavel_1, tipo_variavel_2, 'Nome', 'RG', False)
    

class PessoaJuridica:    
    
    def __init__(self, lista_menu, opcao, valor_variavel, tipo_variavel_1, tipo_variavel_2):

        return Menu.menu_acao(self, lista_menu, opcao, valor_variavel, 
        tipo_variavel_1, tipo_variavel_2, 'Nome', 'CNPJ', False)
    

Pessoa()

  
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





