#!/bin/bash

# Script de configuração inicial do projeto Moviendo
echo "🚀 Configurando projeto Moviendo..."

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Instale Python 3.8+ primeiro."
    exit 1
fi

# Verificar se Node.js está instalado
if ! command -v node &> /dev/null; then
    echo "❌ Node.js não encontrado. Instale Node.js 16+ primeiro."
    exit 1
fi

# Verificar se PostgreSQL está instalado
if ! command -v psql &> /dev/null; then
    echo "❌ PostgreSQL não encontrado. Instale PostgreSQL primeiro."
    exit 1
fi

echo "✅ Dependências do sistema verificadas"

# Configurar Backend
echo "📦 Configurando Backend Django..."
cd back

# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências Python
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Dependências Python instaladas"

# Criar banco de dados PostgreSQL
echo "🗄️ Configurando banco de dados..."
createdb moviendo_python_db 2>/dev/null || echo "Banco já existe ou erro na criação"

# Executar migrations
python manage.py makemigrations
python manage.py migrate

# Criar superuser (opcional)
echo "👤 Criando superuser (opcional - pressione Ctrl+C para pular)..."
python manage.py createsuperuser --noinput --username admin --email admin@moviendo.com 2>/dev/null || echo "Superuser já existe ou pulado"

echo "✅ Backend configurado"

# Configurar Frontend
echo "🎨 Configurando Frontend React..."
cd ../front

# Instalar dependências Node.js
npm install

echo "✅ Frontend configurado"

# Voltar para raiz
cd ..

echo "🎉 Projeto Moviendo configurado com sucesso!"
echo ""
echo "Para rodar o projeto:"
echo "1. Backend: cd back && source venv/bin/activate && python manage.py runserver"
echo "2. Frontend: cd front && npm run dev"
echo ""
echo "URLs:"
echo "- Backend API: http://localhost:8000"
echo "- Frontend: http://localhost:5173"
echo "- API Docs: http://localhost:8000/api/docs/"
echo "- Admin: http://localhost:8000/admin/"
