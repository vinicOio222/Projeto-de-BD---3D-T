from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Tecnica(db.Model):
    __tablename__ = "Tecnicas"
    id_tecnica = db.Column(db.Integer, db.ForeignKey('Itens.id_item', ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    xp = db.Column(db.Integer, nullable=False)
    custo = db.Column(db.Integer, nullable=False)
    alcance = db.Column(db.String(120), nullable=False)
    duracao = db.Column(db.String(120), nullable=False)

    requisitos = db.relationship('Requisito', back_populates='tecnica', cascade="all, delete-orphan", single_parent=True)
    item = db.relationship('Item', back_populates='tecnicas')

    def __init__(self,id_tecnica, xp, custo, alcance, duracao):
        self.id_tecnica = id_tecnica
        self.xp = xp
        self.custo = custo
        self.alcance = alcance
        self.duracao = duracao
        self.requisitos = []

    def to_dict(self):
        return {
            "id_tecnica": self.id_tecnica,
            "xp": self.xp,
            "custo": self.custo,
            "alcance": self.alcance,
            "duracao": self.duracao,
            "requisitos": [r.to_dict() for r in self.requisitos]
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
