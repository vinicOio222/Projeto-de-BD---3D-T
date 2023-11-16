import os
from sqlalchemy import event, Engine
from flask import Flask, jsonify
from flask_migrate import Migrate
from api_3dt_rpg_SQLAlchemy.app.controllers.mesa_controller import mesa_bp
from api_3dt_rpg_SQLAlchemy.app.controllers.usuario_controller import usuario_bp
from api_3dt_rpg_SQLAlchemy.app.controllers.ficha_controller import ficha_bp
from api_3dt_rpg_SQLAlchemy.app.database.database import db

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database/3D&T.db')
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

@app.route('/')
def index():
    return jsonify({"message": "API 3D&T RPG - SQLAlchemy"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
