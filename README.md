# PyConES 2018 Web

Web page made for PyConES 2018, made in Django with ❤️.

## Deploy with Docker

1. Create a `.env` file with required environment variables.

```console
$ cp web.env.example web.env
```

2. Run docker services:

```console
$ docker-compose up
```

## Local development

1. Create a virtualenv:

```console
$ virtualenv --python=python3 pycones18
```

2. Activate it:

```console
$ source pycones18/bin/activate
```

3. Install dependencies:

```console
$ pip install -r requirements.txt
```

4. Set the secret key:

```console
$ export SECRET_KEY=<YOUR_SUPER_SECRET_KEY_HERE>
```

5. Create the database:

```console
$ python manage.py migrate
```

6. Launch the development server:

```console
$ python manage.py runserver
```

7. Visit the url http://127.0.0.1:8000/
