from services.UsuarioService import UsuarioService
from services.LivroService import LivroService
from services.EmprestimoService import EmprestimoService

def test_sistema_biblioteca():
    # Inicializa os serviços
    usuario_service = UsuarioService()
    livro_service = LivroService()
    emprestimo_service = EmprestimoService()

    # Teste: Listar Usuários
    print("Usuários carregados:")
    for usuario in usuario_service.usuarios:
        print(
            f"Código: {usuario.codigo}, Nome: {usuario.nome}, "
            f"Login: {usuario.login}, Senha: {usuario.senha}"
        )

    # Teste: Listar Livros
    print("\nLivros carregados:")
    for livro in livro_service.livros:
        print(f"Código: {livro.codigo}, Nome: {livro.nome}, Autor: {livro.autor}")

    # Teste: Listar Empréstimos
    print("\nEmpréstimos carregados:")
    for emprestimo in emprestimo_service.emprestimos:
        print(
            f"Código Empréstimo: {emprestimo.codigo}, "
            f"Código Livro: {emprestimo.codigo_livro}, "
            f"Data de Devolução: {emprestimo.data_devolucao}"
        )

if __name__ == "__main__":
    test_sistema_biblioteca()
