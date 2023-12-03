from flask import Blueprint, request, jsonify
from sqlalchemy import or_
from api_3dt_rpg_SQLAlchemy.app.models.usuario import Usuario

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario_endpoint():
    data = request.get_json()
    email = data['email']
    username = data['username']
    nome = data['nome']
    senha = data['senha']
    usuario = Usuario(email=email, username=username, nome=nome, senha=senha)
    try:
        usuario.save()
        return jsonify({"message": "Usuário cadastrado com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@usuario_bp.route('/listar_usuarios', methods=['GET'])
def listar_usuario_endpoint():
    try:
        usuarios = Usuario.query.all()
        lista_usuarios = [usuario.to_dict() for usuario in usuarios]
        return jsonify({"usuarios": lista_usuarios})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@usuario_bp.route('/pesquisar_usuario/<email>', methods=['GET'])
def pesquisar_usuario(email):
    usuario = Usuario.query.filter(Usuario.email.like(f'%{email}%')).first()
    if usuario is not None:
        usuario_dict = usuario.to_dict()
        return jsonify(usuario_dict), 200
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404


@usuario_bp.route('/excluir_usuario/<email>', methods=['DELETE'])
def excluir_usuario(email):
    usuario = Usuario.query.get(email)
    try:
        if usuario:
            usuario.delete()
            return jsonify({"message": f"Usuário com email {email} excluído com sucesso"}), 200
        else:
            return jsonify({"erro": f"Usuário com email {email} não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@usuario_bp.route('/atualizar_usuario/<email>', methods=['PUT'])
def atualizar_usuario(email):
    try:
        data = request.get_json()
        usuario = Usuario.query.get(email)
        if usuario:
            usuario.email = data.get('email', usuario.email)
            usuario.username = data.get('username', usuario.username)
            usuario.nome = data.get('nome', usuario.nome)
            usuario.senha = data.get('senha', usuario.senha)
            usuario.save()
            return jsonify({"message": f"Usuário com email {email} atualizado com sucesso"})
        else:
            return jsonify({"message": "Usuário não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 404
