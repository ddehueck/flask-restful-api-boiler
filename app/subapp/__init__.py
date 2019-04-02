from flask import Blueprint

bp = Blueprint('subapp', __name__)

from app.subapp import routes
