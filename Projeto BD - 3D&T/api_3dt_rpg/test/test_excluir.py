import requests

url_excluir_usuario = "http://127.0.0.1:5000/excluir_usuario"

email_usuario_a_excluir = "novo_usuario@email.com"

response = requests.delete(f"{url_excluir_usuario}/{email_usuario_a_excluir}")

if response.status_code == 200:
    mensagem = response.json()
    print(mensagem)
else:
    print("Erro ao excluir usuário:", response.text)
