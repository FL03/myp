FROM python as builder

ADD . /code
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


FROM builder

ENV PORT=8000

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]