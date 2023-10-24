import sys
sys.path.append('api_3dt_rpg')

from flask import Blueprint, request, jsonify
from models.usuario import Usuario
from controllers.DB_RPG import DataBase

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/cadastrar_usuario', methods = ['POST'])
def cadastrar_usuario_endpoint():
    data = request.get_json()
    email = data['email']
    nome = data['nome']
    senha = data['senha']
    usuario = Usuario(email, nome, senha)
    db = DataBase()
    try:
        query = "INSERT INTO Usuario (Email, Nome, Senha) VALUES (?, ?, ?)"
        values = (usuario.email, usuario.nome, usuario.senha)
        db.cursor.execute(query,values)
        db.conn.commit()
        return jsonify({"message":"Usuario cadastro com sucesso!"})
    except Exception as e:
        return jsonify({"erro" : str(e)})


@usuario_bp.route('/listar_usuarios', methods = ['GET'])
def listar_usuario_endpoint():
    db = DataBase()
    try:
        query = "SELECT Email, Nome, Senha FROM Usuario"
        db.cursor.execute(query)
        usuarios = db.cursor.fetchall()

        lista_usuarios = []
        for usuario in usuarios:
            email, nome, senha = usuario
            usuario_obj = Usuario(email, nome, senha)
            lista_usuarios.append(usuario_obj.to_dict())
        return jsonify({"usuarios" : lista_usuarios})
    except Exception as e:
        return jsonify({"erro" : str(e)})

@usuario_bp.route('/pesquisar_usuario/<email>', methods = ['GET'])
def pesquisar_usuario(email):
    db = DataBase()
    query = "SELECT * FROM Usuario WHERE Email = ?"
    result = db.cursor.execute(query, (email,)).fetchone()

    if result is not None:
        usuario_dict = {
            "email" : result[0],
            "nome" : result[1],
            "senha" : result[2]
        }

        return jsonify(usuario_dict)
    else:
        return jsonify({"message":"Usuario não encontrado"}), 404


@usuario_bp.route('/excluir_usuario/<email>', methods = ['DELETE'])
def excluir_usuario(email):
    db = DataBase()
    try:
        query = "DELETE FROM Usuario WHERE Email = ?"
        db.cursor.execute(query, (email,))
        db.conn.commit()

        return jsonify({"message" : f"Usuário com email {email} excluído com sucesso"})
    except Exception as e:
        return jsonify({"erro" : str(e)})

@usuario_bp.route('/atualizar_usuario/<email>/<campo>', methods=['PUT'])
def atualizar_usuario(email, campo):
    data = request.get_json()

    db = DataBase()
    query = ""
    values = ()

    if campo == "email" and 'email' in data:
        novo_email = data['email']
        query = "UPDATE Usuario SET Email = ? WHERE Email = ?"
        values = (novo_email, email)
    elif campo == "nome" and 'nome' in data:
        novo_nome = data['nome']
        query = "UPDATE Usuario SET Nome = ? WHERE Email = ?"
        values = (novo_nome, email)
    elif campo == "senha" and 'senha' in data:
        nova_senha = data['senha']
        query = "UPDATE Usuario SET Senha = ? WHERE Email = ?"
        values = (nova_senha, email)
    else:
        return jsonify({"message": "Campo inválido ou dados ausentes"}), 404

    db.cursor.execute(query, values)
    db.conn.commit()

    return jsonify({"message": f"Campo {campo} do usuário com email {email} atualizado com sucesso"})
