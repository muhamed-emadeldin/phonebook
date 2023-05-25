import environ
from pathlib import Path

basedir = Path(__file__).resolve().parent.parent.parent
env     = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(basedir.joinpath('.env'))
SECRET_KEY = env('SECRET_KEY')

# Database
DATABASES = {
    'default': {
        'ENGINE': env('ENGINE'),
        'NAME': env('NAME'),
        'HOST': env('HOST'),
        'USER': env('USER_DB'),
        'PASSWORD': env('PASS_DB'),
        'PORT':3600,
    }
}

PRIVATEAPP  = [
    'modules.users',
    "debug_toolbar",
]

LOGIN_URL           = 'users:login'
LOGOUT_REDIRECT_URL = 'users:signup'

#-->AUTH
AUTH_USER_MODEL = env('AUTH_USER_MODEL')

MIDDLEWARE  =   [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]    

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Set our static and media files
STATIC_CDN_UBER    = Path.joinpath(basedir, 'phonebook_cdn_static')
STATICFILES_DIRS    = [Path.joinpath(basedir, 'phonebook/app_static')]
STATIC_ROOT         = Path.joinpath(STATIC_CDN_UBER, 'static')
MEDIA_ROOT          = Path.joinpath(STATIC_CDN_UBER, 'media')
STATIC_URL          = '/static/'
MEDIA_URL           = '/media/'

#-->Set wsgi file
WSGI_APPLICATION = 'config.wsgi.application'


# --> Django DebugToolBar
INTERNAL_IPS = [
    # ...
    "0.0.0.0",
    # ...
]


