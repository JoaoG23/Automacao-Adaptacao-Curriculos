from flask import Blueprint, request, jsonify, send_file, send_from_directory
import os
from src.services.resume_service import ResumeService
from dotenv import load_dotenv

load_dotenv()

resume_bp = Blueprint("resume_bp", __name__)


@resume_bp.route("/generate-resume", methods=["POST"])
def generate_resume():
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

        if result["success"]:
            # Extrair apenas o nome do arquivo para o frontend
            pdf_filename = os.path.basename(result["data"]["pdf_filename"])
            docx_filename = os.path.basename(result["data"]["docx_filename"])

            return (
                jsonify(
                    {
                        "message": "Currículo gerado com sucesso!",
                        "pdf": pdf_filename,
                        "docx": docx_filename,
                    }
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
        # Tenta usar PATH_EXPORT da env, senão usa o padrão /exports
        directory = os.getenv("PATH_EXPORT")
        if not directory:
            directory = os.path.join(os.getcwd(), "exports")

        return send_from_directory(directory, filename, as_attachment=True)
    except Exception as e:
        return jsonify({"message": f"Erro ao baixar arquivo: {str(e)}"}), 404
