FROM python as builder

ADD . /code
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


FROM builder

COPY . .

EXPOSE 8888
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]