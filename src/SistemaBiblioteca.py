import os
from models.Usuario import Usuario
from models.Livro import Livro
from models.Emprestimo import Emprestimo


class SistemaBiblioteca:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()
        self.livros = self.carregar_livros()
        self.emprestimos = self.carregar_emprestimos()
        self.usuario_logado = None

    def carregar_usuarios(self):
        usuarios = []
        usuarios_path = os.path.join("dados", "usuarios.txt")
        with open(usuarios_path, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 5:
                    codigo, nome, tipo, login, senha = dados
                    usuario = Usuario(codigo, nome, tipo, login, senha)
                    usuarios.append(usuario)
        return usuarios

    def carregar_livros(self):
        livros = []
        livros_path = os.path.join("dados", "livros.txt")
        with open(livros_path, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 3:
                    codigo, nome, autor = dados
                    livro = Livro(codigo, nome, autor)
                    livros.append(livro)
        return livros

    def carregar_emprestimos(self):
        emprestimos = []
        emprestimos_path = os.path.join("dados", "emprestimos.txt")
        with open(emprestimos_path, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 4:
                    codigo_emprestimo = dados[0]
                    codigo_usuario = dados[1]
                    codigo_livro = dados[2]
                    data = dados[3]

                    emprestimo = Emprestimo(
                        codigo_emprestimo, codigo_usuario, codigo_livro, data
                    )
                    emprestimos.append(emprestimo)
        return emprestimos

    def validar_usuario(self, login, senha):
        for usuario in self.usuarios:
            if usuario.login == login and usuario.validar_senha(senha):
                self.usuario_logado = usuario
                return True
        return False

    def exibir_menu(self):
        # Mostra as opções disponíveis para o usuário autenticado
        pass

    def listar_emprestimos(self):
        # Lista os empréstimos do usuário logado
        pass

    def listar_livros(self):
        # Lista todos os livros disponíveis
        pass
