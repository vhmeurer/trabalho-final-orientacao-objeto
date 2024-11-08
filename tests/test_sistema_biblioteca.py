# teste_sistema_biblioteca.py

from ..src.SistemaBiblioteca import SistemaBiblioteca

# Cria uma instância do sistema
sistema = SistemaBiblioteca()

# Teste: Listar Usuários
print("Usuários carregados:")
for usuario in sistema.usuarios:
    print(
        f"Código: {usuario.codigo}, Nome: {usuario.nome}",
        f"Login: {usuario.login}, Senha: {usuario.senha}",
    )

# Teste: Listar Livros
print("\nLivros carregados:")
for livro in sistema.livros:
    print(f"Código: {livro.codigo}, Nome: {livro.nome}, Autor: {livro.autor}")

# Teste: Listar Empréstimos
print("\nEmpréstimos carregados:")
for emprestimo in sistema.emprestimos:
    print(
        f"Código Empréstimo: {emprestimo.codigo},"
        f"Código Livro: {emprestimo.codigo_livro}, Data: {emprestimo.data}"
    )
