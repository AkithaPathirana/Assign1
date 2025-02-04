from flask import Flask
from .routes import task_bp

def create_app():
    app = Flask(__name__)

    # Register the blueprint
    app.register_blueprint(task_bp, url_prefix='/tasks')

    return app
