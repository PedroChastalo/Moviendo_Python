# 📊 Relatório da Estrutura da Aplicação Moviendo

## 🎯 Visão Geral

O **Moviendo** é um sistema web completo para gerenciar filmes e séries, permitindo que usuários cataloguem, avaliem e organizem seu entretenimento de forma intuitiva. A aplicação é dividida em duas partes principais: um **backend** (servidor) em Python/Django e um **frontend** (interface) em React.

---

## 🏗️ Arquitetura Geral

```
Moviendo/
├── 🖥️  back/          → Servidor (API)
├── 🎨  front/         → Interface do usuário
├── 🚀  setup.sh       → Script de configuração inicial
├── ⚡  run-dev.sh     → Script para rodar o projeto
└── 📖  README.md      → Instruções de uso
```

---

## 🖥️ Backend (Servidor) - Pasta `back/`

O backend é responsável por **armazenar dados**, **processar requisições** e **fornecer informações** para o frontend através de uma API REST.

### 📁 Estrutura do Backend

```
back/
├── 📦 apps/                    → Módulos da aplicação
│   ├── 🎭 diretores/          → Gerencia diretores de filmes
│   ├── 🎪 generos/            → Gerencia gêneros (ação, drama, etc.)
│   ├── 📺 plataformas/        → Gerencia plataformas (Netflix, Prime, etc.)
│   ├── 🏷️  tags/              → Gerencia tags personalizadas
│   ├── 🎬 obras/              → Gerencia filmes e séries (módulo principal)
│   ├── ⭐ avaliacoes/         → Gerencia avaliações dos usuários
│   └── 📋 listas/             → Gerencia listas personalizadas
├── 🔧 core/                   → Funcionalidades centrais
├── 🌐 integrations/           → Integrações externas (TMDB API)
├── ⚙️  setup/                 → Configurações do Django
└── 🗄️  manage.py             → Comando principal do Django
```

### 🎭 Apps (Módulos) - Explicação Detalhada

Cada "app" é um módulo independente que gerencia uma parte específica do sistema:

#### 1. **Diretores** (`apps/diretores/`)

- **Função**: Armazena informações sobre diretores de filmes e séries
- **Dados**: Nome, biografia, nacionalidade, data de nascimento
- **Exemplo**: "Christopher Nolan", "Quentin Tarantino"

#### 2. **Gêneros** (`apps/generos/`)

- **Função**: Categoriza filmes e séries por gênero
- **Dados**: Nome do gênero, descrição
- **Exemplo**: "Ação", "Drama", "Comédia", "Terror"

#### 3. **Plataformas** (`apps/plataformas/`)

- **Função**: Registra onde assistir os conteúdos
- **Dados**: Nome da plataforma, URL, logo
- **Exemplo**: "Netflix", "Amazon Prime", "Disney+"

#### 4. **Tags** (`apps/tags/`)

- **Função**: Permite criar etiquetas personalizadas
- **Dados**: Nome da tag, cor
- **Exemplo**: "Favoritos", "Para assistir", "Clássicos"

#### 5. **Obras** (`apps/obras/`) - **MÓDULO PRINCIPAL**

- **Função**: Gerencia todos os filmes e séries
- **Dados**: Título, sinopse, ano, duração, capa, tipo (filme/série)
- **Relacionamentos**: Conecta com diretores, gêneros, plataformas e tags
- **Funcionalidades especiais**:
  - Importação automática de dados do TMDB
  - Controle de progresso (episódio atual, temporada)
  - Status (quero assistir, assistindo, assistido)

#### 6. **Avaliações** (`apps/avaliacoes/`)

- **Função**: Permite avaliar filmes e séries
- **Dados**: Nota (0-10), comentário, data da avaliação
- **Relacionamento**: Cada avaliação pertence a uma obra

#### 7. **Listas** (`apps/listas/`)

- **Função**: Cria listas personalizadas de filmes/séries
- **Dados**: Nome da lista, descrição, tipo (pública/privada)
- **Exemplo**: "Melhores de 2024", "Para maratonar no fim de semana"

### 🔧 Core (Núcleo)

- **`exceptions.py`**: Trata erros de forma padronizada
- **`apps.py`**: Configuração básica do módulo core

### 🌐 Integrations (Integrações)

- **`tmdb/client.py`**: Cliente para buscar dados do TMDB (The Movie Database)
- **Função**: Importa automaticamente informações de filmes e séries

### ⚙️ Setup (Configurações)

- **`settings.py`**: Configurações principais do Django
- **`urls.py`**: Define as rotas da API

---

## 🎨 Frontend (Interface) - Pasta `front/`

O frontend é a **interface visual** que os usuários veem e interagem no navegador.

### 📁 Estrutura do Frontend

```
front/
├── 📱 src/                    → Código fonte da interface
│   ├── 🧩 components/         → Componentes reutilizáveis
│   ├── 📄 pages/              → Páginas da aplicação
│   ├── 🔧 services/           → Comunicação com a API
│   └── 🎨 styles/             → Estilos visuais
├── 📦 package.json            → Dependências do Node.js
└── ⚙️  vite.config.js         → Configurações do Vite
```

### 🎯 Tecnologias do Frontend

- **React**: Biblioteca para criar interfaces interativas
- **Vite**: Ferramenta de desenvolvimento rápida
- **TailwindCSS**: Framework para estilização
- **Axios**: Comunicação com o backend

---

## 🔄 Como Tudo Funciona Junto

### 1. **Fluxo de Dados**

```
Usuário → Frontend → API (Backend) → Banco de Dados → API → Frontend → Usuário
```

### 2. **Exemplo Prático: Adicionar um Filme**

1. Usuário acessa o frontend no navegador
2. Clica em "Adicionar Filme"
3. Frontend envia requisição para `/api/obras/` (backend)
4. Backend processa e salva no banco PostgreSQL
5. Backend retorna confirmação para o frontend
6. Frontend atualiza a tela mostrando o novo filme

### 3. **Integração TMDB**

1. Usuário busca por "Inception"
2. Frontend chama `/api/obras/pesquisar_tmdb/?query=Inception`
3. Backend consulta a API do TMDB
4. Retorna resultados com pôster, sinopse, etc.
5. Usuário pode importar automaticamente

---

## 📊 Banco de Dados

### 🗄️ Estrutura das Tabelas Principais

1. **diretores**: Informações dos diretores
2. **generos**: Lista de gêneros disponíveis
3. **plataformas**: Plataformas de streaming
4. **tags**: Tags personalizadas
5. **obras**: Filmes e séries (tabela central)
6. **avaliacoes**: Avaliações dos usuários
7. **listas**: Listas personalizadas

### 🔗 Relacionamentos

- Uma **obra** pode ter vários **diretores**
- Uma **obra** pode ter vários **gêneros**
- Uma **obra** pode estar em várias **plataformas**
- Uma **obra** pode ter uma **avaliação**
- Uma **lista** pode conter várias **obras**

---

## 🚀 Scripts de Automação

### 📋 Arquivos Criados

#### 1. **`setup.sh`** - Configuração Inicial

- **Função**: Configura o projeto pela primeira vez
- **O que faz**:
  - Verifica se Python, Node.js e PostgreSQL estão instalados
  - Cria ambiente virtual Python
  - Instala dependências do backend e frontend
  - Cria banco de dados
  - Executa migrações
  - Cria usuário administrador

#### 2. **`run-dev.sh`** - Execução Diária

- **Função**: Inicia os servidores de desenvolvimento
- **O que faz**:
  - Inicia o backend Django na porta 8000
  - Inicia o frontend React na porta 5173
  - Permite parar ambos com Ctrl+C

---

## 🎯 Principais Funcionalidades

### Para Usuários Finais:

1. **Catalogar**: Adicionar filmes e séries à biblioteca
2. **Avaliar**: Dar notas e comentários
3. **Organizar**: Criar listas temáticas
4. **Descobrir**: Importar dados do TMDB
5. **Acompanhar**: Controlar progresso de séries

### Para Desenvolvedores:

1. **API REST**: Endpoints padronizados
2. **Documentação**: Swagger automático
3. **Modular**: Código organizado por domínio
4. **Escalável**: Fácil adicionar novas funcionalidades

---

## 🔧 Arquivos Importantes Explicados

### Backend:

- **`requirements.txt`**: Lista todas as bibliotecas Python necessárias
- **`manage.py`**: Comando principal para rodar o Django
- **`settings.py`**: Configurações do banco, APIs, etc.

### Frontend:

- **`package.json`**: Lista todas as bibliotecas JavaScript necessárias
- **`vite.config.js`**: Configurações do servidor de desenvolvimento

---

## 🎓 Conceitos Técnicos Simplificados

### **API REST**

- Forma padronizada de comunicação entre frontend e backend
- Usa URLs como `/api/obras/` para diferentes operações

### **Django Apps**

- Módulos independentes que podem ser reutilizados
- Cada app tem sua responsabilidade específica

### **Migrations**

- Scripts que criam/modificam tabelas no banco de dados
- Mantém histórico de mudanças na estrutura

### **Serializers**

- Convertem dados do banco para JSON (e vice-versa)
- Garantem que apenas dados válidos sejam salvos

### **ViewSets**

- Classes que definem como a API responde às requisições
- Implementam operações CRUD (Create, Read, Update, Delete)

---

## 🎯 Resumo Final

O **Moviendo** é uma aplicação moderna que segue as melhores práticas de desenvolvimento:

- **Separação de responsabilidades**: Frontend e backend independentes
- **Arquitetura modular**: Cada funcionalidade em seu próprio módulo
- **Código limpo**: Fácil de entender e manter
- **Automação**: Scripts facilitam configuração e uso
- **Escalabilidade**: Fácil adicionar novas funcionalidades

A estrutura permite que a aplicação cresça de forma organizada, mantendo a qualidade e facilitando a manutenção por outros desenvolvedores.
