from pathlib import Path
import environ
import os

BASE_DIR = Path(__file__).resolve().parent.parent
# загрузить переменные либо с переменных среды либо с файла .env
# если нет ни того не другого, то значениями по умолчанию
env = environ.Env()
env.read_env(env.str('ENV_PATH', BASE_DIR / '.env'))
# from django.core.management.utils import get_random_secret_key 
# get_random_secret_key()
SECRET_KEY = env.get_value('SECRET_KEY',
                           cast=str,
                           default='django-insecure-dp*hw^h1@**w-#vir436-y)$y&zd*=)3(o0$k56u=_or$$ax7a')
DEBUG = env.get_value('DEBUG',
                      cast=bool,
                      default=True)
NO_DB = os.environ.get('NO_DB', None)
if not DEBUG:
    ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
else:
    ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalog',
    'user',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'catalog.context_processors.basket',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
if DEBUG or NO_DB:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'OPTIONS': {
    #             'service': 'my_service',
    #             'passfile': '.my_pgpass',
    #         },
    #     }
    # }
    PG_HOST = env('PG_HOST', default='localhost')
    PG_PORT = env('PG_PORT', default='5432')
    PG_DBNAME = env('PG_DBNAME', default='project_db_sheme')
    PG_USER = env('PG_USER', default='pg_user')
    PG_PASS = env('PG_PASS', default='pg_pass')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': PG_DBNAME,
            'USER': PG_USER,
            'PASSWORD': PG_PASS,
            'HOST': PG_HOST,
            'PORT': PG_PORT,
        }
    }  


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Irkutsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = BASE_DIR / 'static'
else:
    STATICFILES_DIRS = (
        BASE_DIR / 'static',
        )

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'
LOGIN_URL = '/user/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
