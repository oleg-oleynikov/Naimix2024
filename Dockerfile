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
COPY . /app
COPY .env .
COPY app/sweph/. ./app

ARG REST_PORT
ENV REST_PORT=${REST_PORT}

EXPOSE ${REST_PORT}

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "-m", "app.main"]
