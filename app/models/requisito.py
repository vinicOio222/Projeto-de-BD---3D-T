from database.database import db

class Requisito(db.Model):
    __tablename__ = "Requisitos"
    id_requisito = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_requisito = db.Column(db.String(500), nullable=False)
    id_tecnica = db.Column(db.Integer, db.ForeignKey('Tecnicas.id_tecnica', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    tecnica = db.relationship('Tecnica', back_populates='requisitos')


    def __init__(self, nome_requisito, id_tecnica):
        self.nome_requisito = nome_requisito
        self.id_tecnica = id_tecnica


    def to_dict(self):
        return {
            "id_requisito": self.id_requisito,
            "nome_requisito": self.nome_requisito,
            "id_tecnica": self.id_tecnica,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
