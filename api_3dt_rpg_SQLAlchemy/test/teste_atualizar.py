import requests

url_atualizar_campo_ficha = "http://127.0.0.1:5000/atualizar_ficha"

id_ficha_a_atualizar = "1"  # Substitua pelo ID da ficha que deseja atualizar

campo_para_atualizar = "id_mesa"

dados_de_atualizacao = {}

if campo_para_atualizar == "nome":
    dados_de_atualizacao['nome'] = 'Cecilus Siegmund'
elif campo_para_atualizar == "arquetipo":
    dados_de_atualizacao['arquetipo'] = 'Humano'
elif campo_para_atualizar == "poder":
    dados_de_atualizacao['poder'] = 5  # Substitua pelo novo valor do poder
elif campo_para_atualizar == "habilidade":
    dados_de_atualizacao['habilidade'] = 4  # Substitua pelo novo valor de habilidade
elif campo_para_atualizar == "resistencia":
    dados_de_atualizacao['resistencia'] = 6  # Substitua pelo novo valor de resistência
elif campo_para_atualizar == "tipo_ficha":
    dados_de_atualizacao['tipo_ficha'] = 'Veiculo'
elif campo_para_atualizar == "email_usuario":
    dados_de_atualizacao['email_usuario'] = 'novoemail@gmail.com'
elif campo_para_atualizar == "id_mesa":
    dados_de_atualizacao['id_mesa'] = "3465"  # Substitua pelo novo ID de mesa
elif campo_para_atualizar == "id_veiculo":
    dados_de_atualizacao['id_veiculo'] = 2  # Substitua pelo novo ID de veículo

response = requests.put(f"{url_atualizar_campo_ficha}/{id_ficha_a_atualizar}/{campo_para_atualizar}", json=dados_de_atualizacao)

if response.status_code == 200:
    mensagem = response.json()
    print(mensagem)
else:
    print("Erro ao atualizar campo da ficha:", response.text)
