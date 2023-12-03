from database.database import db

class Mesa(db.Model):
    __tablename__ = "Mesas"
    nome_mesa = db.Column(db.String(120), nullable=False)
    id_mesa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mestre_email = db.Column(db.String(120), db.ForeignKey('Usuarios.email', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    mestre = db.relationship('Usuario', back_populates='mesas')
    fichas = db.relationship('Ficha', back_populates='mesa', cascade="all, delete-orphan")


    def __init__(self, nome_mesa, id_mesa, mestre_email):
        self.nome_mesa = nome_mesa
        self.id_mesa = id_mesa
        self.mestre_email = mestre_email

    def to_dict(self):
        return {
            "nome_mesa": self.nome_mesa,
            "id_mesa": self.id_mesa,
            "mestre_email" : self.mestre_email
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
