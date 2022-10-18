FROM python:3.11.0a6-alpine3.15
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt --no-cache-dir
CMD python app.py
