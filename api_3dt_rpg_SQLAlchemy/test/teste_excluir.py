import requests

url_excluir_ficha = "http://127.0.0.1:5000/excluir_mesa"

id_ficha = "3465"
# nome = "Dobra Elemento"

response = requests.delete(f"{url_excluir_ficha}/{id_ficha}")

if response.status_code == 200:
    mensagem = response.json()
    print(mensagem)
else:
    print("Erro ao excluir elemento:", response.text)
