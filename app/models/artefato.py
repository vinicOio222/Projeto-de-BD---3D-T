from database.database import db

class Artefato(db.Model):
    __tablename__ = "Artefatos"
    id_artefato = db.Column(db.Integer, db.ForeignKey('Itens.id_item', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    xp = db.Column(db.Integer, nullable=False)

    qualidades = db.relationship('Qualidade', back_populates='artefato', cascade="all, delete-orphan", single_parent=True)
    item = db.relationship('Item', back_populates='artefatos')


    def __init__(self, id_artefato, xp):
        self.xp = xp
        self.id_artefato = id_artefato
        self.qualidades = []

    def to_dict(self):
        return {
            "id_artefato": self.id_artefato,
            "xp": self.xp,
            "qualidades": [q.to_dict() for q in self.qualidades]
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
