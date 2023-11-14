from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///.venv\api_3dt_rpg_SQLAlchemy\app\database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Usuario(db.Model):
    Email = db.Column(db.String(120), primary_key=True)
    Username = db.Column(db.String(120), unique=True, nullable=False)
    Nome = db.Column(db.String(120), unique=True, nullable=False)
    Senha = db.Column(db.String(120), nullable=False)

class Mesa(db.Model):
    Nome_Mesa = db.Column(db.String(120), nullable=False)
    ID_Mesa = db.Column(db.Integer, primary_key=True)
    Mestre = db.Column(db.String(120), db.ForeignKey('usuario.Email', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

class Ficha(db.Model):
    ID_Ficha = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(120), nullable=False)
    Arquetipo = db.Column(db.String(120))
    XP = db.Column(db.Integer, nullable=False)
    Poder = db.Column(db.Integer, nullable=False)
    Habilidade = db.Column(db.Integer, nullable=False)
    Resistencia = db.Column(db.Integer, nullable=False)
    Tipo_Ficha = db.Column(db.String(120), nullable=False, check_constraint="Tipo_Ficha IN ('Player', 'Veiculo')")
    Email_Usuario = db.Column(db.String(120), db.ForeignKey('usuario.Email', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    ID_Mesa = db.Column(db.Integer, db.ForeignKey('mesa.ID_Mesa', ondelete='SET NULL', onupdate='CASCADE'))
    ID_Veiculo = db.Column(db.Integer, db.ForeignKey('ficha.ID_Ficha', ondelete='CASCADE', onupdate='CASCADE'))

class Desvantagem(db.Model):
    nome_Desv = db.Column(db.String(120), nullable=False)
    ID_Ficha = db.Column(db.Integer, db.ForeignKey('ficha.ID_Ficha', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

class Vantagem(db.Model):
    Nome_Vant = db.Column(db.String(120), nullable=False)
    ID_Ficha = db.Column(db.Integer, db.ForeignKey('ficha.ID_Ficha', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

class Pericia(db.Model):
    Nome_Pericia = db.Column(db.String(120), primary_key=True)
    ID_Ficha = db.Column(db.Integer, db.ForeignKey('ficha.ID_Ficha', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

class Item(db.Model):
    ID_Item = db.Column(db.Integer, primary_key=True)
    Nome_Item = db.Column(db.String(120), nullable=False)
    Raridade = db.Column(db.String(120), nullable=False)
    Efeito = db.Column(db.String(120), nullable=False)
    ID_Ficha = db.Column(db.Integer, db.ForeignKey('ficha.ID_Ficha', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

class Artefato(db.Model):
    ID_Item = db.Column(db.Integer, db.ForeignKey('item.ID_Item', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    XP = db.Column(db.Integer, nullable=False)

class Tecnica(db.Model):
    ID_Item = db.Column(db.Integer, db.ForeignKey('item.ID_Item', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    XP = db.Column(db.Integer, nullable=False)
    Custo = db.Column(db.Integer, nullable=False)
    Alcance = db.Column(db.String(120), nullable=False)
    Duracao = db.Column(db.String(120), nullable=False)

class Qualidade(db.Model):
    Nome = db.Column(db.String(120), unique=True, nullable=False)
    ID_Artefato = db.Column(db.Integer, db.ForeignKey('artefato.ID_Item', ondelete='CASCADE', onupdate='CASCADE'))

class Requisito(db.Model):
    ID_Requisito = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(120), unique=True, nullable=False)
    ID_Tecnica = db.Column(db.Integer, db.ForeignKey('tecnica.ID_Item', ondelete='CASCADE', onupdate='CASCADE'))
