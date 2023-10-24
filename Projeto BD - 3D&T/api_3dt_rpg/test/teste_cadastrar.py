import requests
import json

novo_usuario = {
    "email": "bilal_rodrigues@gmail.com",
    "nome": "Likak",
    "senha": "2003IhaveBigJiromba"
}

url_cadastro_usuario = "http://127.0.0.1:5000/cadastrar_usuario"

response = requests.post(url_cadastro_usuario, json=novo_usuario)

if response.status_code == 200:
    print("Usuário cadastrado com sucesso!")
else:
    print("Erro no cadastro do usuário:", response.text)
