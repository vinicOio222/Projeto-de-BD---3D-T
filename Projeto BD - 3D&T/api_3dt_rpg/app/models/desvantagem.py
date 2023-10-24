class Desvantagem:
    def __init__(self, nome_desvant, id_ficha):
        self.nome_desvant = nome_desvant
        self.id_ficha = id_ficha

    def to_dict(self):
        return {
            "nome_desvant" : self.nome_desvant,
            "id_ficha" : self.id_ficha
        }
