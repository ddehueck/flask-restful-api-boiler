from config import Config
from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS

cors = CORS()

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


def create_app(config_class=Config):
    app = Flask(__name__)

    cors.init_app(app, resources={r'*': {
            'origins': '*',
            'supports_credentials': True
        }
    })

    app.config.from_object(config_class)

    # Register blueprints from modules here!
    app.register_blueprint(api_bp)

    from app.subapp import bp as subapp_bp
    app.register_blueprint(subapp_bp)

    return app

