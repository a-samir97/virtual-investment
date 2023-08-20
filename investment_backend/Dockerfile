FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get install -y netcat-openbsd
WORKDIR /app/backend
COPY requirements.txt /app/backend/
RUN pip install -r requirements.txt
COPY . /app/backend/
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]