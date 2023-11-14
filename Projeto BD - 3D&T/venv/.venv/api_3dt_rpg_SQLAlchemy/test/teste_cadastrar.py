import requests

novo_elemento = {
    "id_ficha": 1,
    "nome": "Cecilus Siegmund",
    "arquetipo": "Humano",
    "poder": "2",
    "habilidade": "3",
    "resistencia": "3",
    "tipo_ficha": "Player",
    "email_usuario": "vinicoios@gmail.com",
    "id_mesa": 3465,
}

# novo_elemento = {
#     "email": "vinicoios@gmail.com",
#     "username": "Vinicoios",
#     "nome" : "Vinícius dos Santos",
#     "senha": "vini290903"
# }

# novo_elemento = {
#     "email": "kalil_rodrigues@gmail.com",
#     "username": "Kamodres",
#     "nome" : "Kalil Henrique",
#     "senha": "kalil123"
# }

novo_elemento = {
    "nome_mesa" : "Sol Vermelho",
    "id_mesa" : "3465",
    "mestre": "kalil_rodrigues@gmail.com",
}

novo_elemento = {
    "id_ficha" : "1",
    "nome" : "Alcance"
}

# novo_elemento = {
#     "id_ficha" : "1",
#     "nome" : "Ambiente"

# }

novo_elemento = {
    "id_ficha":"1",
    "nome" : "Artefato"
}

novo_elemento = {
    "id_item": 1,
    "nome": "Espada do Rei",
    "raridade": "Lendária",
    "efeito": "Arma",
    "id_ficha": 1,
    "xp_custo": 50,
    "qualidades": ["Afiada", "+Dano", "Rigidez"]
}

novo_elemento = {
    "id_item": 2,
    "nome": "Dobra Elemento",
    "raridade": "Lendária",
    "efeito": "Técnica",
    "id_ficha": 1,
    "xp_custo": 50,
    "custo_PM": 1,
    "alcance": "Perto",
    "duracao": "Instantanea",
    "requisitos": ["Magia", "Mística"]
}
url_cadastro = "http://127.0.0.1:5000/cadastrar_ficha/tecnica"

response_player = requests.post(url_cadastro, json= novo_elemento)

if response_player.status_code == 200:
    print("Elemento cadastrado com sucesso!")
else:
    print("Erro no cadastro:", response_player.text)

