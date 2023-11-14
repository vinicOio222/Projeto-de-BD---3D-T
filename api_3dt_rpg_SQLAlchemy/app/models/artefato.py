class Artefato:
    def __init__(self, id_artefato, nome_artefato, raridade, efeito, xp, id_ficha):
        self.id_artefato = id_artefato
        self.nome_artefato = nome_artefato
        self.raridade = raridade
        self.efeito = efeito
        self.xp = xp
        self.id_ficha = id_ficha
        self.qualidades = []

    def to_dict(self):
        return {
            "id_artefato" : self.id_artefato,
            "nome_artefato" : self.nome_artefato,
            "raridade" : self.raridade,
            "efeito" : self.efeito,
            "xp" : self.xp,
            "id_ficha" : self.id_ficha,
            "qualidades" : self.qualidades
        }
