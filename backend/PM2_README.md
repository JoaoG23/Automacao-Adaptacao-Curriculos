# 🚀 Deploy com PM2 - API de Currículos

Este guia explica como fazer o deploy da aplicação usando PM2 com Pipenv.

## 📋 Pré-requisitos

- Node.js (para PM2)
- Python 3.12
- Pipenv

## 🔧 Instalação

### 1. Instalar PM2 globalmente
```bash
npm install -g pm2
```

### 2. Instalar dependências Python
```bash
cd backend
pipenv install
```

## 🚀 Deploy

### Deploy Automático (Windows)
```bash
cd backend
start-pm2.bat
```

### Deploy Manual
```bash
cd backend

# Criar diretório de logs
mkdir logs

# Iniciar aplicação
pm2 start ecosystem.config.js --env production

# Salvar configuração
pm2 save
```

## 🔍 Comandos Úteis

### Ver status
```bash
pm2 status
```

### Ver logs
```bash
pm2 logs automacao-adaptacao-curriculos-backend
```

### Parar aplicação
```bash
pm2 stop automacao-adaptacao-curriculos-backend
```

### Reiniciar aplicação
```bash
pm2 restart automacao-adaptacao-curriculos-backend
```

### Deletar aplicação
```bash
pm2 delete automacao-adaptacao-curriculos-backend
```

### Monitoramento
```bash
pm2 monit
```

## 📊 Configuração

O arquivo `ecosystem.config.js` está configurado para:

- ✅ Usar **Pipenv** como interpretador
- ✅ Ambiente de **produção** por padrão
- ✅ **Auto-restart** em caso de falha
- ✅ **Logs** organizados em `./logs/`
- ✅ **Limite de memória** de 1GB
- ✅ **Restart automático** com delay de 4s

## 🌐 Acesso

- **API**: http://localhost:5000
- **Health Check**: http://localhost:5000/health
- **Endpoint**: POST http://localhost:5000/api/generate-resume

## 🔧 Variáveis de Ambiente

O PM2 carrega automaticamente as variáveis do Pipenv:

- `FLASK_ENV=production`
- `FLASK_APP=app.py`
- `PYTHONPATH=./backend`

## 📁 Estrutura de Logs

```
backend/
├── logs/
│   ├── err.log      # Logs de erro
│   ├── out.log      # Logs de saída
│   └── combined.log # Logs combinados
```

## 🛠️ Troubleshooting

### Aplicação não inicia
```bash
# Verificar logs
pm2 logs automacao-adaptacao-curriculos-backend

# Verificar se pipenv está funcionando
pipenv run python --version
```

### Problemas de dependências
```bash
# Reinstalar dependências
pipenv install --dev

# Verificar ambiente virtual
pipenv shell
```

### PM2 não encontra pipenv
```bash
# Verificar se pipenv está instalado
pipenv --version

# Instalar pipenv se necessário
pip install pipenv
```

## 🔄 Atualizações

Para atualizar a aplicação:

1. Parar: `pm2 stop automacao-adaptacao-curriculos-backend`
2. Atualizar código
3. Instalar novas dependências: `pipenv install`
4. Iniciar: `pm2 start ecosystem.config.js --env production`

## 📞 Suporte

Em caso de problemas:
1. Verificar logs: `pm2 logs`
2. Verificar status: `pm2 status`
3. Testar manualmente: `pipenv run python run.py`
