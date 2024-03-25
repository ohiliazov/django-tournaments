help:
    just --list

install:
    poetry install --all-extras --sync --no-interaction --no-root
    poetry run pre-commit install
    npm install --no-audit

requirements:
    poetry lock --no-update
    poetry export -f requirements.txt -o requirements.txt --without-hashes

format:
    poetry run pre-commit run --all

watch:
    npx tailwindcss -i static/css/input.css -o static/css/output.css --watch

makemigrations:
    poetry run python manage.py makemigrations

migrate:
    poetry run python manage.py migrate
