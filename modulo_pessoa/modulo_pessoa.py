"""
    Esse módulo inicia os tipos de cadastro de pessoa disponíveis na agência:
    pessoa física (RG) e pessoa jurídica (CNPJ)"""
print('4.0_')
class Pessoa:   # 4.1.1.0_
    print('4.1.0_')
    def __init__(self, contas):   # 4.1.1_
        print('4.1.1_')
        self.valor_agencia = contas['valor_agencia']
        self.lista_pessoa_json = f'lista_pessoa_{self.valor_agencia}.json'
        self.lista_pessoa = [[], []]

        self.tipo_pessoa = 'Tipo Pessoa'
        self.pessoa_fisica = 'Pessoa Física'
        self.pessoa_juridica = 'Pessoa Jurídica'
        self.pessoa_variavel = None
        self.classe_nome = Pessoa.__name__
        self.dado_nome = 'Nome'
        self.dado_sexo = 'Sexo'
        self.dado_nome_variavel = None
        self.valor_dado_variavel = None
        self.dado_rg = 'RG'
        self.dado_cnpj = 'CNPJ'
        self.dado_variavel = None
        self.pessoa_cadastrada = None

        self.self_pessoa = self
    """
        Fim da adição dos selfs das classes à lista_self.
        Direcionamento para o menu autenticação."""
    def menu_self(self, lista_self, valor_agencia_filial):   # 4.1.2_
        print('4.1.2_')
        self_agencia = lista_self.get('self_agencia', )

        self_pessoa = self.self_pessoa
        lista_self.update({'self_pessoa': self_pessoa})

        if valor_agencia_filial is True:
            from modulo_agencia.modulo_menu_agencia import Menu
            Menu.menu_opcao(self_agencia, lista_self)

        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_autenticacao(self_agencia, lista_self)
