import requests

url_atualizar_campo_usuario = "http://127.0.0.1:5000/atualizar_usuario"

email_usuario_a_atualizar = "bilal_rodrigues@gmail.com"

campo_para_atualizar = "email"

dados_de_atualizacao = {}

if campo_para_atualizar == "email":
    dados_de_atualizacao['email'] = 'iiihaaaaa_emoteDeSertanejo@hotmail.com'
elif campo_para_atualizar == "nome":
    dados_de_atualizacao['nome'] = 'Bilal'
elif campo_para_atualizar == "senha":
    dados_de_atualizacao['senha'] = 'KillLaKill9723'

response = requests.put(f"{url_atualizar_campo_usuario}/{email_usuario_a_atualizar}/{campo_para_atualizar}", json=dados_de_atualizacao)

if response.status_code == 200:
    mensagem = response.json()
    print(mensagem)
else:
    print("Erro ao atualizar campo do usuário:", response.text)
