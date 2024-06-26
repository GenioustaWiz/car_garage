
"""
Django settings for hospital_management_webapp project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "76f38950-9eab-4703-9288-ced63971d2c6"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['cargarage-production.up.railway.app']

CSRF_TRUSTED_ORIGINS = ['https://cargarage-production.up.railway.app']
# Application definition

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    
]
INSTALLED_APPS = [
    'users',
    'main',
    'services',
    'blog',
    'visitors_counter',
    'contact_us',
    # for security enforcement
    # 'axes', #remember to un comment other parts of the code for AXES
    # =========
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party Apps
    'tinymce',
    'django_cleanup', # overrides older images
    'debug_toolbar',
    'phonenumber_field',
    'django_countries',
    'taggit',
    # Django Allauth 
    'django.contrib.sites',  # make sure sites is included
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # 'allauth_2fa',
      # the social providers
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.linkedin_oauth2',
    # end django-allauth
] 
#====pip install django-axes for sec==
# AXES_FAILURE_LIMIT = 5
# AXES_LOCK_OUT_AT_FAILURE = True
# AXES_LOCKOUT_PARAMETERS = [
#         ["ip_address", 
#         "user_agent"]
#     ]
# ==========END==============

# DJango  ALLAUTH
AUTH_USER_MODEL = "users.User"
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'client_id': config('GOOGLE_CLIENT_ID'),
        'secret': config('GOOGLE_SECRET'),
        'key': '',
        'SCOPE': ['profile','email'],
        'AUTH_PARAMS': {'access_type': 'offline'},
        'OAUTH_PKCE_ENABLED': True,
        'redirect_url': 'https://cargarage-production.up.railway.app/accounts/github/login/callback/',  
    },
    'linkedin': {
        'HEADERS': {
            'x-li-src': 'msdk'
        },
        'SCOPE': [
            'openid',
        ],
        # 'PROFILE_FIELDS': [
        #     'id',
        #     'first-name',
        #     'last-name',
        #     'email-address',
        #     'picture-url',
        #     'public-profile-url',
        # ]
    },
    'github': {
        'client_id': config('GITHUB_CLIENT_ID'),
        'secret': config('GITHUB_SECRET'),
        'key': '',
        'SCOPE': [
            'user',
            # 'repo',
            'read:org',
        ],
        'redirect_url': 'https://cargarage-production.up.railway.app/accounts/github/login/callback/',
    },
}

SITE_ID = 1
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
    # EMAIL_BACKEND so allauth can proceed to send confirmation emails
    # ONLY for development/testing use console 
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
    # Make email verification mandatory to avoid junk email accounts
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory' 
# Enable two-factor authentication
# ACCOUNT_ADAPTER = 'allauth_2fa.adapter.OTPAdapter'
ACCOUNT_FORMS = {
    'update_account': 'users.forms.UserUpdateForm',  # Point to your custom form
}
ACCOUNT_SET_PASSWORD_REDIRECT_URL = "/your/profile/"

SOCIALACCOUNT_PIPELINE = (
    'socialaccount.pipeline.social.social_account',
    # ... other pipeline steps ...
)

# End DJango  ALLAUTH

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #new serving static files for production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # New Added
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    # It only formats user lockout messages and renders Axes lockout responses
    # on failed user authentication attempts from login views.
    # If you do not want Axes to override the authentication response
    # you can skip installing the middleware and use your own views.

    # 'axes.middleware.AxesMiddleware',
]


ROOT_URLCONF = 'car_garage.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # this part is for the user_profile, for mostly sending the user Image to the header
                'users.context_processors.user_info',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'car_garage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = "Africa/Nairobi"

USE_I18N = True

USE_L10N = True

USE_TZ = True 


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


STATIC_URL = "/static/"
# This is the directory where the collected static files will be stored.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# This is where Django will look for static files during development.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
#     ) 
MEDIA_URL = '/media/' # Public URL at the browser
MEDIA_ROOT = os.path.join(BASE_DIR, 'media',) # Directory where uploaded media is saved.

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "main_index" #afterlogin
LOGOUT_REDIRECT_URL = "main_index"

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))