from datetime import date, timedelta

class Emprestimo:
    def __init__(self, codigo, codigo_usuario, codigo_livro, data_emprestimo, data_devolucao):
        self.codigo = codigo
        self.codigo_usuario = codigo_usuario
        self.codigo_livro = codigo_livro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def setCodigo_usuario(self, codigo_usuario):
        self.codigo_usuario = codigo_usuario

    def getCodigo_usuario(self):
        return self.codigo_usuario

    def setCodigo_livro(self, codigo_livro):
        self.codigo_livro = codigo_livro

    def getCodigo_livro(self):
        return self.codigo_livro
