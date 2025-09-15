from src.services.extract_text_from_pdf.extract_text_from_pdf import extract_text_from_pdf
from src.services.read_prompt_replace_resume.read_prompt_replace_resume import read_prompt_replace_resume
from src.services.extract_json_from_response.extract_json_from_response import extract_json_from_response
from src.services.create_document_pdf_and_docx.create_document_pdf_and_docx import create_document_pdf_and_docx       
from src.services.fetch_ia_and_generate_resume_personalized_json.fetch_ia_and_generate_resume_personalized_json import fetch_ia_and_generate_resume_personalized_json
from time import sleep
import json
class ResumeService:
    def __init__(self):
        self.pdf_path = 'imports/curriculo.pdf'
        self.prompt_path = 'templates/prompt_special.txt'
    
    def generate_resume_personalized(self, job_description):
        """
        Service para gerar currículo personalizado
        """
        try:
            # Extrair texto do PDF
            text = extract_text_from_pdf(self.pdf_path)
            
            # Ler prompt e substituir placeholder
            prompt = read_prompt_replace_resume(self.prompt_path, text)
            sleep(3)
            # Chamar IA para gerar resposta
            response_json = fetch_ia_and_generate_resume_personalized_json(job_description, prompt)
           
            # Extrair JSON da resposta
            parsed_json = extract_json_from_response(response_json)
            # print(json.dumps(parsed_json, indent=4))
            if parsed_json:
                # Criar documento
                sleep(1)
                create_document_pdf_and_docx(parsed_json)
                
                return {
                    'success': True,
                    'data': {
                        'nome_candidato': parsed_json.get('nome_candidato'),
                        'email': parsed_json.get('informacoes_contato', {}).get('email'),
                        'message': 'Currículo criado com sucesso!'
                    }
                }
            else:
                return {
                    'success': False,
                    'error': 'Erro ao extrair JSON da resposta da IA'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Erro no processamento: {str(e)}'
            }
