"""
    Os módulos das agências são gerados pelos usuários da agência matriz, com permissão, apartir
    do modulo_lista_matriz, classe Lista, função cadastrar_agencia."""

class Agencia:   # _2.0
    def __init__(self, valor_agencia):   # _2.1
        self.valor_agencia = valor_agencia
        self.classe_nome = 'Agência'
        self.lista_acesso_json = f'lista_acesso_{self.valor_agencia}.json'
        self.lista_acesso = []
        self.lista_transferencia_json = 'lista_transferencia.json'
        self.lista_transferencia = [] 
        self.valor_matricula = None
        self.matricula = 'Matrícula'
        self.valor_senha = None
        self.senha = 'Senha'
        self.opcao = 'cadastrar'  
        self.usuario_autenticado = None
               
        self.modulo_menu_matriz = 'modulo_menu_matriz'
        self.modulo_menu_agencia = 'modulo_menu_agencia' 
        self.modulo_lista_agencia = 'modulo_lista_agencia'
        self.modulo_contas = 'modulo_contas'
        
        self.self_agencia = self

    """
        O modulo_agencia_0001 será acessado por funcionários da agência Matriz e da agência 0001. """
            
    def menu_self(self, self_matriz):   # _2.2
        self_agencia = self.self_agencia            

        if self_matriz is not None:
            lista_self = {'self_matriz': self_matriz, 'self_agencia': self_agencia}
        else:
            lista_self = {'self_agencia': self_agencia}

        from modulo_contas.modulo_contas import Contas
        Contas(self.__dict__).menu_self(lista_self)   
    
    # def menu_opcao(self, lista_self):   # _2.3

    #     from modulo_agencia.modulo_menu_agencia import Menu
    #     Menu.menu_opcao(self, lista_self)  
