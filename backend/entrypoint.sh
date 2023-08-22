#!/bin/bash
while ! nc -z db 5432 ; do
    echo "Waiting for the Postgres Server"
    sleep 3
done

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Load Fixtures"
python manage.py loaddata fixtures/accounts.json
python manage.py loaddata fixtures/stocks.json
python manage.py loaddata fixtures/transactions.json

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000