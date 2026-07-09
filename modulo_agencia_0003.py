class Agencia:
    def __init__(self, valor_agencia):
        self.valor_agencia = valor_agencia
        self.classe_nome = "Agência"
        self.lista_acesso_json = f"lista_acesso_{self.valor_agencia}.json"
        self.lista_acesso = []
        self.lista_transferencia_json = "lista_transferencia.json"
        self.lista_transferencia = []
        self.valor_matricula = None
        self.matricula = "Matrícula"
        self.valor_senha = None
        self.senha = "Senha"
        self.opcao = "cadastrar"
        self.usuario_autenticado = None

        self.modulo_menu_matriz = "modulo_menu_matriz"
        self.modulo_menu_agencia = "modulo_menu_agencia"
        self.modulo_lista_agencia = "modulo_lista_agencia"
        self.modulo_contas = "modulo_contas"

        self.self_agencia = self

    def menu_self(self, self_matriz):
        self_agencia = self.self_agencia

        if self_matriz is not None:
            lista_self = {"self_matriz": self_matriz, "self_agencia": self_agencia}

        else:
            lista_self = {"self_agencia": self_agencia}

        from modulo_contas.modulo_contas import Contas
        Contas(self.__dict__).menu_self(lista_self)

    def menu_opcao(self, lista_self):

        from modulo_agencia.modulo_menu_agencia import Menu
        Menu.menu_opcao(self, lista_self)


if __name__ == "__main__":
    Agencia("0003").menu_self(None)
