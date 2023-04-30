#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py flush --noinput

python manage.py migrate

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --username kingship --email kingship.lc@gmail.com --noinput

python manage.py add_manufacturers
python manage.py add_employees
python manage.py add_suppliers
python manage.py add_categories
python manage.py add_section
python manage.py add_ink
python manage.py add_stationery
python manage.py add_tolietries
python manage.py add_xerox_printer_models
python manage.py add_hp_printer_models


# python manage.py migrate --run-syncdb

python manage.py collectstatic --noinput

exec "$@"