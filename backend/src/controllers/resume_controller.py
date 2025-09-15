from flask import request, jsonify
from src.services.resume_service import ResumeService

class ResumeController:
    def __init__(self):
        self.resume_service = ResumeService()
    
    def generate_personalized_resume(self):
        """
        Controller para gerar currículo personalizado
        Recebe descrição da vaga via JSON
        """
        try:
            data = request.get_json()
            
            if not data or 'descricao_vaga' not in data:
                return jsonify({
                    'error': 'Campo "descricao_vaga" é obrigatório'
                }), 400
            
            descricao_vaga = data['descricao_vaga']
            
            result = self.resume_service.generate_resume_personalized(descricao_vaga)
            
            if result['success']:
                return jsonify({
                    'message': 'Currículo gerado com sucesso!',
                    'data': result['data']
                }), 200
            else:
                return jsonify({
                    'error': result['error']
                }), 400
                
        except Exception as e:
            return jsonify({
                'error': f'Erro interno do servidor: {str(e)}'
            }), 500
