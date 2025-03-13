FROM arm64v8/python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Show environment and run bot
CMD echo "Environment variables:" && \
    env | grep DISCORD && \
    echo "Starting bot..." && \
    python bot.py
