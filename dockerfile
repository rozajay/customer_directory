FROM python
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

# Wait for the database to be available, run migrations, and start the server
CMD sh -c "python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py loaddata view_customers \
    && python manage.py runserver 0.0.0.0:8000"

EXPOSE 8000