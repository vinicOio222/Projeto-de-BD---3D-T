from flask import Blueprint, request, jsonify
import sys

sys.path.append('.venv\api_3dt_rpg_SQLAlchemy')

from api_3dt_rpg_SQLAlchemy.app.models.ficha import Ficha
from api_3dt_rpg_SQLAlchemy.app.models.vantagem import Vantagem
from api_3dt_rpg_SQLAlchemy.app.models.desvantagem import Desvantagem
from api_3dt_rpg_SQLAlchemy.app.models.pericia import Pericia
from api_3dt_rpg_SQLAlchemy.app.models.artefato import Artefato
from api_3dt_rpg_SQLAlchemy.app.models.tecnica import Tecnica

from flask import Blueprint, request, jsonify
from api_3dt_rpg_SQLAlchemy.app.database.database import db
from api_3dt_rpg_SQLAlchemy.app.models.ficha import Ficha

ficha_bp = Blueprint('ficha_bp', __name__)

@ficha_bp.route('/cadastrar_ficha', methods=['POST'])
def cadastrar_ficha_endpoint():
    data = request.get_json()

    nova_ficha = Ficha(
        id_ficha=data['id_ficha'],
        nome=data['nome'],
        arquetipo=data['arquetipo'],
        xp=data['xp'],
        poder=data['poder'],
        habilidade=data['habilidade'],
        resistencia=data['resistencia'],
        tipo_ficha=data['tipo_ficha'],
        email_usuario=data['email_usuario'],
        id_mesa=data['id_mesa'],
        id_veiculo=data.get('id_veiculo')
    )

    nova_ficha.save()

    return jsonify(nova_ficha.to_dict()), 201

@ficha_bp.route('/listar_fichas', methods=['GET'])
def listar_fichas():
    fichas = Ficha.query.all()
    return jsonify([ficha.to_dict() for ficha in fichas]), 200

@ficha_bp.route('/pesquisar_ficha/<int:id_ficha>', methods=['GET'])
def obter_ficha(id_ficha):
    ficha = Ficha.query.get(id_ficha)
    if ficha is None:
        return jsonify({'error': 'Ficha não encontrada'}), 404
    return jsonify(ficha.to_dict()), 200

@ficha_bp.route('/atualizar_ficha/<int:id_ficha>', methods=['PUT'])
def atualizar_ficha(id_ficha):
    data = request.get_json()
    ficha = Ficha.query.get(id_ficha)
    if ficha is None:
        return jsonify({'error': 'Ficha não encontrada'}), 404

    ficha.nome = data.get('nome', ficha.nome)
    ficha.arquetipo = data.get('arquetipo', ficha.arquetipo)
    ficha.xp = data.get('xp', ficha.xp)
    ficha.poder = data.get('poder', ficha.poder)
    ficha.habilidade = data.get('habilidade', ficha.habilidade)
    ficha.resistencia = data.get('resistencia', ficha.resistencia)
    ficha.tipo_ficha = data.get('tipo_ficha', ficha.tipo_ficha)
    ficha.email_usuario = data.get('email_usuario', ficha.email_usuario)
    ficha.id_mesa = data.get('id_mesa', ficha.id_mesa)
    ficha.id_veiculo = data.get('id_veiculo', ficha.id_veiculo)

    ficha.save()

    return jsonify(ficha.to_dict()), 200

@ficha_bp.route('/excluir_ficha/<int:id_ficha>', methods=['DELETE'])
def deletar_ficha(id_ficha):
    ficha = Ficha.query.get(id_ficha)
    if ficha is None:
        return jsonify({'error': 'Ficha não encontrada'}), 404

    ficha.delete()

    return jsonify({'message': 'Ficha deletada com sucesso'}), 200

@ficha_bp.route('/fichas/<int:id_ficha>/vantagens', methods=['POST'])
def adicionar_vantagem(id_ficha):
    data = request.get_json()
    vantagem = Vantagem.query.get(data['id_vantagem'])
    if vantagem is None:
        return jsonify({'error': 'Vantagem não encontrada'}), 404

    ficha = Ficha.query.get(id_ficha)
    if ficha is None:
        return jsonify({'error': 'Ficha não encontrada'}), 404

    ficha.vantagens.append(vantagem)
    ficha.save()

    return jsonify(ficha.to_dict()), 200

@ficha_bp.route('/cadastrar_ficha/vantagem/<int:id_ficha>', methods=['POST'])
def adicionar_desvantagem(id_ficha):
    data = request.get_json()
    desvantagem = Desvantagem.query.get(data['id_desvantagem'])
    if desvantagem is None:
        return jsonify({'error': 'Desvantagem não encontrada'}), 404

    ficha = Ficha.query.get(id_ficha)
    if ficha is None:
        return jsonify({'error': 'Ficha não encontrada'}), 404

    ficha.desvantagens.append(desvantagem)
    ficha.save()

    return jsonify(ficha.to_dict()), 200

# @ficha_bp.route('/cadastrar_ficha/artefato', methods = ['POST'])
# def cadastrar_artefato_endpoint():
#     data = request.get_json()
#     id_artefato = data['id_item']
#     nome_artefato = data['nome']
#     raridade  = data['raridade']
#     efeito = data['efeito']
#     id_ficha = data['id_ficha']
#     xp_custo = data['xp_custo']
#     qualidades = data['qualidades']
#     artefato = Artefato(id_artefato, nome_artefato, raridade, efeito, xp_custo, id_ficha)
#     db = DataBase()
#     try:
#         query_A = "INSERT INTO Item (ID_Item, Nome_Item, Raridade, Efeito, ID_Ficha) VALUES (?, ?, ?, ?, ?)"
#         query_B = "INSERT INTO Artefato (ID_Item, XP) VALUES (?, ?)"
#         query_C = "INSERT INTO Qualidade (Nome, ID_Artefato) VALUES (?, ?)"
#         values_A = (artefato.id_artefato, artefato.nome_artefato, artefato.raridade, artefato.efeito, artefato.id_ficha)
#         values_B = (artefato.id_artefato, artefato.xp)
#         db.cursor.execute(query_A,values_A)
#         db.cursor.execute(query_B,values_B)

#         for qualidade in qualidades:
#             values_C = (qualidade , artefato.id_artefato)
#             db.cursor.execute(query_C, values_C)

#         db.conn.commit()
#         return jsonify({"message":"Artefato cadastrado com sucesso!"})
#     except Exception as e:
#         return jsonify({"erro" : str(e)}), 404

# @ficha_bp.route('/cadastrar_ficha/tecnica', methods = ['POST'])
# def cadastrar_tecnica_endpoint():
#     data = request.get_json()
#     id_tecnica = data['id_item']
#     nome_tecnica = data['nome']
#     raridade  = data['raridade']
#     efeito = data['efeito']
#     id_ficha = data['id_ficha']
#     xp_custo = data['xp_custo']
#     custo_PM = data['custo_PM']
#     alcance = data['alcance']
#     duracao = data['duracao']
#     requisitos = data['requisitos']
#     tecnica = Tecnica(id_tecnica, nome_tecnica, raridade, efeito, xp_custo, custo_PM, alcance, duracao, id_ficha)
#     db = DataBase()
#     try:
#         query_A = "INSERT INTO Item (ID_Item, Nome_Item, Raridade, Efeito, ID_Ficha) VALUES (?, ?, ?, ?, ?)"
#         query_B = "INSERT INTO Tecnica (ID_Item, XP, Custo, Alcance, Duracao) VALUES (?, ?, ?, ?, ?)"
#         query_C = "INSERT INTO Requisito (Nome,  ID_Requisito) VALUES (?, ?)"
#         values_A = (tecnica.id_tecnica, tecnica.nome_tecnica, tecnica.raridade, tecnica.efeito, tecnica.id_ficha)
#         values_B = (tecnica.id_tecnica, tecnica.xp, tecnica.custo, tecnica.alcance, tecnica.duracao)
#         db.cursor.execute(query_A,values_A)
#         db.cursor.execute(query_B,values_B)

#         for requisito in requisitos:
#             values_C = (requisito , tecnica.id_tecnica)
#             db.cursor.execute(query_C, values_C)

#         db.conn.commit()
#         return jsonify({"message":"Tecnica cadastrada com sucesso!"})
#     except Exception as e:
#         return jsonify({"erro" : str(e)}), 404

# @ficha_bp.route('/listar_fichas', methods=['GET'])
# def listar_ficha_endpoint():
#     db = DataBase()
#     try:
#         query = "SELECT * FROM Ficha"
#         db.cursor.execute(query)
#         fichas = db.cursor.fetchall()

#         lista_fichas = []
#         for ficha in fichas:
#             id_ficha, nome, arquetipo, xp, poder, habilidade, resistencia, tipo_ficha, email_usuario, id_mesa, id_veiculo = ficha
#             ficha_obj = Ficha(id_ficha, nome, arquetipo, xp, poder, habilidade, resistencia, tipo_ficha, email_usuario, id_mesa, id_veiculo)

#             query_vantagens = "SELECT Nome_Vant FROM Vantagem WHERE ID_Ficha = ? "
#             db.cursor.execute(query_vantagens, (id_ficha,))
#             vantagens = db.cursor.fetchall()

#             query_desvantagens = "SELECT nome_Desv FROM Desvantagem WHERE ID_Ficha = ?"
#             db.cursor.execute(query_desvantagens, (id_ficha,))
#             desvantagens = db.cursor.fetchall()

#             query_pericias = "SELECT Nome_Pericia FROM Pericia WHERE ID_Ficha = ?"
#             db.cursor.execute(query_pericias, (id_ficha,))
#             pericias = db.cursor.fetchall()

#             lista_vantagens = [v[0] for v in vantagens]
#             lista_desvantagens = [d[0] for d in desvantagens]
#             lista_pericias = [p[0] for p in pericias]

#             ficha_dict = ficha_obj.to_dict()
#             ficha_dict["vantagens"] = lista_vantagens
#             ficha_dict["desvantagens"] = lista_desvantagens
#             ficha_dict["pericias"] = lista_pericias

#             # Consultar itens da ficha
#             query_itens = "SELECT * FROM Item WHERE ID_Ficha = ?"
#             db.cursor.execute(query_itens, (id_ficha,))
#             itens = db.cursor.fetchall()

#             lista_itens = []
#             for item in itens:
#                 id_item, nome_item, raridade, efeito, id_ficha = item
#                 item_dict = {
#                     "ID_Item": id_item,
#                     "Nome_Item": nome_item,
#                     "Raridade": raridade,
#                     "Efeito": efeito,
#                     "ID_Ficha": id_ficha
#                 }
#                 lista_itens.append(item_dict)

#             ficha_dict["itens"] = lista_itens

#             lista_fichas.append(ficha_dict)

#         return jsonify({"fichas": lista_fichas})
#     except Exception as e:
#         return jsonify({"erro": str(e)}), 404


# @ficha_bp.route('/pesquisar_ficha/<nome>', methods = ['GET'])
# def pesquisar_ficha(nome):
#     db = DataBase()
#     query = "SELECT * FROM Ficha WHERE Nome = ?"
#     result = db.cursor.execute(query, (nome,)).fetchone()

#     if result is not None:
#         ficha_dict = {
#             "id_ficha" : result[0],
#             "nome": result[1],
#             "arquetipo" : result[2],
#             "poder" : result[3],
#             "habilidade" : result[4],
#             "resistencia" : result[5],
#             "id_mesa": result[6],
#             "tipo_ficha" : result[7],
#             "email_usuario" : result[8]
#         }

#         return jsonify(ficha_dict)
#     else:
#         return jsonify({"message":"Ficha não encontrada"}), 404


# @ficha_bp.route('/excluir_ficha/<id_ficha>', methods = ['DELETE'])
# def excluir_ficha(id_ficha):
#     db = DataBase()
#     try:
#         check_query = "SELECT 1 FROM Ficha WHERE ID_Ficha = ?"
#         db.cursor.execute(check_query, (id_ficha,))
#         exists = db.cursor.fetchone()

#         if exists:
#             delete_query = "DELETE FROM Ficha WHERE ID_Ficha = ?"
#             db.cursor.execute(delete_query, (id_ficha,))
#             db.conn.commit()

#             return jsonify({"message" : f"Ficha com nome {id_ficha} excluído com sucesso"})
#         else:
#             return jsonify({"erro": f"Ficha com nome {id_ficha} não encontrado"})
#     except Exception as e:
#         return jsonify({"erro" : str(e)}), 404

# @ficha_bp.route('/excluir_desvantagem/<int:id_ficha>/<nome>', methods=['DELETE'])
# def excluir_desvantagem(id_ficha, nome):
#     db = DataBase()
#     try:
#         check_ficha_query = "SELECT 1 FROM Ficha WHERE ID_Ficha = ?"
#         db.cursor.execute(check_ficha_query, (id_ficha,))
#         exists_ficha = db.cursor.fetchone()

#         if exists_ficha:
#             check_desvantagem_query = "SELECT 1 FROM Desvantagem WHERE ID_Ficha = ? AND nome_Desv = ?"
#             db.cursor.execute(check_desvantagem_query, (id_ficha, nome))
#             exists_desvantagem = db.cursor.fetchone()

#             if exists_desvantagem:
#                 delete_desvantagem_query = "DELETE FROM Desvantagem WHERE ID_Ficha = ? AND nome_Desv = ?"
#                 db.cursor.execute(delete_desvantagem_query, (id_ficha, nome))
#                 db.conn.commit()

#                 return jsonify({"message": f"Desvantagem '{nome}' excluída com sucesso da ficha com ID {id_ficha}"})
#             else:
#                 return jsonify({"erro": f"Desvantagem '{nome}' não encontrada na ficha com ID {id_ficha}"}), 404
#         else:
#             return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404
#     except Exception as e:
#         return jsonify({"erro": str(e)}), 404

# @ficha_bp.route('/excluir_vantagem/<int:id_ficha>/<nome>', methods=['DELETE'])
# def excluir_vantagem(id_ficha, nome):
#     db = DataBase()
#     try:
#         check_ficha_query = "SELECT 1 FROM Ficha WHERE ID_Ficha = ?"
#         db.cursor.execute(check_ficha_query, (id_ficha,))
#         exists_ficha = db.cursor.fetchone()

#         if exists_ficha:
#             check_vantagem_query = "SELECT 1 FROM Vantagem WHERE ID_Ficha = ? AND Nome_Vant = ?"
#             db.cursor.execute(check_vantagem_query, (id_ficha, nome))
#             exists_vantagem = db.cursor.fetchone()

#             if exists_vantagem:
#                 delete_vantagem_query = "DELETE FROM Vantagem WHERE ID_Ficha = ? AND Nome_Vant = ?"
#                 db.cursor.execute(delete_vantagem_query, (id_ficha, nome))
#                 db.conn.commit()

#                 return jsonify({"message": f"Vantagem '{nome}' excluída com sucesso da ficha com ID {id_ficha}"})
#             else:
#                 return jsonify({"erro": f"Vantagem '{nome}' não encontrada na ficha com ID {id_ficha}"}), 404
#         else:
#             return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404
#     except Exception as e:
#         return jsonify({"erro": str(e)}), 404

# @ficha_bp.route('/excluir_pericia/<int:id_ficha>/<nome>', methods=['DELETE'])
# def excluir_pericia(id_ficha, nome):
#     db = DataBase()
#     try:
#         check_ficha_query = "SELECT 1 FROM Ficha WHERE ID_Ficha = ?"
#         db.cursor.execute(check_ficha_query, (id_ficha,))
#         exists_ficha = db.cursor.fetchone()

#         if exists_ficha:
#             check_pericia_query = "SELECT 1 FROM Pericia WHERE ID_Ficha = ? AND Nome_Pericia = ?"
#             db.cursor.execute(check_pericia_query, (id_ficha, nome))
#             exists_pericia = db.cursor.fetchone()

#             if exists_pericia:
#                 delete_pericia_query = "DELETE FROM Pericia WHERE ID_Ficha = ? AND Nome_Pericia = ?"
#                 db.cursor.execute(delete_pericia_query, (id_ficha, nome))
#                 db.conn.commit()

#                 return jsonify({"message": f"Perícia '{nome}' excluída com sucesso da ficha com ID {id_ficha}"})
#             else:
#                 return jsonify({"erro": f"Perícia '{nome}' não encontrada na ficha com ID {id_ficha}"}), 404
#         else:
#             return jsonify({"erro": f"Ficha com ID {id_ficha} não encontrada"}), 404
#     except Exception as e:
#         return jsonify({"erro": str(e)}), 404

# @ficha_bp.route('/excluir_item/<id_item>', methods=['DELETE'])
# def excluir_item(id_item):
#     db = DataBase()
#     try:
#         check_item_query = "SELECT 1 FROM Item WHERE ID_Item = ?"
#         db.cursor.execute(check_item_query, (id_item,))
#         exists_item = db.cursor.fetchone()

#         if exists_item:
#             delete_item_query = "DELETE FROM Item WHERE ID_Item = ?"
#             db.cursor.execute(delete_item_query, (id_item,))
#             db.conn.commit()

#             return jsonify({"message": f"Item com ID {id_item} excluído com sucesso"})
#         else:
#             return jsonify({"erro": f"Item com ID {id_item} não encontrado"}), 404
#     except Exception as e:
#         return jsonify({"erro": str(e)}), 404

# @ficha_bp.route('/atualizar_ficha/<id_ficha>/<campo>', methods=['PUT'])
# def atualizar_ficha(id_ficha, campo):
#     data = request.get_json()
#     db = DataBase()

#     query = ""
#     values = (id_ficha,)

#     if campo == "nome" and 'nome' in data:
#         novo_nome = data['nome']
#         query = "UPDATE Ficha SET Nome = ? WHERE ID_Ficha = ?"
#         values = (novo_nome, id_ficha)
#     elif campo == "arquetipo" and 'arquetipo' in data:
#         novo_arquetipo = data['arquetipo']
#         query = "UPDATE Ficha SET Arquetipo = ? WHERE ID_Ficha = ?"
#         values = (novo_arquetipo, id_ficha)
#     elif campo == "poder" and 'poder' in data:
#         novo_poder = data['poder']
#         query = "UPDATE Ficha SET Poder = ? WHERE ID_Ficha = ?"
#         values = (novo_poder, id_ficha)
#     elif campo == "habilidade" and 'habilidade' in data:
#         nova_habilidade = data['habilidade']
#         query = "UPDATE Ficha SET Habilidade = ? WHERE ID_Ficha = ?"
#         values = (nova_habilidade, id_ficha)
#     elif campo == "resistencia" and 'resistencia' in data:
#         nova_resistencia = data['resistencia']
#         query = "UPDATE Ficha SET Resistencia = ? WHERE ID_Ficha = ?"
#         values = (nova_resistencia, id_ficha)
#     elif campo == "tipo_ficha" and 'tipo_ficha' in data:
#         novo_tipo_ficha = data['tipo_ficha']
#         query = "UPDATE Ficha SET Tipo_Ficha = ? WHERE ID_Ficha = ?"
#         values = (novo_tipo_ficha, id_ficha)
#     elif campo == "email_usuario" and 'email_usuario' in data:
#         novo_email_usuario = data['email_usuario']
#         query = "UPDATE Ficha SET Email_Usuario = ? WHERE ID_Ficha = ?"
#         values = (novo_email_usuario, id_ficha)
#     elif campo == "id_mesa" and 'id_mesa' in data:
#         novo_id_mesa = data['id_mesa']
#         query = "UPDATE Ficha SET ID_Mesa = ? WHERE ID_Ficha = ?"
#         values = (novo_id_mesa, id_ficha)
#     elif campo == "id_veiculo" and 'id_veiculo' in data:
#         novo_id_veiculo = data['id_veiculo']
#         query = "UPDATE Ficha SET ID_Veiculo = ? WHERE ID_Ficha = ?"
#         values = (novo_id_veiculo, id_ficha)
#     else:
#         return jsonify({"message": "Campo inválido ou dados ausentes"}), 404

#     if not query:
#         return jsonify({"message": "Nenhum campo a ser atualizado ou campo inválido"}), 400

#     try:
#         db.cursor.execute(query, values)
#         db.conn.commit()
#         return jsonify({"message": f"Campo {campo} da ficha com ID {id_ficha} atualizado com sucesso"})
#     except Exception as e:
#         return jsonify({"erro": str(e)}), 404
