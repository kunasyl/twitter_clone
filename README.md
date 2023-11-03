# Twitter in Django

### Installation Instructions
- Run following commands after cloning the repository

```
# Go inside the directory containing the project
cd twitter-django

# Create virtual environment
virtualenv env

# Activate the virtualenv
source env/bin/activate

# Install requirements/libraries
pip install -r requirements.txt

# Go inside the 'tweeter' directory and run migrations
cd tweeter
python manage.py makemigrations
python manage.py migrate

```

#### Run the App
```
python manage.py runserver
```

