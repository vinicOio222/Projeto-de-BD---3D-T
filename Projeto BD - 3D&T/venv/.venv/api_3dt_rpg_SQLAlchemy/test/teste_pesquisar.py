import requests

url_pesquisar_ficha = "http://127.0.0.1:5000/pesquisar_ficha"

nome_ficha_a_pesquisar = "Cecilus Siegmund"

response = requests.get(f"{url_pesquisar_ficha}/{nome_ficha_a_pesquisar}")

if response.status_code == 200:
    ficha = response.json()
    print("Dados do ficha:")
    print(f"ID da Ficha: {ficha['id_ficha']}")
    print(f"Nome: {ficha['nome']}")
    print(f"E-mail: {ficha['email_usuario']}")
    print(f"Tipo da Ficha: {ficha['tipo_ficha']}")
    print(f"ID da Mesa: {ficha['id_mesa']} ")
else:
    print("Erro ao pesquisar ficha:", response.text)
