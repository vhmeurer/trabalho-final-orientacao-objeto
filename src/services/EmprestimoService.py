from models.Emprestimo import Emprestimo
from datetime import date, timedelta
import os

class EmprestimoService:
    def __init__(self):
        self.emprestimos = self.carregar_emprestimos()

    def carregar_emprestimos(self):
        emprestimos = []
        emprestimos_path = os.path.join("dados", "emprestimos.txt")
        with open(emprestimos_path, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 4:
                    emprestimos.append(Emprestimo(*dados))
        return emprestimos

    def listar_emprestimos(self, codigo_usuario):
        return [e for e in self.emprestimos if e.codigo_usuario == codigo_usuario]

    def realizar_emprestimo(self, codigo_usuario, codigo_livro):
        for emprestimo in self.emprestimos:
            if emprestimo.codigo_usuario == codigo_usuario and emprestimo.codigo_livro == codigo_livro:
                return False, "Você já realizou o empréstimo deste livro."

        novo_emprestimo = Emprestimo(
            str(len(self.emprestimos) + 1),
            codigo_usuario,
            codigo_livro,
            date.today(),
            date.today() + timedelta(days=7)
        )
        self.emprestimos.append(novo_emprestimo)
        return True, "Empréstimo realizado com sucesso!"
