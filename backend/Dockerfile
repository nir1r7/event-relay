FROM python:3.11-slim

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# copy app source code
COPY app ./app
COPY alembic.ini ./alembic.ini
COPY alembic ./alembic

# environment variables
ENV PYTHONUNBUFFERED=1

# entrypoint: run migrations then start up
CMD ["sh", "-c", "alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]


