import requests

url_listar_fichas = "http://127.0.0.1:5000/listar_fichas"

response = requests.get(url_listar_fichas)

if response.status_code == 200:
    fichas = response.json().get("fichas", [])
    if fichas:
        print("Fichas Cadastradas:")
        for ficha in fichas:
            print(f"ID da Ficha: {ficha['id_ficha']}")
            print(f"Nome: {ficha['nome']}")
            print(f"Arquétipo: {ficha['arquetipo']}")
            print(f"Tipo da Ficha: {ficha['tipo_ficha']}")

            vantagens = ficha.get("vantagens", [])
            if vantagens:
                print("Vantagens:", vantagens)

            desvantagens = ficha.get("desvantagens", [])
            if desvantagens:
                print("Desvantagens:", desvantagens)

            pericias = ficha.get("pericias", [])
            if pericias:
                print("Pericias:", desvantagens)

            print("\n")

    else:
        print("Nenhuma ficha cadastrada.")
else:
    print("Erro ao listar fichas:", response.text)
