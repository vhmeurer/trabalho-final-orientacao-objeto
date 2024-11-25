from csv import excel
from datetime import date, timedelta

from SistemaBiblioteca import SistemaBiblioteca
from models.Emprestimo import Emprestimo
from models.Livro import Livro


def exibir_menu():
    print("\nMenu:")
    print("1. Visualizar Empréstimos")
    print("2. Visualizar Livros Disponíveis")
    print("3. Fazer Empréstimo")
    print("4. Cadastrar Livro")
    print("5. Sobre")
    print("6. Sair")


def livro_ja_emprestado(sistema, codigo_livro):
    """Verifica se o livro já foi emprestado para o usuário logado."""
    for emprestimo in sistema.emprestimos:
        if (emprestimo.codigo_usuario == sistema.usuario_logado.codigo and
                emprestimo.codigo_livro == codigo_livro):
            return True
    return False


def main():
    sistema = SistemaBiblioteca()
    print("Bem-vindo ao BW Library, o seu Sistema da Biblioteca !\n")

    login = input("Digite o login: ")
    senha = input("Digite a senha: ")

    if sistema.validar_usuario(login, senha):
        print(f"\nUsuário '{sistema.usuario_logado.nome}' já cadastrado")

        while True:
            exibir_menu()
            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                # Visualizar Empréstimos
                print("\nEmpréstimos realizados:")
                for emprestimo in sistema.emprestimos:
                    if (emprestimo.codigo_usuario ==
                            sistema.usuario_logado.codigo):
                        print(
                            f"Código Empréstimo: {emprestimo.codigo}, "
                            f"Código Livro: {emprestimo.codigo_livro}, "
                            f"Data de Devolução: {emprestimo.data_devolucao}"
                        )
                if not any(
                    emprestimo.codigo_usuario == sistema.usuario_logado.codigo
                    for emprestimo in sistema.emprestimos
                ):
                    print("Nenhum empréstimo realizado.")

            elif escolha == "2":
                # Visualizar Livros Disponíveis
                print("\nLivros disponíveis:")
                for livro in sistema.livros:
                    if not livro_ja_emprestado(sistema, livro.codigo):
                        print(
                            f"Código: {livro.codigo}, Nome: {livro.nome}",
                            f"Autor: {livro.autor}"
                        )
                if not any(not livro_ja_emprestado(sistema, livro.codigo)
                           for livro in sistema.livros):
                    print("Nenhum livro disponível para empréstimo.")

            elif escolha == "3":
                # Fazer Empréstimo
                codigo_livro = input("Digite o código do livro desejado: ")
                livro_encontrado = next(
                    (
                        livro for livro in sistema.livros
                        if livro.codigo == codigo_livro
                    ),
                    None,
                )

                if livro_encontrado:
                    if livro_ja_emprestado(sistema, livro_encontrado.codigo):
                        print("Você já emprestou este livro.")
                    else:
                        codigo_emprestimo = str(len(sistema.emprestimos) + 1)
                        data_emprestimo = date.today()
                        data_devolucao = data_emprestimo + timedelta(days=7)
                        novo_emprestimo = Emprestimo(
                            codigo_emprestimo,
                            sistema.usuario_logado.codigo,
                            livro_encontrado.codigo,
                            data_emprestimo,
                            data_devolucao
                        )
                        sistema.emprestimos.append(novo_emprestimo)
                        print(
                            f"Empréstimo realizado com sucesso! "
                            f"Código do empréstimo: {codigo_emprestimo} "
                            f"Devolução para o dia: {data_devolucao.strftime('%d/%m/%Y')}"
                        )
                else:
                    print("Livro não encontrado.")

            elif escolha == "4":
                livro = Livro("","","")
                codigo = input("Digite o codigo do livro:")

                if Livro.verificar_codigo(codigo):
                    print("Codigo existente")
                    break
                else:
                    livro.setCodigo(codigo)
                    livro.setNome(input("Digite o Nome do livro:"))
                    livro.setAutor(input("Digite o Autor do livro:"))
                    livro.salvar_livro()
                    print("Livro cadastrado com sucesso!")
                    break
                
            elif escolha == "5":
                print("Na BookWorms, acreditamos no poder transformador da leitura e do conhecimento. Fundada por um grupo de apaixonados por tecnologia e literatura, nossa missão é conectar pessoas ao universo dos livros por meio de soluções inovadoras e acessíveis.\nCombinando expertise em desenvolvimento de software com um profundo respeito pelo papel das bibliotecas na sociedade, criamos o BW Library, um sistema de empréstimos de livros projetado para simplificar a gestão e melhorar a experiência dos leitores.\nNosso compromisso é empoderar bibliotecas a alcançarem mais leitores, oferecendo ferramentas tecnológicas que promovem a eficiência, a inclusão e a cultura. Com cada projeto, buscamos reforçar nosso propósito: unir tecnologia e conhecimento para um futuro melhor.\nVenha fazer parte dessa jornada com a gente!\n\nDesenvolvido por:\nGabriel Mazilão Ferreira da Silva\nJoão Pedro Dutra Coutinho\nJoão Victor Alves Campos\nLuiz Eduardo Ferreira Netto\nRuan de Toledo Barros Lamarca\nVictor Hugo Meurer Ribeiro")

            elif escolha == "6":
                print("Saindo do sistema. Até logo!")
                break
            

            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("\nLogin ou senha incorretos.")


if __name__ == "__main__":
    main()
