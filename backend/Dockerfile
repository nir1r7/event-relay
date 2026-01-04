FROM python:3.11-slim

# set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# copy app source code
COPY . .

RUN chmod +x entrypoint.sh

# environment variables
ENV PYTHONUNBUFFERED=1

# entrypoint: run migrations then start up
ENTRYPOINT ["./entrypoint.sh"]


