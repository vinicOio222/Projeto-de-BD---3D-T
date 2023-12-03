# Projeto-de-BD---3D-T
Projeto para a cadeira de Banco de Dados que funciona como um SGDB para armazenamento de informações sobre usuários, mesas e fichas do RPG 3D&T.

**Como usar a API Flask com SQLAlchemy**
1. Clone o repositório com o seguinte comando do git

       git clone https://github.com/vinicOio222/Projeto-de-BD---3D-T.git -b SQLAlchemy

2. Crie um ambiente virtual em Python

       python -m venv .venv

3. Inicialize o .venv dentro do workspace projeto

       .venv\Scripts\activate

4. Insira a pasta da API dentro do .venv e instale o Flask e suas dependências dentro ambiente

        pip install Flask
        pip install flask_sqlalchemy
        pip install flask_migrate
        pip install sqlalchemy
        pip install flask_cors

5. Vá até a pasta do app dentro da api (para isso o .venv tem que estar ativado)

       .venv\api_3dt_rpg_SQLAlchemy\app

**ATENÇÃO** -> A instrução 6 a seguir será somente necessária se não houver o arquivo .db e/ou a pasta **migrations** ou os mesmos forem deletados

6. Ajuste as migrações das tabelas no Banco de Dados

       flask db init
       flask db migrate
       flask db upgrade

7. Se tudo estiver configurado, inicialize a API Flask. Divirta-se :D

       flask run

* Devs:
  - Vinícius dos Santos
  - Kalil Henrique
  - Gabryella Santos
  - Lucas Holanda
