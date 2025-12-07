
# 🚀 C.A Gestão

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.0-green?style=for-the-badge&logo=django)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue?style=for-the-badge&logo=docker)
![uv](https://img.shields.io/badge/uv-Fast%20Package%20Manager-purple?style=for-the-badge)

## 📹 Demonstração do Sistema

Confira nosso vídeo explicativo detalhando o funcionamento e as principais funcionalidades do sistema:

[![Assista ao Vídeo](https://img.youtube.com/vi/VP9DcIsrbc8/0.jpg)](https://youtu.be/VP9DcIsrbc8)

> **Link direto:** [https://youtu.be/VP9DcIsrbc8](https://youtu.be/VP9DcIsrbc8)

-----

## ⚡ Gerenciamento de Dependências com `uv`

Optamos pelo **[uv](https://github.com/astral-sh/uv)** devido à sua velocidade superior na resolução e instalação de pacotes.

O `uv` garante que as dependências sejam instaladas de forma determinística através do arquivo `uv.lock`. No ambiente Docker, ele já está configurado automaticamente. Caso queira rodar localmente:

```bash
# Instalar dependências
uv sync

# Adicionar uma nova biblioteca (exemplo)
uv add djangorestframework
````

-----

## 🐳 Como rodar o projeto (Docker)

Siga os passos abaixo para levantar o ambiente de desenvolvimento completo.

### 1️. Configuração de Ambiente

Primeiro, crie o arquivo de variáveis de ambiente baseado no exemplo:

```bash
cp .env.example .env
```

> **Nota:** Verifique o arquivo `.env` e ajuste as credenciais do banco de dados se necessário.

### 2️. Construir e Iniciar os Containers

Para subir a aplicação e o banco de dados:

```bash
docker compose up --build -d
```

*O parâmetro `-d` executa os containers em segundo plano (detach mode).*

### 3️. Configuração Inicial do Django

Após os containers estarem rodando, você precisa aplicar as migrações no banco de dados:

```bash
docker compose exec web python manage.py migrate
```

(Opcional) Crie um superusuário para acessar o admin do Django:

```bash
docker compose exec web python manage.py createsuperuser
```

### 4️. Acessando a Aplicação

  - **Aplicação:** [http://localhost:8000](http://localhost:8000)
  - **Admin:** [http://localhost:8000/admin](http://localhost:8000/admin)

-----

## Comandos Úteis

Aqui estão alguns comandos frequentes para o dia a dia:

| Ação | Comando |
| :--- | :--- |
| **Ver logs em tempo real** | `docker compose logs -f` |
| **Parar containers** | `docker compose stop` |
| **Parar e remover containers/redes** | `docker compose down` |
| **Criar novas migrações** | `docker compose exec web python manage.py makemigrations` |
| **Entrar no shell do container** | `docker compose exec web bash` |

-----
