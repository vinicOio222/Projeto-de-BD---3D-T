class Pericia:
    def __init_(self, nome_pericia, id_ficha):
        self.nome_mesa = nome_pericia
        self.id_mesa = id_ficha

    def to_dict(self):
        return {
            "nome_mesa": self.nome_mesa,
            "id_ficha": self.id_ficha
        }
