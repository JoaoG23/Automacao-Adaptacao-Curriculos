# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_generate_resume(client):
    data = {
        "descricao_vaga": "Desenvolvedor Python com experiência em Flask, APIs REST e processamento de documentos."
    }
    response = client.post("/api/generate-resume", json=data)

    assert response.status_code == 201
    json_data = response.get_json()


