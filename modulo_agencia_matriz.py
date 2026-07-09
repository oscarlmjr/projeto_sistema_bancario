class Matriz:   # _1
    
    def __init__(self, valor_agencia):
        print(f'self.valor_agencia_filial__ = {valor_agencia}')
        self.classe_nome = Matriz.__name__
        self.lista_boa_vista_bank_json = 'lista_boa_vista_bank.json'
        self.lista_agencia = ['0001']
        self.valor_agencia = valor_agencia

        self.modulo_agencia_numero = f'modulo_agencia_{self.valor_agencia}'
        self.self_matriz = self

    def menu_self(self):   # _1.1
        self_matriz = self.self_matriz
        __import__(self.modulo_agencia_numero).Agencia(self.valor_agencia).menu_self(self_matriz)
   
    def menu_agencia(self, lista_self):   # _1.2
        
        __import__(self.modulo_agencia_numero).Agencia(self.valor_agencia).menu_opcao(lista_self)


if __name__ == '__main__':
    Matriz('0001').menu_self()
