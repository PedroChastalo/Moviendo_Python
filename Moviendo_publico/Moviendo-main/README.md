# 🎬 Moviendo - Sistema de Gerenciamento de Filmes e Séries

Sistema completo para catalogar, avaliar e organizar filmes e séries, com integração ao TMDB (The Movie Database).

**Desenvolvido por:**  
Pedro Vitor Chastalo Santos  
RA: 2576759

---

## Configuração Rápida

### Primeira vez (PC zerado)

```bash
# Clone o repositório
git clone <url-do-repositorio>
cd Moviendo-main

## Pré-requisitos

- **Python 3.8+** - [Download](https://python.org)
- **Node.js 16+** - [Download](https://nodejs.org)
- **PostgreSQL** - [Download](https://postgresql.org)

## Comandos Manuais

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

## 🔧 Tecnologias

### Backend

- Django 5.2.8 + Django REST Framework
- PostgreSQL
- Integração TMDB API

### Frontend

- React 18 + Vite
- TailwindCSS + Shadcn/UI
- Axios para API calls
