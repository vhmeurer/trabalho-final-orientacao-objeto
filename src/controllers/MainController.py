from services.UsuarioService import UsuarioService
from services.LivroService import LivroService
from services.EmprestimoService import EmprestimoService

class MainController:
    def __init__(self):
        self.usuario_service = UsuarioService()
        self.livro_service = LivroService()
        self.emprestimo_service = EmprestimoService()
        self.usuario_logado = None

    def exibir_menu(self):
        print("\nMenu:")
        print("1. Visualizar Empréstimos")
        print("2. Visualizar Livros Disponíveis")
        print("3. Fazer Empréstimo")
        print("4. Cadastrar Livro")
        print("5. Sobre")
        print("6. Sair")

    def executar(self):
        print("Bem-vindo ao BW Library, o seu Sistema da Biblioteca!\n")
        login = input("Digite o login: ")
        senha = input("Digite a senha: ")

        self.usuario_logado = self.usuario_service.validar_usuario(login, senha)
        if self.usuario_logado:
            print(f"\nBem-vindo, {self.usuario_logado.nome}!")
            while True:
                self.exibir_menu()
                escolha = input("Escolha uma opção: ")

                match escolha:
                    case "1":
                        self.visualizar_emprestimos()
                    case "2":
                        self.visualizar_livros_disponiveis()
                    case "3":
                        self.fazer_emprestimo()
                    case "4":
                        self.cadastrar_livro()
                    case "5":
                        self.exibir_sobre()
                    case "6":
                        print("Saindo do sistema. Até logo!")
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")
        else:
            print("\nLogin ou senha incorretos.")

    def visualizar_emprestimos(self):
        emprestimos = self.emprestimo_service.listar_emprestimos(self.usuario_logado.codigo)
        if emprestimos:
            print("\nEmpréstimos realizados:")
            for emprestimo in emprestimos:
                print(f"Código: {emprestimo.codigo}, Livro: {emprestimo.codigo_livro}, "
                      f"Devolução: {emprestimo.data_devolucao}")
        else:
            print("Nenhum empréstimo realizado.")

    def visualizar_livros_disponiveis(self):
        livros = self.livro_service.listar_livros_disponiveis(self.usuario_logado.codigo)
        if livros:
            print("\nLivros disponíveis:")
            for livro in livros:
                print(f"Código: {livro.codigo}, Nome: {livro.nome}, Autor: {livro.autor}")
        else:
            print("Nenhum livro disponível para empréstimo.")

    def fazer_emprestimo(self):
        codigo_livro = input("Digite o código do livro desejado: ")
        sucesso, mensagem = self.emprestimo_service.realizar_emprestimo(
            self.usuario_logado.codigo, codigo_livro)
        print(mensagem)

    def cadastrar_livro(self):
        codigo = input("Digite o código do livro: ")
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")

        sucesso, mensagem = self.livro_service.cadastrar_livro(codigo, nome, autor)
        print(mensagem)

    def exibir_sobre(self):
        print("Na BookWorms, acreditamos no poder transformador da leitura e do conhecimento. Fundada por um grupo de apaixonados por tecnologia e literatura, nossa missão é conectar pessoas ao universo dos livros por meio de soluções inovadoras e acessíveis.\nCombinando expertise em desenvolvimento de software com um profundo respeito pelo papel das bibliotecas na sociedade, criamos o BW Library, um sistema de empréstimos de livros projetado para simplificar a gestão e melhorar a experiência dos leitores.\nNosso compromisso é empoderar bibliotecas a alcançarem mais leitores, oferecendo ferramentas tecnológicas que promovem a eficiência, a inclusão e a cultura. Com cada projeto, buscamos reforçar nosso propósito: unir tecnologia e conhecimento para um futuro melhor.\nVenha fazer parte dessa jornada com a gente!\n\nDesenvolvido por:\nGabriel Mazilão Ferreira da Silva\nJoão Pedro Dutra Coutinho\nJoão Victor Alves Campos\nLuiz Eduardo Ferreira Netto\nRuan de Toledo Barros Lamarca\nVictor Hugo Meurer Ribeiro")


if __name__ == "__main__":
    controller = MainController()
    controller.executar()
