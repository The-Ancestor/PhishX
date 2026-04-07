FROM python:3.11.9 AS builder

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
RUN python -m venv .venv

COPY requirements.txt ./
RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

FROM python:3.11.9-slim
WORKDIR /app

# Copy venv and app
COPY --from=builder /app/.venv .venv/
COPY . .

EXPOSE 8080
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

CMD ["/app/.venv/bin/gunicorn", "-b", "0.0.0.0:8080", "main:app"]
