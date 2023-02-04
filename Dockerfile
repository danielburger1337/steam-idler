FROM python:3

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

RUN apt update && apt upgrade -y

RUN mkdir -p /app

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
