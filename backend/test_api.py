import requests
import json

def test_generate_resume():
    """
    Função para testar a API
    """
    url = "http://localhost:5000/api/generate-resume"
    
    # Dados de exemplo
    data = {
        "descricao_vaga": "Desenvolvedor Python com experiência em Flask, APIs REST e processamento de documentos. Conhecimento em IA e automação de processos."
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor. Certifique-se de que a API está rodando.")
    except Exception as e:
        print(f"Erro: {str(e)}")

def test_health_check():
    """
    Função para testar o health check
    """
    url = "http://localhost:5000/health"
    
    try:
        response = requests.get(url)
        print(f"Health Check - Status Code: {response.status_code}")
        print(f"Health Check - Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
        
    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor. Certifique-se de que a API está rodando.")
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    print("=== Testando Health Check ===")
    test_health_check()
    print("\n=== Testando Geração de Currículo ===")
    test_generate_resume()
