FROM arm64v8/python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY .env .

ENV $(cat .env | xargs)

CMD ["python", "bot.py"]
