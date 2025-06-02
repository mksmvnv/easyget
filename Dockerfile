FROM python:3.12-alpine

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --only main --no-root && \
    pip uninstall -y poetry

COPY . .

CMD ["python3", "core/app.py"]
