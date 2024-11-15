FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
COPY .env .
COPY app/sweph/. ./app
COPY ./alembic.ini .

ARG REST_PORT
ENV REST_PORT=${REST_PORT}

EXPOSE ${REST_PORT}

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "-B", "-m", "app.main"]
CMD ["sh", "-c", "python -m alembic upgrade head && python -B -m app.main"]
