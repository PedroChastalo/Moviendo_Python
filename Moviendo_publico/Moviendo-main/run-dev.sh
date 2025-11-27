#!/bin/bash

# Script para rodar o projeto em modo desenvolvimento
echo "🚀 Iniciando projeto Moviendo em modo desenvolvimento..."

# Função para matar processos ao sair
cleanup() {
    echo "🛑 Parando servidores..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit
}

# Capturar Ctrl+C
trap cleanup SIGINT

# Iniciar Backend
echo "📡 Iniciando Backend Django..."
cd back
source venv/bin/activate
python manage.py runserver &
BACKEND_PID=$!
cd ..

# Aguardar um pouco para o backend iniciar
sleep 3

# Iniciar Frontend
echo "🎨 Iniciando Frontend React..."
cd front
npm run dev &
FRONTEND_PID=$!
cd ..

echo "✅ Servidores iniciados!"
echo ""
echo "URLs disponíveis:"
echo "- Frontend: http://localhost:5173"
echo "- Backend API: http://localhost:8000"
echo "- API Docs: http://localhost:8000/api/docs/"
echo "- Admin: http://localhost:8000/admin/"
echo ""
echo "Pressione Ctrl+C para parar os servidores"

# Aguardar indefinidamente
wait
