import requests

url_pesquisar_usuario = "http://127.0.0.1:5000/pesquisar_usuario"

email_usuario_a_pesquisar = "iiihaaaaa_emoteDeSertanejo@hotmail.com"

response = requests.get(f"{url_pesquisar_usuario}/{email_usuario_a_pesquisar}")

if response.status_code == 200:
    usuario = response.json()
    print("Dados do usuário:")
    print(f"Email: {usuario['email']}")
    print(f"Nome: {usuario['nome']}")
    print(f"Senha: {usuario['senha']}")
else:
    print("Erro ao pesquisar usuário:", response.text)
