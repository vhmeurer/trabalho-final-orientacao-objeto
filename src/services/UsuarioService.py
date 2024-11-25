from models.Usuario import Usuario
import os

class UsuarioService:
    def __init__(self):
        self.usuarios = self.carregar_usuarios()

    def carregar_usuarios(self):
        usuarios = []
        usuarios_path = os.path.join("dados", "usuarios.txt")
        with open(usuarios_path, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 5:
                    usuarios.append(Usuario(*dados))
        return usuarios

    def validar_usuario(self, login, senha):
        for usuario in self.usuarios:
            if usuario.login == login and usuario.validar_senha(senha):
                return usuario
        return None
