from flask import Flask
from .routes.planet_routes import planets_bp
from .db import db, migrate
from .models import planet


def create_app():
    app = Flask(__name__)

    app.register_blueprint(planets_bp)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/planets_development'

    db.init_app(app)
    migrate.init_app(app, db)
    return app
