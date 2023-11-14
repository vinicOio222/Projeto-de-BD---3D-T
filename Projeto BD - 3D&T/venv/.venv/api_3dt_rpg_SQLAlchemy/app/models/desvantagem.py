from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Desvantagem(db.Model):
    __tablename__ = "Desvantagens"
    nome_desvant = db.Column(db.String(120), primary_key=True)
    id_ficha = db.Column(db.Integer, db.ForeignKey('Fichas.id_ficha', ondelete = "CASCADE", onupdate = "CASCADE"), nullable=False)

    ficha = db.relationship('Ficha', back_populates='desvantagens', cascade = "all, delete-orphan")

    def __init__(self, nome_desvant, id_ficha):
        self.nome_desvant = nome_desvant
        self.id_ficha = id_ficha

    def to_dict(self):
        return {
            "nome_desvant" : self.nome_desvant,
            "id_ficha" : self.id_ficha
        }

    def save():
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
