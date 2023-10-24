class Tecnica:
    def __init__(self, id_tecnica, nome_tecnica,
                raridade, efeito,
                xp, custo, alcance,
                duracao, requisito,
                id_ficha
        ):
        self.id_tecnica = id_tecnica
        self.nome_tecnica = nome_tecnica
        self.raridade = raridade
        self.efeito = efeito
        self.xp = xp
        self.id_ficha = id_ficha
        self.custo = custo
        self.alcance = alcance
        self.duracao = duracao
        self.requisito = requisito

    def to_dict(self):
        return {
            "id_artefato" : self.id_artefato,
            "nome_artefato" : self.nome_artefato,
            "raridade" : self.raridade,
            "efeito" : self.efeito,
            "xp" : self.xp,
            "id_ficha" : self.id_ficha,
            "qualidade" : self.qualidade,
        }
