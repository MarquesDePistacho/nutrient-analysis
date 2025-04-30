# Базовый образ
FROM mcr.microsoft.com/vscode/devcontainers/python:3.10

# Установка PostgreSQL client и Git
RUN apt-get update && \
    apt-get install -y postgresql-client git && \
    rm -rf /var/lib/apt/lists/*

# Установка дополнительных зависимостей
WORKDIR /workspace
COPY requirements.txt /workspace/
RUN pip install --no-cache-dir -r requirements.txt

# Создание пользователя vscode с правами
USER vscode