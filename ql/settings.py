import json, os, sys

def _fetch_settings(config_path, constant_config, default_config):
    try:
        config = constant_config.copy()
        config.update(json.load(open(config_path)))
        if 'NAME' not in config:
            config['NAME'] = input('Please enter database name: ')
        return config
    except FileNotFoundError:
        with open(config_path, 'w') as new_config:
            json.dump(default_config, new_config)
        print(
            'Config file %s created, fill it up!' %
            os.path.realpath(config_path)
        )
        sys.exit()
    except ValueError:
        print(
            'Config file %s invalid, fix it!' %
            os.path.realpath(config_path)
        )
        sys.exit(1)

DATABASES = {
    'default': _fetch_settings(
        'config.json',
        {
            'ENGINE': 'mysql.connector.django'
        },
        {
            'HOST': 'localhost',
            'PORT': '3306',
            'USER': 'root',
            'PASSWORD': '',
            'NAME': 'belongs_to_us'
        }
    )
}

INSTALLED_APPS = (
    'ql.orm',
)

SECRET_KEY = 'f5a73e42-a600-4925-a860-b40b72acf497'
