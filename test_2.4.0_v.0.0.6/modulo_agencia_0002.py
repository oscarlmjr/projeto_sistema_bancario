print('2.4_')
class Agencia:   # 2.4.0_
    print('2.4.0_')
    def __init__(self, valor_agencia):   # 2.4.1_
        print('2.4.1_')
        self.valor_agencia = valor_agencia
        self.classe_nome = 'Agência'
        self.lista_acesso_json = f'lista_acesso_{self.valor_agencia}.json'
        self.lista_acesso = [] 
        self.valor_matricula = None
        self.matricula = 'Matrícula'
        self.valor_senha = None
        self.senha = 'Senha'
        self.opcao = None

        self.self_agencia = self

    def menu_self(self, self_matriz, valor_agencia_filial):   # 2.4.2_
        print('2.4.2_')
        self_agencia = self.self_agencia

        if self_matriz is not None:
            lista_self = {"self_matriz": self_matriz, "self_agencia": self_agencia}

        else:
            lista_self = {"self_agencia": self_agencia}

        from modulo_contas.modulo_contas import Contas
        Contas(self.__dict__).menu_self(lista_self, valor_agencia_filial)

    def menu_opcao(self, lista_self):   # 2.4.3_
        print('2.4.3_')

        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_opcao(self, lista_self)


if __name__ == "__main__":

    Agencia("0002").menu_self(None, None)
