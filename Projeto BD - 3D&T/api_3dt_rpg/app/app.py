from flask import Flask
from controllers.usuario_controller import usuario_bp

app = Flask(__name__)

# Aqui estarão
# registradas as rotas
# que serão inicializadas na API
app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug = True)
