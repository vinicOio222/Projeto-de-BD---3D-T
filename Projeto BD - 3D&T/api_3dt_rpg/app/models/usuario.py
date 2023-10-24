class Usuario:
    def __init__(self, email, nome, senha):
        self.email = email
        self.nome = nome
        self.senha = senha

    def to_dict(self):
        return {
            "email" : self.email,
            "nome" : self.nome,
            "senha" : self.senha
        }
