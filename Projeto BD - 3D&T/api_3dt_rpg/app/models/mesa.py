class Mesa:
    def __init_(self, nome_mesa, id_mesa, email_usuario):
        self.nome_mesa = nome_mesa
        self.id_mesa = id_mesa
        self.email_usuaro = email_usuario

    def to_dict(self):
        return {
            "nome_mesa": self.nome_mesa,
            "id_mesa": self.id_mesa,
            "email_usuario": self.email_usuario
        }
