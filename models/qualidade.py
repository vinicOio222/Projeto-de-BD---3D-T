from database.database import db

class Qualidade(db.Model):
    __tablename__ = "Qualidades"
    id_qualidade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_qualidade = db.Column(db.String(500), nullable=False)
    id_artefato = db.Column(db.Integer, db.ForeignKey('Artefatos.id_artefato', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    artefato = db.relationship('Artefato', back_populates='qualidades')

    def __init__(self, nome_qualidade, id_artefato):
        self.nome_qualidade = nome_qualidade
        self.id_artefato = id_artefato

    def to_dict(self):
        return {
            "id_qualidade": self.id_qualidade,
            "nome_qualidade": self.nome_qualidade,
            "id_artefato": self.id_artefato,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

