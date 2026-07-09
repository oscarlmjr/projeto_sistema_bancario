
class Agencia:
    def __init__(self):
        self.classe = Agencia
        self.classe_nome = Agencia.__name__
        self.agencia = 'Agência'
        self.numero_agencia = '0001'
        self.lista_transferencia = [] 
        self.lista_json_transferencia = 'lista_transferencia.json' 
            
    def contas_opcao(self):

        from modulo_contas import Contas
        Contas(self.__dict__).opcao_menu()
            
    def contas_cadastrar(self, lista_acao_contas, lista):
        
        from modulo_contas import Contas
        Contas(self.__dict__).cadastrar_menu(lista_acao_contas, lista)


if __name__ == '__main__':
    Agencia().contas_opcao()
