FROM python:3.11-slim AS base

ARG APP_USER=appuser
ARG DEFAULT_PORT=8000

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PORT=${DEFAULT_PORT}

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create non-root user and group
RUN useradd -m ${APP_USER} && chown -R ${APP_USER}:${APP_USER} /app
USER ${APP_USER}

RUN python manage.py collectstatic --noinput

EXPOSE ${PORT}

# Run gunicorn
CMD gunicorn --bind 0.0.0.0:${PORT} --workers 3 your_project.wsgi:application
