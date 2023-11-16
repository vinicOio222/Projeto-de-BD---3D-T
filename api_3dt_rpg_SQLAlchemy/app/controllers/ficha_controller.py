from flask import Blueprint, request, jsonify
from sqlalchemy.orm.exc import NoResultFound
from api_3dt_rpg_SQLAlchemy.app.models.ficha import Ficha
from api_3dt_rpg_SQLAlchemy.app.models.vantagem import Vantagem
from api_3dt_rpg_SQLAlchemy.app.models.desvantagem import Desvantagem
from api_3dt_rpg_SQLAlchemy.app.models.pericia import Pericia
from api_3dt_rpg_SQLAlchemy.app.models.item import Item
from api_3dt_rpg_SQLAlchemy.app.models.artefato import Artefato
from api_3dt_rpg_SQLAlchemy.app.models.qualidade import Qualidade
from api_3dt_rpg_SQLAlchemy.app.models.tecnica import Tecnica
from api_3dt_rpg_SQLAlchemy.app.models.requisito import Requisito
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

            lista_itens = []

            for item in ficha.itens:
                item_dict = item.to_dict()

                artefato = Artefato.query.filter_by(id_artefato=item.id_item).first()
                if artefato:

                    qualidades = Qualidade.query.filter_by(id_artefato=artefato.id_artefato).all()
                    item_dict["qualidades"] = [q.nome_qualidade for q in qualidades]

                tecnica = Tecnica.query.filter_by(id_tecnica=item.id_item).first()
                if tecnica:
                    requisitos = Requisito.query.filter_by(id_tecnica=tecnica.id_tecnica).all()
                    item_dict["requisitos"] = [r.nome_requisito for r in requisitos]

                lista_itens.append(item_dict)

            ficha_dict["itens"] = lista_itens
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
        if 'xp' in data:
            ficha.xp = data['xp']

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

@ficha_bp.route('/cadastrar_ficha/artefato', methods=['POST'])
def cadastrar_artefato_endpoint():
    data = request.get_json()
    id_artefato = data.get('id_item')
    id_ficha = data['id_ficha']
    nome_artefato = data['nome_item']
    raridade = data['raridade']
    efeito = data['efeito']
    xp = data['xp']
    lista_qualidades = data.get('qualidades', [])

    ficha = Ficha.query.get(id_ficha)

    if not ficha.gastar_xp_ficha(xp):
            return jsonify({"erro": "XP insuficiente para adquirir artefato."}), 400

    try:
        novo_item = Item(id_item = id_artefato,id_ficha=id_ficha, nome_item=nome_artefato, raridade=raridade, efeito=efeito)
        novo_item.save()
        item = Item.query.filter_by(nome_item = nome_artefato).first()
        novo_artefato = Artefato(id_artefato = item.id_item, xp=xp)
        novo_artefato.save()

        for qualidade in lista_qualidades:
            nova_qualidade = Qualidade(nome_qualidade=qualidade, id_artefato=item.id_item)
            nova_qualidade.save()

        return jsonify({"message": "Artefato cadastrado com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify('erro' + str(e)), 404

@ficha_bp.route('/cadastrar_ficha/tecnica', methods=['POST'])
def cadastrar_tecnica_endpoint():
    data = request.get_json()
    id_tecnica = data.get('id_item')
    id_ficha = data['id_ficha']
    nome_tecnica = data['nome_item']
    raridade = data['raridade']
    efeito = data['efeito']
    xp = data['xp']
    custo = data['custo']
    alcance = data['alcance']
    duracao = data['duracao']
    lista_requisitos = data.get('requisitos', [])

    ficha = Ficha.query.get(id_ficha)

    if not ficha.gastar_xp_ficha(xp):
            return jsonify({"erro": "XP insuficiente para aprender técnica."}), 400

    try:
        novo_item = Item(id_item = id_tecnica,id_ficha=id_ficha, nome_item=nome_tecnica, raridade=raridade, efeito=efeito)
        novo_item.save()
        item = Item.query.filter_by(nome_item = nome_tecnica).first()
        nova_tecnica = Tecnica(id_tecnica = item.id_item, xp=xp, custo = custo, alcance = alcance, duracao = duracao)
        nova_tecnica.save()

        for requisito in lista_requisitos:
            novo_requisito = Requisito(nome_requisito=requisito, id_tecnica=item.id_item)
            novo_requisito.save()

        return jsonify({"message": "Tecnica cadastrada com sucesso!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify('erro' + str(e)), 404

@ficha_bp.route('/excluir_item/<int:id_ficha>/<nome_item>', methods=['DELETE'])
def excluir_item(id_ficha, nome_item):
    try:
        ficha = Ficha.query.get(id_ficha)
        if not ficha:
            return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404

        item = Item.query.filter_by(nome_item=nome_item, id_ficha=ficha.id_ficha).first()
        if not item:
            return jsonify({"erro": f"Item {nome_item} não encontrada na ficha com ID {id_ficha}"}), 404

        item.delete()
        return jsonify({"message": f"Item {nome_item} excluída da ficha com ID {id_ficha} com sucesso"})
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@ficha_bp.route('/atualizar_ficha/item/<int:id_ficha>/<int:id_item>', methods=['PUT'])
def atualizar_item_endpoint(id_ficha, id_item):
    data = request.get_json()
    nome_item = data.get('nome_item')
    raridade = data.get('raridade')
    efeito = data.get('efeito')
    tipo = data.get('tipo')
    xp = data.get('xp')
    custo = data.get('custo')
    alcance = data.get('alcance')
    duracao = data.get('duracao')
    lista_qualidades = data.get('qualidades', [])
    lista_requisitos = data.get('requisitos', [])

    try:
        item = Item.query.filter_by(id_ficha=id_ficha, id_item=id_item).first()

        if item:
            item.nome_item = nome_item
            item.raridade = raridade
            item.efeito = efeito

            if tipo == 'artefato':
                artefato = Artefato.query.filter_by(id_artefato=id_item).first()
                if artefato:
                    artefato.xp = xp

                    qualidades = Qualidade.query.filter_by(id_artefato=id_item).all()
                    for i, q in enumerate(qualidades):
                        if i < len(lista_qualidades):
                            q.nome_qualidade = lista_qualidades[i]
                        else:
                            nova_qualidade = Qualidade(nome_qualidade=lista_qualidades[i], id_artefato=id_item)
                            db.session.add(nova_qualidade)

            elif tipo == 'tecnica':
                tecnica = Tecnica.query.filter_by(id_tecnica=id_item).first()
                if tecnica:
                    tecnica.xp = xp
                    tecnica.custo = custo
                    tecnica.alcance = alcance
                    tecnica.duracao = duracao

                    requisitos = Requisito.query.filter_by(id_tecnica=id_item).all()
                    for i, r in enumerate(requisitos):
                        if i < len(lista_requisitos):
                            r.nome_requisito = lista_requisitos[i]
                        else:
                            novo_requisito = Requisito(nome_requisito=lista_requisitos[i], id_tecnica=id_item)
                            db.session.add(novo_requisito)

            db.session.commit()
            return jsonify({"message": f"Item {tipo} atualizado com sucesso!"}), 200

        else:
            return jsonify({"erro": "Item não encontrado ou falha na atualização."}), 404

    except Exception as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 404

