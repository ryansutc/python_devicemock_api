## Python Device Mock API

A small Python Django API that mocks devices with real-time data values. Particularly those organized in a file-directory like structure.

## Getting Started

1. Create your virtual python env.

`export PIPENV_VENV_IN_PROJECT=1 && pipenv install`

2. Load Fixture Data:
   `./loaddata.sh`

3. Run app:
   `python manage.py runserver`

4. open `localhost:8000/api`
