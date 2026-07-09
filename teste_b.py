from teste_a import A


class B:
    def __init__(self, tipo_variavel='Conta Corrente', classe=None, classe_nome=None):
    # def __init__(self, tipo_variavel):
        # tipo_variavel = 'Conta Corrente'
        classe = B
        classe_nome = B.__name__
        # self.tipo_variavel = tipo_variavel
        self.classe = classe
        self.classe_nome = classe_nome

        print(f'self.lista_menu = {self.__dict__}\n')
        # print(f'B = {self.tipo_variavel}\n')

    def b(self, tipo_variavel, classe=None, classe_nome=None):
        self.tipo_variavel = tipo_variavel
        classe = B
        classe_nome = B.__name__
        self.classe = classe
        self.classe_nome = classe_nome

        print(f'def b self.classe = {self.classe}')
        print(f'def b self.classe_nome = {self.classe_nome}')


B()


# class B:
#     def __init__(self, tipo_variavel='Conta Corrente', classe=None, classe_nome=None):
#     # def __init__(self, tipo_variavel):
#         # tipo_variavel = 'Conta Corrente'
#         classe = B
#         classe_nome = B.__name__
#         # self.tipo_variavel = tipo_variavel
#         self.classe = classe
#         self.classe_nome = classe_nome

#         print(f'self.lista_menu = {self.__dict__}\n')
#         # print(f'B = {self.tipo_variavel}\n')


#     def b(self, tipo_variavel, classe=None, classe_nome=None):
#         self.tipo_variavel = tipo_variavel
#         classe = B
#         classe_nome = B.__name__
#         self.classe = classe
#         self.classe_nome = classe_nome

#         print(f'def b self.classe = {self.classe}')
#         print(f'def b self.classe_nome = {self.classe_nome}')


# B()

# print(f'classe = {B}')


