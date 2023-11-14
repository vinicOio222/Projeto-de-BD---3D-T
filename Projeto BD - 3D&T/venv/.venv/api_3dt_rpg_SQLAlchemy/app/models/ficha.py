from sqlalchemy import CheckConstraint
from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Ficha(db.Model):
    __tablename__ = "Fichas"
    id_ficha = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    arquetipo = db.Column(db.String(120), nullable=False)
    xp = db.Column(db.Integer, nullable=False)
    poder = db.Column(db.Integer, nullable=False)
    habilidade = db.Column(db.Integer, nullable=False)
    resistencia = db.Column(db.Integer, nullable=False)
    tipo_ficha = db.Column(db.String(120), nullable=False)
    email_usuario = db.Column(db.String(120), db.ForeignKey('Usuarios.email'), nullable=False)
    id_mesa = db.Column(db.Integer, db.ForeignKey('Mesas.id_mesa', ondelete = 'SET NULL', onupdate = "CASCADE"), nullable=False)
    id_veiculo = db.Column(db.Integer)

    usuario = db.relationship('Usuario', back_populates='fichas')
    mesa = db.relationship('Mesa', back_populates='fichas')
    veiculo = db.relationship('Veiculo', back_populates='fichas')

    __table_args__ = (
        CheckConstraint(tipo_ficha.in_(['Player', 'Veiculo']), name='check_tipo_ficha'),
    )

    def __init__(self, id_ficha, nome, arquetipo, xp, poder,
                 habilidade, resistencia, tipo_ficha, email_usuario,
                 id_mesa, id_veiculo):
        self.id_ficha = id_ficha
        self.nome = nome
        self.arquetipo = arquetipo
        self.xp = xp
        self.poder = poder
        self.habilidade = habilidade
        self.resistencia = resistencia
        self.tipo_ficha = tipo_ficha
        self.email_usuario = email_usuario
        self.id_mesa = id_mesa
        self.id_veiculo = id_veiculo

    def to_dict(self):
        return {
            "id_ficha": self.id_ficha,
            "nome": self.nome,
            "arquetipo": self.arquetipo,
            "xp": self.xp,
            "poder": self.poder,
            "habilidade": self.habilidade,
            "resistencia": self.resistencia,
            "tipo_ficha": self.tipo_ficha,
            "email_usuario": self.email_usuario,
            "id_mesa": self.id_mesa,
            "id_veiculo": self.id_veiculo
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
