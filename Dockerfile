FROM python:3.10-slim-buster

WORKDIR /opt
COPY ./requirements ./app/requirements/
RUN pip install --no-cache-dir -r ./app/requirements/base.txt
COPY ./src ./app

COPY migrate.sh /opt/
RUN chmod +x /opt/migrate.sh
RUN /opt/migrate.sh

CMD ["python", "manage.py", "runserver"]
