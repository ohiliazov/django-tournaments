help:
    just --list

install:
    poetry install --sync --no-interaction --no-root
    poetry run pre-commit install

requirements:
    poetry export -f requirements.txt -o requirements.txt --without-hashes

format:
    poetry run pre-commit run --all

runserver:
    poetry run python manage.py runserver

makemigrations:
    poetry run python manage.py makemigrations

migrate:
    poetry run python manage.py migrate
