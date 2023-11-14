import sys
sys.path.append('api_3dt_rpg')

from flask import Blueprint, request, jsonify
from api_3dt_rpg_SQLAlchemy.app.models.mesa import Mesa
from api_3dt_rpg_SQLAlchemy.app.database.database import db

mesa_bp = Blueprint('mesa', __name__)

@mesa_bp.route('/cadastrar_mesa', methods=['POST'])
def cadastrar_mesa_endpoint():
    data = request.get_json()
    nome_mesa = data['nome_mesa']
    mestre_email = data['mestre_email']
    id_mesa = data['id_mesa']
    mesa = Mesa(nome_mesa=nome_mesa, id_mesa=id_mesa, mestre_email=mestre_email)

    try:
        mesa.save()
        return jsonify({"message": "Mesa cadastrada com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@mesa_bp.route('/listar_mesas', methods=['GET'])
def listar_mesas_endpoint():
    try:
        mesas = Mesa.query.all()
        lista_mesas = [mesa.to_dict() for mesa in mesas]
        return jsonify({"mesas": lista_mesas})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@mesa_bp.route('/excluir_mesa/<id_mesa>', methods=['DELETE'])
def excluir_mesa(id_mesa):
    try:
        mesa = Mesa.query.get(id_mesa)
        if mesa:
            mesa.delete()
            return jsonify({"message": f"Mesa com ID {id_mesa} excluída com sucesso"})
        else:
            return jsonify({"erro": f"Mesa com ID {id_mesa} não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 404
