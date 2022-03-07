FROM python:3.10.2-slim


ADD main.py /

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED = 1

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
COPY . /tmp/

WORKDIR /app
ADD . /app

RUN adduser -u 1234 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser


CMD ["python", "./main.py"]