# 🎬 Moviendo - Sistema de Gerenciamento de Filmes e Séries

Sistema completo para catalogar, avaliar e organizar filmes e séries, com integração ao TMDB (The Movie Database).

**Desenvolvido por:**  
Pedro Vitor Chastalo Santos  
RA: 2576759

---

## 🚀 Configuração Rápida

### Primeira vez (PC zerado)

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd Moviendo-main

# Execute o script de configuração automática
./setup.sh
```

### Execução diária

```bash
# Rodar ambos os servidores (backend + frontend)
./run-dev.sh
```

## 📋 Pré-requisitos

- **Python 3.8+** - [Download](https://python.org)
- **Node.js 16+** - [Download](https://nodejs.org)
- **PostgreSQL** - [Download](https://postgresql.org)

## 🌐 URLs do Sistema

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Documentação API**: http://localhost:8000/api/docs/
- **Painel Admin**: http://localhost:8000/admin/

## 🛠️ Comandos Manuais

### Backend Django

```bash
cd back
source venv/bin/activate
python manage.py runserver
```

### Frontend React

```bash
cd front
npm run dev
```

## 📚 Funcionalidades

- ✅ Cadastro de filmes e séries
- ✅ Integração com TMDB para importar dados
- ✅ Sistema de avaliações
- ✅ Criação de listas personalizadas
- ✅ Gerenciamento de diretores, gêneros e plataformas
- ✅ API REST completa
- ✅ Interface moderna e responsiva

## 🔧 Tecnologias

### Backend

- Django 5.2.8 + Django REST Framework
- PostgreSQL
- Integração TMDB API

### Frontend

- React 18 + Vite
- TailwindCSS + Shadcn/UI
- Axios para API calls
