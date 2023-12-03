import os
from sqlalchemy import event, Engine
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from controllers.usuario_controller import usuario_bp
from controllers.mesa_controller import mesa_bp
from controllers.ficha_controller import ficha_bp
from database.database import db

path = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(path, 'database/3D&T.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

app.register_blueprint(usuario_bp)
app.register_blueprint(mesa_bp)
app.register_blueprint(ficha_bp)

migrate = Migrate(app, db)

CORS(app, origins=["http://localhost:3000"])

@app.route('/')
def index():
    return jsonify({"message": "API 3D&T RPG - SQLAlchemy"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
