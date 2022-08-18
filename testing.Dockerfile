FROM tiangolo/uvicorn-gunicorn-fastapi

COPY app/requirements.txt requirements.txt
COPY app/requirements-dev.txt requirements-dev.txt

RUN pip install -r requirements-dev.txt

COPY . .

CMD [ "pytest" ]