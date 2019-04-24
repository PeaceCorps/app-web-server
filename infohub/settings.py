import os
from infohub.config import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@0kjw@u5rv7mf!s2j8ix7lq@n%w&v$6p8ku%8hkmmxxj$w44ys'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR,'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'debug': DEBUG,
            },
            'OPTIONS': {
                    'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',

                    'social_django.context_processors.backends',  # <--
                    'social_django.context_processors.login_redirect', # <--
                ],
            },

        },]

# ALLOWED_HOSTS = ['0.0.0.0','localhost','192.168.33.10','192.168.33.10:8000']


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'infohub',
    'malaria_web',
    'malaria_api',
    'webhub',
    'profiles',
    'pcsa',
    'pcsa_GHN',
    'pcsa_safety_tools',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
    'social_django',
    'firstaide',
    'django_wysiwyg',
    'ckeditor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    "allauth.account.auth_backends.AuthenticationBackend"
)

ROOT_URLCONF = 'infohub.urls'

WSGI_APPLICATION = 'infohub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'webapp',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = '/vagrant/submit/media/propics/'
STATIC_URL = '/static/'
STATIC_ROOT = ''

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}
# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# SMTP Settings
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'pc.mobile.control.center@gmail.com'
SERVER_EMAIL = 'pc.mobile.control.center@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'pc.mobile.control.center.com'
EMAIL_HOST_PASSWORD = 'alphadeltaepsilon'
EMAIL_PORT = 465

SWAGGER_SETTINGS = {
    'is_authenticated': True,
}

DJANGO_WYSIWYG_FLAVOR = "ckeditor"


# Django allauth configurations

# AUTHENTICATION_BACKENDS = (
#     # Needed to login by username in Django admin, regardless of `allauth`
#     "django.contrib.auth.backends.ModelBackend",
#     # `allauth` specific authentication methods, such as login by e-mail
#     "allauth.account.auth_backends.AuthenticationBackend"
# )

# To redirect to root page when login is required
LOGIN_REDIRECT_URL = '/'

# Logout from the account when password is changed
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True

# Email not verified yet since there is a two step authentication used in the email for sending Authentication messages
ACCOUNT_EMAIL_VERIFICATION ="none"
