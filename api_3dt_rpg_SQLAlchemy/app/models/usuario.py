from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Usuario(db.Model):
    __tablename__ = "Usuarios"
    email = db.Column(db.String(120), primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    nome = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

    mesas = db.relationship('Mesa', back_populates='mestre', cascade="all, delete-orphan")
    fichas = db.relationship('Ficha', back_populates='usuario', cascade="all, delete-orphan")

    def __init__(self, email, username, nome, senha):
        self.email = email
        self.username = username
        self.nome = nome
        self.senha = senha

    def to_dict(self):
        return {
            "email": self.email,
            "username": self.username,
            "nome": self.nome,
            "senha": self.senha
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
