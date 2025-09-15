# API de Geração de Currículos Personalizados

## Instalação

1. Instale as dependências:
```bash
pipenv install
```

2. Ative o ambiente virtual:
```bash
pipenv shell
```

## Execução

Para rodar a API:
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

## Endpoints

### POST /api/generate-resume

Gera um currículo personalizado baseado na descrição da vaga.

**Request Body:**
```json
{
    "descricao_vaga": "Descrição da vaga de emprego"
}
```

**Response (Sucesso - 200):**
```json
{
    "message": "Currículo gerado com sucesso!",
    "data": {
        "nome_candidato": "Nome do Candidato",
        "email": "email@exemplo.com",
        "message": "Currículo criado com sucesso!"
    }
}
```

**Response (Erro - 400/500):**
```json
{
    "error": "Mensagem de erro"
}
```

### GET /health

Verifica se a API está funcionando.

**Response:**
```json
{
    "status": "OK",
    "message": "API funcionando"
}
```

## Teste

Para testar a API, execute:
```bash
python test_api.py
```

## Estrutura do Projeto

```
backend/
├── app.py                          # Aplicação Flask principal
├── src/
│   ├── controllers/
│   │   └── resume_controller.py    # Controller (MVC)
│   └── services/
│       └── resume_service.py       # Service layer
├── imports/                        # PDFs de entrada
├── exports/                        # Documentos gerados
└── templates/                      # Templates de prompt
```

## Exemplo de Uso com cURL

```bash
# Health check
curl -X GET http://localhost:5000/health

# Gerar currículo
curl -X POST http://localhost:5000/api/generate-resume \
  -H "Content-Type: application/json" \
  -d '{"descricao_vaga": "Desenvolvedor Python com experiência em Flask"}'
```

## Exemplo de Uso com JavaScript

```javascript
// Gerar currículo
fetch('http://localhost:5000/api/generate-resume', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        descricao_vaga: 'Desenvolvedor Python com experiência em Flask'
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Erro:', error));
```
