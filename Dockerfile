FROM tiangolo/uvicorn-gunicorn-fastapi

COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN pip install python-jose

COPY ./app /app