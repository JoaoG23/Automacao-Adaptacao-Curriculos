from flask import Blueprint, request, jsonify, send_file
import os
from src.services.resume_service import ResumeService
from dotenv import load_dotenv

load_dotenv()

resume_bp = Blueprint("resume_bp", __name__)


@resume_bp.route("/generate-resume", methods=["POST"])
def generate_resume():

    PATH_EXPORT = os.getenv("PATH_EXPORT")
    """
    Controller para gerar currículo personalizado
    Recebe descrição da vaga via JSON
    """
    try:
        data = request.get_json()

        if not data or "descricao_vaga" not in data:
            return jsonify({"message": 'Campo "descricao_vaga" é obrigatório'}), 400

        descricao_vaga = data["descricao_vaga"]
        result = ResumeService.generate_resume_personalized(descricao_vaga)
        # result = {
        #     "success": True,
        #     "data": {
        #         "docx_filename": "N:\\github\\Automacao-Adaptacao-Curriculos\\backend\\exports\\curriculo_joão_guilherme_teste.docx",
        #         "email": "jguilhermeempresarial@outlook.com",
        #         "message": "Currículo criado com sucesso!",
        #         "nome_candidato": "JOÃO GUILHERME",
        #         "pdf_filename": "N:\\github\\Automacao-Adaptacao-Curriculos\\backend\\exports\\curriculo_joão_guilherme_teste.pdf"
        #     },
        #     "message": "Currículo gerado com sucesso!"
        # }

        if result["success"]:
            return (
                send_file(
                    result["data"]["pdf_filename"],
                    mimetype="application/pdf",
                    as_attachment=True,
                ),
                201,
            )

        return (
            jsonify({"message": result.get("message", "Erro ao gerar currículo")}),
            500,
        )

    except Exception as e:
        return jsonify({"message": f"Erro interno do servidor: {str(e)}"}), 500


@resume_bp.route("/download/<filename>", methods=["GET"])
def download_resume(filename):
    """
    Controller para baixar o currículo gerado
    """
    try:
        directory = os.path.join(os.getcwd(), "exports")
        return send_from_directory(directory, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"message": f"Erro ao baixar arquivo: {str(e)}"}), 404
