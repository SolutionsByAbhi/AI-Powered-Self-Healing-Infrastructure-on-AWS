FROM python:3.11

WORKDIR /app

COPY ml/requirements.txt .

RUN pip install \
-r requirements.txt

COPY ml .

CMD ["python","train.py"]
