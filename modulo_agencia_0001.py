print('2.0_')


class Agencia:   # 2.1.0_
    """
        Os módulos das agências são gerados pelos usuários da agência matriz, 
        com permissão, apartir
        do modulo_lista_matriz, classe Lista, função cadastrar_agencia."""
    print('2.1.0_')

    def __init__(self, valor_agencia):   # 2.1.1_
        print('2.1.1_')
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

    def menu_self(self, self_matriz, valor_agencia_filial):   # 2.1.2_
        print('2.1.2_')
        self_agencia = self.self_agencia

        if self_matriz is not None:
            lista_self = {
                'self_matriz': self_matriz, 'self_agencia': self_agencia
                }
        else:
            lista_self = {'self_agencia': self_agencia}

        from modulo_contas.modulo_contas import Contas
        Contas(self.__dict__).menu_self(lista_self, valor_agencia_filial)


"""
    O modulo_agencia_0001 será acessado por funcionários da agência Matriz e da
     agência 0001. """

if __name__ == '__main__':

    Agencia('0001').menu_self(None, None)
