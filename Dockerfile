FROM python:3.7-alpine 

RUN pip install --upgrade pip
RUN apk --no-cache add gcc musl-dev

RUN adduser -D -h /app bot
USER bot
WORKDIR /app

COPY --chown=bot:bot requirements.txt .
RUN pip install --user -r requirements.txt

ENV PATH="/app/.local/bin:$PATH" 

COPY --chown=bot:bot . .

CMD ["python", "main.py"]
