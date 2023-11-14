from flask import Blueprint, request, jsonify
from sqlalchemy.orm.exc import NoResultFound
from api_3dt_rpg_SQLAlchemy.app.models.ficha import Ficha
from api_3dt_rpg_SQLAlchemy.app.models.vantagem import Vantagem
from api_3dt_rpg_SQLAlchemy.app.models.desvantagem import Desvantagem
from api_3dt_rpg_SQLAlchemy.app.models.pericia import Pericia
from api_3dt_rpg_SQLAlchemy.app.database.database import db

ficha_bp = Blueprint('ficha', __name__)

@ficha_bp.route('/cadastrar_ficha', methods=['POST'])
def cadastrar_ficha_endpoint():
    data = request.get_json()
    id_ficha = data.get('id_ficha')
    nome = data['nome']
    tipo_ficha = data['tipo_ficha']
    id_mesa = data['id_mesa']
    arquetipo = data['arquetipo'] if tipo_ficha == "Player" else "Nenhum"
    xp = 100 if tipo_ficha == "Player" else 0
    poder = data['poder']
    habilidade = data['habilidade']
    resistencia = data['resistencia']
    email_usuario = data['email_usuario']
    id_veiculo = data.get('id_veiculo')

    if tipo_ficha not in ("Player", "Veiculo"):
        return jsonify({"erro": "Tipo de ficha inválido"}), 404

    ficha = Ficha(id_ficha = id_ficha, nome=nome, arquetipo=arquetipo, xp=xp, poder=poder, habilidade=habilidade,
                  resistencia=resistencia, tipo_ficha=tipo_ficha, email_usuario=email_usuario,
                  id_mesa=id_mesa, id_veiculo=id_veiculo)

    try:
        ficha.save()
        return jsonify({"message": "Ficha cadastrada com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@ficha_bp.route('/listar_fichas', methods=['GET'])
def listar_fichas_endpoint():
    try:
        fichas = Ficha.query.all()
        lista_fichas = []

        for ficha in fichas:
            ficha_dict = ficha.to_dict()

            lista_vantagens = [v.nome_vant for v in ficha.vantagens]
            lista_desvantagens = [d.nome_desvant for d in ficha.desvantagens]
            lista_pericias = [p.nome_pericia for p in ficha.pericias]

            ficha_dict["vantagens"] = lista_vantagens
            ficha_dict["desvantagens"] = lista_desvantagens
            ficha_dict["pericias"] = lista_pericias

            lista_fichas.append(ficha_dict)

        return jsonify({"fichas": lista_fichas})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@ficha_bp.route('/excluir_ficha/<int:id_ficha>', methods=['DELETE'])
def excluir_ficha(id_ficha):
    try:
        ficha = Ficha.query.get(id_ficha)
        if ficha:
            ficha.delete()
            return jsonify({"message": f"Ficha com ID {id_ficha} excluída com sucesso"})
        else:
            return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@ficha_bp.route('/atualizar_ficha/<int:id_ficha>', methods=['PUT'])
def atualizar_ficha(id_ficha):
    data = request.get_json()
    try:
        ficha = Ficha.query.get(id_ficha)
        if not ficha:
            return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404
        if 'id_ficha' in data:
            ficha.id_ficha = data['id_ficha']
        if 'nome' in data:
            ficha.nome = data['nome']
        if 'arquetipo' in data:
            ficha.arquetipo = data['arquetipo']
        if 'poder' in data:
            ficha.poder = data['poder']
        if 'habilidade' in data:
            ficha.habilidade = data['habilidade']
        if 'resistencia' in data:
            ficha.resistencia = data['resistencia']
        if 'tipo_ficha' in data:
            novo_tipo_ficha = data['tipo_ficha']
            if novo_tipo_ficha not in ['Player', 'Veiculo']:
                return jsonify({"message": "O tipo de ficha deve ser 'Player' ou 'Veiculo'"}), 400
            ficha.tipo_ficha = novo_tipo_ficha
        if 'email_usuario' in data:
            ficha.email_usuario = data['email_usuario']
        if 'id_mesa' in data:
            ficha.id_mesa = data['id_mesa']
        if 'id_veiculo' in data:
            ficha.id_veiculo = data['id_veiculo']

        ficha.save()
        return jsonify({"message": f"Ficha com ID {id_ficha} atualizada com sucesso"})
    except NoResultFound:
        return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@ficha_bp.route('/pesquisar_ficha/<nome>', methods=['GET'])
def pesquisar_ficha(nome):
    resultados = Ficha.query.filter(Ficha.nome.like(f"%{nome}%")).all()

    if resultados:
        fichas_dict = [ficha.to_dict() for ficha in resultados]
        return jsonify(fichas_dict), 200
    else:
        return jsonify({"message": "Nenhuma ficha encontrada"}), 404

@ficha_bp.route('/cadastrar_ficha/vantagem', methods=['POST'])
def cadastrar_vantagem_endpoint():
    data = request.get_json()
    id_ficha = data['id_ficha']
    nome_vant = data['nome']

    try:
        ficha = Ficha.query.get(id_ficha)
        if ficha:
            vantagem = Vantagem(nome_vant, id_ficha)
            ficha.vantagens.append(vantagem)
            vantagem.save()
            return jsonify({"message": "Vantagem cadastrada com sucesso!"})
        else:
            return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 404

@ficha_bp.route('/cadastrar_ficha/desvantagem', methods=['POST'])
def cadastrar_desvantagem_endpoint():
    data = request.get_json()
    id_ficha = data['id_ficha']
    nome_desv = data['nome']
    desvantagem = Desvantagem(nome_desvant=nome_desv, id_ficha=id_ficha)

    try:
        desvantagem.save()
        return jsonify({"message": "Desvantagem cadastrada com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404


@ficha_bp.route('/cadastrar_ficha/pericia', methods=['POST'])
def cadastrar_pericia_endpoint():
    data = request.get_json()
    id_ficha = data['id_ficha']
    nome_pericia = data['nome']
    pericia = Pericia(nome_pericia=nome_pericia, id_ficha=id_ficha)

    try:
        pericia.save()
        return jsonify({"message": "Perícia cadastrada com sucesso!"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 404


@ficha_bp.route('/excluir_vantagem/<int:id_ficha>/<nome_vantagem>', methods=['DELETE'])
def excluir_vantagem(id_ficha, nome_vantagem):
    try:
        ficha = Ficha.query.get(id_ficha)
        if not ficha:
            return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404

        vantagem = Vantagem.query.filter_by(nome_vant=nome_vantagem, id_ficha=ficha.id_ficha).first()
        if not vantagem:
            return jsonify({"erro": f"Vantagem {nome_vantagem} não encontrada na ficha com ID {id_ficha}"}), 404

        vantagem.delete()
        return jsonify({"message": f"Vantagem {nome_vantagem} excluída da ficha com ID {id_ficha} com sucesso"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@ficha_bp.route('/excluir_desvantagem/<int:id_ficha>/<nome_desvantagem>', methods=['DELETE'])
def excluir_desvantagem(id_ficha, nome_desvantagem):
    try:
        ficha = Ficha.query.get(id_ficha)
        if not ficha:
            return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404

        desvantagem = Desvantagem.query.filter_by(nome_desvant=nome_desvantagem, id_ficha=ficha.id_ficha).first()
        if not desvantagem:
            return jsonify({"erro": f"Desvantagem {nome_desvantagem} não encontrada na ficha com ID {id_ficha}"}), 404

        desvantagem.delete()
        return jsonify({"message": f"Desvantagem {nome_desvantagem} excluída da ficha com ID {id_ficha} com sucesso"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@ficha_bp.route('/excluir_pericia/<int:id_ficha>/<nome_pericia>', methods=['DELETE'])
def excluir_pericia(id_ficha, nome_pericia):
    try:
        ficha = Ficha.query.get(id_ficha)
        if not ficha:
            return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404

        pericia = Pericia.query.filter_by(nome_pericia=nome_pericia, id_ficha=ficha.id_ficha).first()
        if not pericia:
            return jsonify({"erro": f"Perícia {nome_pericia} não encontrada na ficha com ID {id_ficha}"}), 404

        pericia.delete()
        return jsonify({"message": f"Perícia {nome_pericia} excluída da ficha com ID {id_ficha} com sucesso"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
