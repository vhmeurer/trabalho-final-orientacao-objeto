import os

class Livro:
    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getCodigo(self):
        return self.codigo

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setAutor(self, autor):
        self.autor = autor

    def getAutor(self):
        return self.autor

    def salvar_livro(self):
        arquivo_path = os.path.join("dados", "livros.txt")
        with open(arquivo_path, "a") as arquivo:
            arquivo.write(f"{self.codigo};{self.nome};{self.autor}\n")

    @staticmethod
    def verificar_codigo(codigo):
        arquivo_path = os.path.join("dados", "livros.txt")
        # Verifica se o arquivo existe antes de tentar abrir
        if not os.path.exists(arquivo_path):
            return False

        with open(arquivo_path, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if dados[0] == codigo:  # O código do livro é o primeiro item
                    return True
        return False