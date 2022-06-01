FROM python as builder

ADD . /code
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


FROM builder

ENV SERVER_PORT=8888 \
    DETA_ACCESS_TOKEN=token

COPY . .

EXPOSE 8888:8888
EXPOSE 5432:5432

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]