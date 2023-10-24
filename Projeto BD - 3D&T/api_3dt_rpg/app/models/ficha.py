class Ficha:
    def __init_(
            self,
            id_ficha, nome,
            arquetipo, xp,
            poder, habilidade,
            resistencia, tipo_ficha, email_usuario,
        ):
        self.id_ficha = id_ficha
        self.nome = nome
        self.arquetipo = arquetipo
        self.xp = xp
        self.poder = poder
        self.habilidade = habilidade
        self.resistencia = resistencia
        self.tipo_ficha = tipo_ficha
        self.email_usuario = email_usuario

    def to_dict(self):
        return {
            "id_ficha": self.id_ficha,
            "nome": self.nome,
            "arquetipo": self.arquetipo,
            "xp": self.xp,
            "poder": self.poder,
            "habilidade": self.habilidade,
            "resistencia": self.resistencia,
            "tipo_ficha": self.tipo_ficha,
            "email_usuario": self.email_usuario
        }
