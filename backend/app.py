from flask import Flask
from flask_cors import CORS
from src.controllers.resume_controller import ResumeController

def create_app():
    app = Flask(__name__)
    CORS(app)  # Permite CORS para requisições do frontend
    
    # Inicializar controller
    resume_controller = ResumeController()
    
    # Rota POST para gerar currículo personalizado
    @app.route('/api/generate-resume', methods=['POST'])
    def generate_resume():
        return resume_controller.generate_personalized_resume()
    
    # Rota de health check
    @app.route('/health', methods=['GET'])
    def health_check():
        return {'status': 'OK', 'message': 'API funcionando'}, 200
    
    return app

app = create_app()
