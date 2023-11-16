from api_3dt_rpg_SQLAlchemy.app.database.database import db

class Item(db.Model):
    __tablename__ = "Itens"
    id_item = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_item = db.Column(db.String(120), nullable=False)
    raridade = db.Column(db.String(120), nullable=False)
    efeito = db.Column(db.String(3500), nullable=False)
    id_ficha = db.Column(db.Integer, db.ForeignKey('Fichas.id_ficha', ondelete="CASCADE", onupdate="CASCADE"), nullable=False)

    fichas = db.relationship('Ficha', back_populates='itens')
    artefatos = db.relationship('Artefato', back_populates='item', cascade="all, delete-orphan", uselist=False, single_parent=True)
    tecnicas = db.relationship('Tecnica', back_populates='item', cascade="all, delete-orphan", uselist=False, single_parent=True)

    def __init__(self, id_item, id_ficha, nome_item, raridade, efeito):
        self.id_item = id_item
        self.id_ficha = id_ficha
        self.nome_item = nome_item
        self.raridade = raridade
        self.efeito = efeito

    def to_dict(self):
        return {
            "id_item": self.id_item,
            "id_ficha": self.id_ficha,
            "nome_item": self.nome_item,
            "raridade": self.raridade,
            "efeito": self.efeito
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

