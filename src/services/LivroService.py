from models.Livro import Livro
import os

class LivroService:
    def __init__(self):
        self.livros = self.carregar_livros()

    def carregar_livros(self):
        livros = []
        livros_path = os.path.join("dados", "livros.txt")
        with open(livros_path, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 3:
                    livros.append(Livro(*dados))
        return livros

    def listar_livros_disponiveis(self, codigo_usuario):
        return [livro for livro in self.livros if not livro.verificar_codigo(codigo_usuario)]

    def cadastrar_livro(self, codigo, nome, autor):
        if any(livro.codigo == codigo for livro in self.livros):
            return False, "Código do livro já existe."
        novo_livro = Livro(codigo, nome, autor)
        self.livros.append(novo_livro)
        return True, "Livro cadastrado com sucesso!"
