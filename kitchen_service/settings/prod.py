from kitchen_service.settings.base import *
from dotenv import load_dotenv


DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRASE_DB"],
        "USER": os.environ["POSTGRASE_USER"],
        "PASSWORD": os.environ["POSTGRASE_PASSWORD"],
        "HOST": os.environ["POSTGRASE_HOST"],
        "PORT": os.environ("POSTGRES_DB_PORT", 5432),
        "OPTIONS": {"sslmode": "require"},
    }
}
