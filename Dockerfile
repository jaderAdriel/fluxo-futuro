FROM python:3.13-slim

# Copiar binário do uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT="/opt/venv"

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar dependências
COPY pyproject.toml uv.lock ./

# Instalar dependências no venv
RUN uv sync --no-dev --frozen

# Colocar o venv no PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copiar entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copiar código
COPY ./src /app/src

ENTRYPOINT ["/entrypoint.sh"]

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
