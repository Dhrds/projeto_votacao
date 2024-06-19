FROM python:3.11-alpine
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

WORKDIR /app/project
COPY requirements.txt ./

RUN pip install -r requirements.txt
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
RUN chown -R appuser:appgroup /app

USER appuser
COPY . /app/project/
USER root

RUN apt-get update && apt-get install -y default-libmysqlclient-dev
EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:9000
