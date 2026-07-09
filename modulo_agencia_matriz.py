"""
Esse módulo inicia o sistema.
Apenas usuários da agência Matriz e usuários com permissão de administrador estão 
autorizados ao acesso.
Todas as classes e funções do sistema estão numeradas afim de identificação no processo de teste, 
de acordo com execução do sistema e opções dos menus. """
print('1.0_')
class Matriz:   # 1.1.0_
    print('1.1.0_')
    def __init__(self, valor_agencia):   # 1.1.1_
        print('1.1.1_')
        self.valor_agencia = valor_agencia
        self.classe_nome = Matriz.__name__
        self.lista_boa_vista_bank_json = 'lista_boa_vista_bank.json'
        self.lista_agencia = ['0001']

        self.modulo_agencia_numero = f'modulo_agencia_{self.valor_agencia}'
        self.self_matriz = self
    """
        A função menu_self, em todos os módulos, transporta o self da classe de cada módulo e 
        adiciona-o ao dict lista_self. """

    def menu_self(self, valor_agencia_filial):   # 1.1.2_
        print('1.1.2_')
        self_matriz = self.self_matriz
        __import__(self.modulo_agencia_numero).Agencia(self.valor_agencia).menu_self(self_matriz, valor_agencia_filial)

    def menu_agencia(self, lista_self):   # 1.1.3_
        print('1.1.3_')
        __import__(self.modulo_agencia_numero).Agencia(self.valor_agencia).menu_opcao(lista_self)


if __name__ == '__main__':

    Matriz('0001').menu_self(None)
