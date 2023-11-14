from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Vantagem(db.Model):
    __tablename__ = "Vantagens"
    nome_vant = db.Column(db.String(120))
    id_ficha = db.Column(db.Integer, db.ForeignKey('Fichas.id_ficha', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    ficha = db.relationship('Ficha', back_populates='vantagens')

    def __init__(self, nome_vant, id_ficha):
        self.nome_vant = nome_vant
        self.id_ficha = id_ficha

    def to_dict(self):
        return {
            "nome_vant" : self.nome_vant,
            "id_ficha" : self.id_ficha
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
