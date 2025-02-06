from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Регистрируем маршруты через Blueprint
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
