FROM python:3.13-slim AS base

# Copiar binário do uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT="/opt/venv" \
    PATH="/opt/venv/bin:$PATH"

# Dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copiar binário do uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# ----------------------------
# STAGE 1 — instalar dependências
# ----------------------------
FROM base AS deps

WORKDIR /app

COPY pyproject.toml uv.lock ./

# Instalar dependências no venv (aproveita cache quando deps não mudam)
RUN uv sync --no-dev --frozen


# ----------------------------
# STAGE 2 — imagem final
# ----------------------------
FROM base AS final

WORKDIR /app
COPY --from=deps /opt/venv /opt/venv

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copiar código
COPY ./src /app/src

ENTRYPOINT ["/entrypoint.sh"]

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
