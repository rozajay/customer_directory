FROM python

# Install system dependencies for PostgreSQL
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# Wait for the database to be available, run migrations, and start the server
CMD sh -c "until pg_isready -U root -h db; do sleep 1; done \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py loaddata view_customers \
    && python manage.py runserver 0.0.0.0:8000"

EXPOSE 8000