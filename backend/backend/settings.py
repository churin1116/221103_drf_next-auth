from pathlib import Path
from .settings_local import *
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = [
    '127.0.0.1',
    '160.251.12.90', #東京のサーバーIP
    'nakabayashi-kakomon.com',
]

CSRF_TRUSTED_ORIGINS=['http://localhost:3000','http://160.251.12.90/','https://160.251.12.90','http://nakabayashi-kakomon.com/','https://nakabayashi-kakomon.com/']

CORS_ORIGIN_WHITELIST=[
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 以下追加
    'testapp',
    'rest_framework',
    'corsheaders',
    'django.contrib.sites',
    'rest_framework.authtoken',
    'accounts',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # 追加（一番上）
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

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
                # 以下追加
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'



# allauth Googleプロバイダー設定
# https://django-allauth.readthedocs.io/en/latest/providers.html#google
SOCIALACCOUNT_PROVIDERS={
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}
# allauth設定
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_EMAIL_VERIFICATION="none"
SOCIALACCOUNT_EMAIL_REQUIRED=False
# dj_rest_auth設定
# https://dj-rest-auth.readthedocs.io/en/latest/installation.html
SITE_ID=1
# https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
REST_USE_JWT=True
REST_AUTH_SERIALIZERS={
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.UserSerializer'
}
# REST Framework設定
REST_FRAMEWORK={
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "dj_rest_auth.utils.JWTCookieAuthentication",
    ),
}
# Simple JWT設定
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
SIMPLE_JWT={
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,
    "USER_ID_FIELD": "userId",
    "USER_ID_CLAIM": "user_id",
}
AUTH_USER_MODEL = 'accounts.CustomUser'



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':{"min_length":6},
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL   = "/media/"
MEDIA_ROOT  = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
SESSION_COOKIE_AGE = 30 * 24 * 60 * 60 # 60 minutes * 24 * 30
SESSION_SAVE_EVERY_REQUEST = True

# LOGIN_URL = 'testapp/login' # 未ログイン状態でのリダイレクト先
# LOGIN_REDIRECT_URL = 'testapp/index' # ログイン認証後のリダイレクト先
# LOGOUT_REDIRECT_URL = 'testapp/login' # ログアウト時の遷移先

