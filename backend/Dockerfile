FROM python:3.8

WORKDIR /app

COPY venv /app/venv
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY .env /app/.env
COPY static /app/static
COPY . /app

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
