# Quick DRF Project

## Getting Started

Setup project environment with:

```
$ git clone https://github.com/pmuston/drf_example.git
$ cd drf_example/
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

## API

Goto http://localhost:8000/api/dessert/

Using DRF GUI you can Create/Update/Delete etc Dessert

Also via http://localhost:8000/admin
