
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+@nu*h!3$ah1^6wg!x@t6(az!sq1c=ff-i69vmw@xq$$-ijd-_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog.apps.BlogConfig',
    'users.apps.UsersConfig',
    'dynamic.apps.DynamicConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'widget_tweaks',
    'storages',
    'face_detector',
    'advance',
    'middleware_demo',
    'rooms.apps.RoomsConfig',
    'social_django',
    'test_mod',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # #cache_middleware
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    #social_django
    'social_django.middleware.SocialAuthExceptionMiddleware',


    #middleware_demo

]




ROOT_URLCONF = 'django_project.urls'

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


                #social_django
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',

    'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'root')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'


# CACHES = {
#     'default':{
#         "BACKEND": "django.core.cache.backends.db.DatabaseCache",
#         'LOCATION': 'blog_cache',
#         "TIMEOUT": 300,
#         'OPTIONS':{
#             "MAX_ENTRIES": 10, 
#             "CULL_FREQUENCY": 1,
#         }
#     }
# }


CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog-home'
LOGIN_URL = 'login'



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'rashidhamid139@gmail.com'
EMAIL_HOST_PASSWORD = ''

DEFAULT_FROM_USER = EMAIL_HOST_USER



AWS_ACCESS_KEY_ID="AKIA45TUDZS3UUHTR6GN"  
AWS_SECRET_ACCESS_KEY="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"
AWS_STORAGE_BUCKET_NAME="data-for-all-files139"
AWS_SS3_REGION_NAME = "ap-south-1"
AWS_S3_SIGNATURE_VERSION = 's3v4'


AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'




#social-django
SOCIAL_AUTH_GITHUB_KEY = 'e0226c674f88cac56b5d'
SOCIAL_AUTH_GITHUB_SECRET = 'eed03edd34c0525a25b5fb0b77c4ae029ddd7799'

SOCIAL_AUTH_FACEBOOK_KEY = '375927473370726'
SOCIAL_AUTH_FACEBOOK_SECRET = 'cf5c63019cbe4f9ae6f2f598c45f8f2c'


SOCIAL_LINKS = {
    'github': 'https://github.com/rashidhamid139',
    'facebook': 'https://www.facebook.com/rashid.hamid3?ref=bookmarks',
    'twitter':  'https://twitter.com/rashidhamid139',
    'linkedin':  'https://www.linkedin.com/in/rashid-hamid-dar-698279b7/',
    'instagram':  '',
}


# LOGGING = {
#     'version': 1,
#     # Version of logging
#     'disable_existing_loggers': False,
#     #disable logging 
#     # Handlers #############################################################
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'dataforall.log',
#         },
# ########################################################################
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     # Loggers ####################################################################
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console'],
#             'level': 'DEBUG',
#             'propagate': True,
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG')
#         },
#     },
# }
