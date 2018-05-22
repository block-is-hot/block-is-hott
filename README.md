# block-is-hott

**Authors:** Shannon Tully, Jeremy Crawford and Gene Pieterson

# What is Block Is Hott?

Block is hott is an integrated heat map showing different layers of 

# Our Vision

We want to show a new resident, or an exisiting resident, the trends of the areas in the city that interests them.

# Routes

# Getting Started

We made an organization through github. After creating an organization and setting up a repo, we cloned it to our directory.

```
$ git clone https://github.com/block-is-hot/block-is-hott.git
```

Inside of **block-is-hott**, we make a virtual environment and activate it.

```
$ python3 -m venv ENV
source ENV/bin/activate
```

Now it's time to start the scaffold for our app. We start with installing django and then making the project.

```
(ENV)$ pip install django
(ENV)$ django-admin startproject hott

(ENV)$ tree hott
hott
├── hott
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```

# Setting up the Database

Since we'll be passing a few variable through the database and doing testing, we will use the database format in settings.py. But first we [`pip install psycopg2-binary`], then create the database with [`createdb hottdb`] and [`createdb hottdb_test`]. Our database in settings will be:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME', ''),
        'USER': os.environ.get('DATABASE_USER', ''),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('DATABASE_HOST', ''),
        'PORT': '5432',
        'TEST': {
            'NAME': hottdb_test
        }
    }
}
```

**Exporting Environmental Variables**: In the ENV/bin/activate, we exported the environmental variables.

```
export SECRET_KEY='secret'
export DB_NAME='hottdb'
export DB_USER=''
export DB_PASS=''
export DB_HOST='localhost'
export DEBUG='True'
```

Then we did migrations of our database.

```
(ENV)$ python manage.py makemigrations
(ENV)$ python manage.py migrate
```

**gitignore**: Make a .gitignore for python, <os>, vscode and django.

To install the application requirements with pip:

```
(ENV) emotion-reader $ pip install -r requirements.txt
```

# Config new app

**Make New App**: In the same directory as manage.py,

```
./manage.py startapp <app name>
```

Then you will want to save all pip installation requirements.

```
(ENV)$ pip freeze > requirements.txt
```

**Django Registration**: Install django-registration. It will downgrade you to Django 1.11.13, but you need Django 2.0.5. So you'll need to upgrade it with the next command.

```
(ENV)$ pip install django-registration
(ENV)$ pip install -U django
```

# SCSS

Here, we made scss files by first playing an underscore before the name, then putting .scss after it like this: [`_base.scss`]. In the main scss, we imported each of the scss files by saying [`@import "base"`]. Then we compile the scss files with this command:

```
(ENV)$ pip install libsass django-compressor django-sass-processor
(ENV)$ ./manage.py compilescss
```

To check how everything looks, run the server.

```
(ENV)$ ./manage.py runserver
```

