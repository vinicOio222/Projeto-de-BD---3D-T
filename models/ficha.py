from database.database import db
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.exc import IntegrityError

class Ficha(db.Model):
    __tablename__ = "Fichas"
    id_ficha = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(120), nullable=False)
    arquetipo = db.Column(db.String(120), nullable=False)
    xp = db.Column(db.Integer, nullable=False)
    poder = db.Column(db.Integer, nullable=False)
    habilidade = db.Column(db.Integer, nullable=False)
    resistencia = db.Column(db.Integer, nullable=False)
    tipo_ficha = db.Column(db.String(120), nullable=False)
    email_usuario = db.Column(db.String(120), db.ForeignKey('Usuarios.email'), nullable=False)
    id_mesa = db.Column(db.Integer, db.ForeignKey('Mesas.id_mesa', ondelete='SET NULL', onupdate='CASCADE'), nullable=False)
    id_veiculo = db.Column(db.Integer, db.ForeignKey('Fichas.id_ficha', ondelete='SET NULL', onupdate='CASCADE'), nullable=True)

    usuario = db.relationship('Usuario', back_populates='fichas')
    mesa = db.relationship('Mesa', back_populates='fichas')
    veiculo = db.relationship('Ficha', back_populates='ficha_associada', remote_side=[id_veiculo])
    vantagens = db.relationship('Vantagem', back_populates='ficha', cascade="all, delete-orphan", single_parent=True)
    desvantagens = db.relationship('Desvantagem', back_populates='ficha', cascade="all, delete-orphan", single_parent=True)
    pericias = db.relationship('Pericia', back_populates='ficha', cascade="all, delete-orphan", single_parent=True)
    itens = db.relationship('Item', back_populates='fichas', cascade="all, delete-orphan", single_parent=True)
    ficha_associada = db.relationship('Ficha', back_populates='veiculo', remote_side=[id_ficha])

    __table_args__ = (
        CheckConstraint('tipo_ficha IN ("Player", "Veiculo")', name='check_tipo_ficha'),
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
        if self.tipo_ficha not in ['Player', 'Veiculo']:
            raise ValueError("O tipo de ficha deve ser 'Player' ou 'Veiculo'")
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def gastar_xp_ficha(self, xp):
        try:
            ficha = Ficha.query.get(self.id_ficha)

            if ficha.xp < xp:
                return False

            ficha.xp -= xp
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False
