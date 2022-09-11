FROM python:3.9

WORKDIR /beender-service

COPY ./requirements.txt /beender-service/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /beender-service/requirements.txt

COPY ./app /beender-service/app

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5000"]
