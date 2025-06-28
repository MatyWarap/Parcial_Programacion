from flask import Flask
from models.db import db
from config.config import DATABASE_CONNECTION_URI
from routes.musica_routes import cancion

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.register_blueprint(cancion)

db.init_app(app)

with app.app_context():
    from models.musica import Musica
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)