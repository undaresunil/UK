FROM python:3.9-slim
WORKDIR /usr/src/app
COPY . .
CMD ["python", "./app.py"]
