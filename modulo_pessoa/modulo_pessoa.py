"""
    Esse módulo inicia os tipos de cadastro de pessoa disponíveis na agência:
    pessoa física (RG) e pessoa jurídica (CNPJ)"""

class Pessoa:   # _4.1.0

    def __init__(self, contas):   # _4.1.1
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
        
    """
        Fim da adição dos selfs das classes à lista_self.
        Direcionamento para o menu autenticação."""

    def menu_self(self, lista_self):   # _4.1.2
        self_pessoa = self.self_pessoa
        lista_self.update({'self_pessoa': self_pessoa})
        self_agencia = lista_self.get('self_agencia', )

        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_autenticacao(self_agencia, lista_self)     

    def menu_opcao(self, agencia, contas, lista_self):   # _4.1.3

        from modulo_pessoa.modulo_menu_pessoa import Menu
        Menu.menu_opcao(self, agencia, contas, lista_self)
        
    def listar_variavel(self, agencia, contas, lista_self):   # _4.1.4

        from modulo_pessoa.modulo_lista_pessoa import Lista
        Lista.listar_variavel(self, agencia, contas, lista_self)    
