FROM python:3.10-slim AS production


ENV MODULE_NAME=app.main:app
ENV PYTHONPATH=/app
ENV WORKER_CLASS=uvicorn.workers.UvicornWorker

ENV SQLALCHEMY_WARN_20=true

COPY /start.sh /start.sh
RUN chmod +x /start.sh

COPY /start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

EXPOSE 80

COPY app/requirements.txt app/requirements.txt

# to build psycopg2
RUN apt-get update \
    && apt-get install -y libpq-dev gcc openssl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir --upgrade pip \
    pip install --no-cache-dir -r app/requirements.txt

COPY app /app

CMD ["/start.sh"]

FROM production AS dev

RUN pip install -r ./requirements-dev.txt

RUN apt update && apt install -y \
    curl \
    gpg
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg;
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null;
RUN apt update && apt install -y gh;
RUN gh auth login -w

COPY /start-test.sh /start-test.sh
RUN chmod +x /start-test.sh


