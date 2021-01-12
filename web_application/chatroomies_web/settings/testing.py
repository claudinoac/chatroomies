from chatroomies_web.settings.production import *  # noqa

DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3",},
}

DEBUG = True
