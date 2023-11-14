from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Pericia(db.Model):
    __tablename__ = "Pericias"
    nome_pericia = db.Column(db.String(120))
    id_ficha = db.Column(db.Integer, db.ForeignKey('Fichas.id_ficha', ondelete = "CASCADE", onupdate = "CASCADE"), nullable=False)

    ficha = db.relationship('Ficha', back_populates='pericias')

    def __init__(self, nome_pericia, id_ficha):
        self.nome_pericia = nome_pericia
        self.id_ficha = id_ficha

    def to_dict(self):
        return {
            "nome_pericia": self.nome_pericia,
            "id_ficha": self.id_ficha
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
