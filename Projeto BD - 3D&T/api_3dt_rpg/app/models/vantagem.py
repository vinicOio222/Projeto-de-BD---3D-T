class Vantagem:
    def __init__(self, nome_vant, id_ficha):
        self.nome_vant = nome_vant
        self.id_ficha = id_ficha

    def to_dict(self):
        return {
            "nome_vant" : self.nome_vant,
            "id_ficha" : self.id_ficha
        }
