FROM python:latest

RUN apt update -y && apt upgrade -y

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

CMD ["python", "init.py"]
