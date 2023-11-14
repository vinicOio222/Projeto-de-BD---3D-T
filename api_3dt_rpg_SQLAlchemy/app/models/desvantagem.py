from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Desvantagem(db.Model):
    __tablename__ = "Desvantagens"
    id_desvant = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_desvant = db.Column(db.String(120), nullable = False)
    id_ficha = db.Column(db.Integer, db.ForeignKey('Fichas.id_ficha', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    ficha = db.relationship('Ficha', back_populates='desvantagens')

    def __init__(self, nome_desvant, id_ficha):
        self.nome_desvant = nome_desvant
        self.id_ficha = id_ficha

    def to_dict(self):
        return {
            "nome_desvant": self.nome_desvant,
            "id_ficha": self.id_ficha
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
