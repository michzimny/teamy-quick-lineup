DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'your-username',
        'PASSWORD': 'your-password',
        'NAME': 'your-database-name',
    }
}

INSTALLED_APPS = (
    'ql.orm',
)

SECRET_KEY = 'f5a73e42-a600-4925-a860-b40b72acf497'
