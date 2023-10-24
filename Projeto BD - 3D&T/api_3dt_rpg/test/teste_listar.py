import requests

url_listar_usuarios = "http://127.0.0.1:5000/listar_usuarios"

response = requests.get(url_listar_usuarios)

if response.status_code == 200:
    usuarios = response.json().get("usuarios", [])
    if usuarios:
        print("Usuários cadastrados:")
        for usuario in usuarios:
            print(f"Email: {usuario['email']}, Nome: {usuario['nome']},  Senha: {usuario['senha']}")
    else:
        print("Nenhum usuário cadastrado.")
else:
    print("Erro ao listar usuários:", response.text)
