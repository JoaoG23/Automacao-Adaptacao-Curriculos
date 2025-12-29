from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv
from src.controllers.resume_controller import resume_bp

# Load environment variables
load_dotenv()


def create_app():
    app = Flask(__name__)

    # Disable automatic slash redirects to prevent CORS issues
    app.url_map.strict_slashes = False

    # Configure CORS
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Register blueprints
    app.register_blueprint(resume_bp, url_prefix="/api")

    @app.route("/")
    def index():
        return {"message": "Automacao Adaptacao Curriculos API", "status": "running"}

    # Rota de health check
    @app.route("/health", methods=["GET"])
    def health_check():
        return {"status": "OK", "message": "API funcionando"}, 200

    return app


app = create_app()

