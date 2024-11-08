from SistemaBiblioteca import SistemaBiblioteca
from models.Emprestimo import Emprestimo


def exibir_menu():
    print("\nMenu:")
    print("1. Visualizar Empréstimos")
    print("2. Visualizar Livros Disponíveis")
    print("3. Fazer Empréstimo")
    print("4. Sair")


def livro_ja_emprestado(sistema, codigo_livro):
    """Verifica se o livro já foi emprestado para o usuário logado."""
    for emprestimo in sistema.emprestimos:
        if (emprestimo.codigo_usuario == sistema.usuario_logado.codigo and
                emprestimo.codigo_livro == codigo_livro):
            return True
    return False


def main():
    sistema = SistemaBiblioteca()
    print("Bem-vindo ao Sistema da Biblioteca!\n")

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
                            f"Data: {emprestimo.data}"
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
                        data_emprestimo = "2024-11-05"
                        novo_emprestimo = Emprestimo(
                            codigo_emprestimo,
                            sistema.usuario_logado.codigo,
                            livro_encontrado.codigo,
                            data_emprestimo,
                        )
                        sistema.emprestimos.append(novo_emprestimo)
                        print(
                            f"Empréstimo realizado com sucesso! "
                            f"Código do empréstimo: {codigo_emprestimo}"
                        )
                else:
                    print("Livro não encontrado.")

            elif escolha == "4":
                print("Saindo do sistema. Até logo!")
                break

            else:
                print("Opção inválida. Tente novamente.")
    else:
        print("\nLogin ou senha incorretos.")


if __name__ == "__main__":
    main()
