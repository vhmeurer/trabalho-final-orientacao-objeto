class Usuario:
    def __init__(self, codigo, nome, tipo, login, senha):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.login = login
        self.senha = senha

    def validar_senha(self, senha):
        return self.senha == senha
