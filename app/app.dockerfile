FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt 

COPY . .

CMD ["python3", "__main__.py"]