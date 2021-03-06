from .base import *

# access heroku environment environment-variable (config variable) of the secret key
SECRET_KEY = get_env('SECRET_KEY')

# Activate Django-Heroku.
django_heroku.settings(locals(), logging=True, allowed_hosts=False, databases=not DEBUG)