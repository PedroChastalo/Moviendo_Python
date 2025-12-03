# Contribuições da Equipe - Projeto Moviendo

Este documento descreve as contribuições de cada membro da equipe no desenvolvimento do sistema Moviendo.

---

## Visão Geral da Equipe

| Membro | RA | Área Principal | Responsabilidades |
|--------|-----|----------------|-------------------|
| Pedro Vitor Chastalo Santos | 2576759 | Frontend & Revisão | Interface do usuário, experiência visual e validação do backend |
| Winicius dos Passos | 2398516 | Backend & Banco de Dados | API REST, lógica de negócio e estrutura de dados |

---

## Pedro Vitor Chastalo Santos
**RA: 2576759**

### Área de Atuação: Frontend & Controle de Qualidade

#### Responsabilidades Principais:

### 1. **Desenvolvimento do Frontend (React)**
- Implementação completa da interface do usuário utilizando React 18
- Desenvolvimento de componentes reutilizáveis com Shadcn/UI
- Estilização moderna com TailwindCSS
- Implementação de animações e interações com Framer Motion

#### Componentes Desenvolvidos:
- **Sistema de Navegação**: Rotas e navegação entre páginas
- **Catálogo de Obras**: Interface para visualização de filmes e séries
- **Formulários**: Criação e edição de obras, avaliações e listas
- **Sistema de Avaliações**: Interface para avaliar e comentar obras
- **Listas Personalizadas**: Criação e gerenciamento de listas
- **Integração TMDB**: Interface de busca e importação de dados

#### Tecnologias Utilizadas:
- React 18 + React Router DOM
- Vite (Build tool)
- TailwindCSS + Shadcn/UI
- Axios (Comunicação com API)
- Framer Motion (Animações)
- Lucide React (Ícones)
- React Hot Toast (Notificações)

### 2. **Revisão e Validação do Backend**
- Testes de integração entre frontend e backend
- Validação de endpoints da API REST
- Verificação de respostas e tratamento de erros
- Testes de fluxos completos da aplicação
- Identificação e reporte de bugs

#### Atividades de Validação:
- Teste de CRUD (Create, Read, Update, Delete) para todas as entidades
- Validação de filtros e buscas
- Teste de integração com TMDB API
- Verificação de CORS e comunicação entre servidores
- Testes de performance e responsividade

### 3. **Experiência do Usuário (UX/UI)**
- Design de interfaces intuitivas e modernas
- Implementação de feedback visual para ações do usuário
- Otimização de fluxos de navegação
- Responsividade para diferentes dispositivos

---

## Winicius dos Passos
**RA: 2398516**

### Área de Atuação: Backend & Infraestrutura de Dados

#### Responsabilidades Principais:

### 1. **Desenvolvimento do Backend (Django)**
- Arquitetura e implementação da API REST com Django REST Framework
- Desenvolvimento de 7 aplicações Django modulares
- Implementação de serializers e viewsets
- Configuração de CORS para comunicação com frontend
- Sistema de tratamento de exceções customizado

#### Aplicações Desenvolvidas:

##### **1. Diretores (`apps/diretores/`)**
- Models: Informações de diretores (nome, biografia, nacionalidade)
- API endpoints para CRUD de diretores
- Relacionamento com obras

##### **2. Gêneros (`apps/generos/`)**
- Models: Categorização de obras por gênero
- Sistema de tags de gênero
- Endpoints para gerenciamento de gêneros

##### **3. Plataformas (`apps/plataformas/`)**
- Models: Plataformas de streaming
- Gerenciamento de onde assistir
- URLs e logos das plataformas

##### **4. Tags (`apps/tags/`)**
- Models: Sistema de etiquetas personalizadas
- Cores e categorização customizada
- Endpoints para CRUD de tags

##### **5. Obras (`apps/obras/`)** - **Módulo Principal**
- Models: Filmes e séries (título, sinopse, ano, duração, etc.)
- Sistema de status (quero assistir, assistindo, assistido)
- Controle de progresso para séries (temporada, episódio)
- Integração com TMDB para importação automática
- Relacionamentos many-to-many com diretores, gêneros, plataformas e tags

##### **6. Avaliações (`apps/avaliacoes/`)**
- Models: Sistema de avaliação (nota 0-10, comentários)
- Relacionamento com obras
- Timestamps de criação e atualização

##### **7. Listas (`apps/listas/`)**
- Models: Listas personalizadas de obras
- Sistema público/privado
- Ordenação de itens nas listas

### 2. **Integração com APIs Externas**
- Implementação do cliente TMDB (`integrations/tmdb/client.py`)
- Endpoints para busca de filmes e séries no TMDB
- Importação automática de dados (pôster, sinopse, elenco, etc.)
- Configuração de API keys e URLs base

### 3. **Banco de Dados PostgreSQL**

#### Estrutura do Banco de Dados:
- Design do schema relacional
- Definição de relacionamentos entre tabelas
- Índices para otimização de consultas
- Constraints e validações

#### Script de Criação (`create_database.py`):
- Conexão automática com PostgreSQL
- Verificação de existência do banco
- Criação do banco `moviendo_python_db`
- Tratamento de erros de conexão

#### Migrações Django:
- Criação de migrations para todas as apps
- Versionamento de mudanças no schema
- Scripts de migração para:
  - Criação de tabelas
  - Relacionamentos many-to-many
  - Alterações de estrutura

### 4. **Configuração e Infraestrutura**

#### Arquivo `settings.py`:
- Configuração de banco de dados PostgreSQL
- Settings de CORS para múltiplas origens
- Configuração do Django REST Framework
- Integração com drf-spectacular (Swagger)
- Configuração de timezone e internacionalização (pt-BR)
- Settings da API TMDB

#### Arquivo `requirements.txt`:
- Django 5.2.8
- djangorestframework 3.15.2
- django-cors-headers 4.6.0
- psycopg2-binary 2.9.10 (Driver PostgreSQL)
- drf-spectacular 0.28.0 (Documentação API)
- djangorestframework-camel-case 1.4.2
- requests 2.32.3

### 5. **Sistema de Exceções Customizado**
- Handler de exceções padronizado (`core/exceptions.py`)
- Respostas de erro formatadas
- Tratamento consistente de erros da API

---

## Fluxo de Trabalho Colaborativo

### Integração Frontend-Backend

```
┌─────────────────────────────────────────────────────────────┐
│                    FLUXO DE TRABALHO                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Pedro (Frontend)          Winicius (Backend)              │
│        │                          │                         │
│        │  1. Desenvolve API       │                         │
│        │  ◄───────────────────────┤                         │
│        │                          │                         │
│        │  2. Testa endpoints      │                         │
│        ├─────────────────────────►│                         │
│        │                          │                         │
│        │  3. Reporta bugs         │                         │
│        ├─────────────────────────►│                         │
│        │                          │                         │
│        │  4. Correções            │                         │
│        │  ◄───────────────────────┤                         │
│        │                          │                         │
│        │  5. Implementa UI        │                         │
│        ├──────────────┐           │                         │
│        │              │           │                         │
│        │  6. Integra com API      │                         │
│        ├─────────────────────────►│                         │
│        │                          │                         │
│        │  7. Validação final      │                         │
│        ├─────────────────────────►│                         │
│        │                          │                         │
└─────────────────────────────────────────────────────────────┘
```

### Divisão de Responsabilidades

| Camada | Responsável | Tecnologias |
|--------|-------------|-------------|
| **Apresentação** | Pedro | React, TailwindCSS, Shadcn/UI |
| **Comunicação** | Ambos | Axios, REST API |
| **Lógica de Negócio** | Winicius | Django, DRF |
| **Persistência** | Winicius | PostgreSQL, Django ORM |
| **Integrações** | Winicius | TMDB API |
| **Validação** | Pedro | Testes de integração |

---

## Estatísticas do Projeto

### Backend (Winicius)
- **7 aplicações Django** completas
- **~15 models** de banco de dados
- **~20 endpoints** REST API
- **1 integração externa** (TMDB)
- **Migrations** para todas as apps
- **1 script** de automação (create_database.py)

### Frontend (Pedro)
- **~40+ componentes** React
- **~10 páginas** principais
- **Integração completa** com todos os endpoints
- **Sistema de roteamento** completo
- **Animações e transições** em toda a aplicação

---

## Resultados Alcançados

### Funcionalidades Implementadas

**Catálogo Completo**
- Adicionar, editar e remover filmes/séries
- Busca e filtros avançados
- Importação automática do TMDB

**Sistema de Avaliações**
- Notas de 0-10
- Comentários e reviews
- Histórico de avaliações

**Listas Personalizadas**
- Criar listas temáticas
- Organizar obras
- Compartilhamento de listas

**Gerenciamento de Dados**
- Diretores, gêneros, plataformas
- Tags personalizadas
- Relacionamentos complexos

**Integração TMDB**
- Busca de filmes/séries
- Importação de metadados
- Imagens e pôsteres

---

## Conclusão

O projeto Moviendo foi desenvolvido com sucesso através da colaboração efetiva entre os membros da equipe:

- **Winicius dos Passos** construiu uma base sólida com um backend robusto, bem estruturado e escalável, além de toda a infraestrutura de banco de dados.

- **Pedro Vitor Chastalo Santos** criou uma interface moderna e intuitiva, garantindo a qualidade através de testes rigorosos e validação contínua do sistema.

A divisão clara de responsabilidades e a comunicação constante entre frontend e backend resultaram em uma aplicação completa, funcional e de alta qualidade.

---

**Data de Conclusão:** Dezembro de 2025  
**Instituição:** Universidade Tecnológica Federal do Paraná 
**Disciplina:** Projeto e Desenvolvimento de Sistemas Web
