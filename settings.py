# -*- coding: utf-8 -*-
from ragendja.settings_pre import *

DEBUG = False

# Increase this when you update your media on the production site, so users
# don't have to refresh their cache. By setting this your MEDIA_URL
# automatically becomes /media/MEDIA_VERSION/
MEDIA_VERSION = 1

# By hosting media on a different domain we can get a speedup (more parallel
# browser connections).
#if on_production_server or not have_appserver:
#    MEDIA_URL = 'http://media.mydomain.com/media/%d/'

# Add base media (jquery can be easily added via INSTALLED_APPS)
COMBINE_MEDIA = {
    'combined-%(LANGUAGE_CODE)s.js': (
        # See documentation why site_data can be useful:
        # http://code.google.com/p/app-engine-patch/wiki/MediaGenerator
        '.site_data.js',
    ),
    'combined-%(LANGUAGE_DIR)s.css': (
        'global/look.css',
        'global/style.css',
    ),
}

# Change your email settings
if on_production_server:
    DEFAULT_FROM_EMAIL = 'bla@bla.com'
    SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Make this unique, and don't share it with anybody.
SECRET_KEY = '1234567890'

#ENABLE_PROFILER = True
#ONLY_FORCED_PROFILE = True
#PROFILE_PERCENTAGE = 25
#SORT_PROFILE_RESULTS_BY = 'cumulative' # default is 'time'
# Profile only datastore calls
#PROFILE_PATTERN = 'ext.db..+\((?:get|get_by_key_name|fetch|count|put)\)'

# Enable I18N and set default language to 'en'
USE_I18N = True
LANGUAGE_CODE = 'en'

# Restrict supported languages (and JS media generation)
LANGUAGES = (
    ('de', 'German'),
    ('en', 'English'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.i18n',
    'misc.context_processors.site_attributes',
)

# We will need to define this tuple explicitly in order to use 
# the improved ragendja template functionality
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'ragendja.template.app_prefixed_loader',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'ragendja.middleware.ErrorMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Django authentication
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Google authentication
    #'ragendja.auth.middleware.GoogleAuthenticationMiddleware',
    # Hybrid Django/Google authentication
    #'ragendja.auth.middleware.HybridAuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

# Google authentication
#AUTH_USER_MODULE = 'ragendja.auth.google_models'
#AUTH_ADMIN_MODULE = 'ragendja.auth.google_admin'
# Hybrid Django/Google authentication
#AUTH_USER_MODULE = 'ragendja.auth.hybrid_models'

LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
    # Add jquery support (app is in "common" folder). This automatically
    # adds jquery to your COMBINE_MEDIA['combined-%(LANGUAGE_CODE)s.js']
    # Note: the order of your INSTALLED_APPS specifies the order in which
    # your app-specific media files get combined, so jquery should normally
    # come first.
    'jquery',

    # Add blueprint CSS (http://blueprintcss.org/)
    'blueprintcss',

    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sites',
    'appenginepatcher',
    'ragendja',
    'myapp',
    'registration',
    'mediautils',

    'homepage',
    'menu',
    'misc',
    'blog', 
    'contact',
    'pagination',
)
SITE_ATTRIBUTES = {
    'name':'Calvin\'s (Web)log',
    'tagline':'(mis)adventures, creative programming and perspectives',
    'yui':'http://yui.yahooapis.com',
    'jquery':'http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js',

    ### the hostname is set dynamically in misc/context_processors.py for templates. if you need it somewhere else use request.get_host()
    'hostname':'http://hobbes006.appspot.com', # for use in the email templates
    'hostname_ssl':'https://hobbes006.appspot.com', # for use in the email templates
    
    #'FTS_PER_PAGE': 20, # full-text search - results per page
    # HTTPS
    #'CAN_USE_SSL': False, # for the devserver. it will be orverriden in local_settings.py.server

}

# List apps which should be left out from app settings and urlsauto loading
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = (
    # Example:
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'yetanotherapp',
)

# Remote access to production server (e.g., via manage.py shell --remote)
DATABASE_OPTIONS = {
    # Override remoteapi handler's path (default: '/remote_api').
    # This is a good idea, so you make it not too easy for hackers. ;)
    # Don't forget to also update your app.yaml!
    #'remote_url': '/remote-secret-url',

    # !!!Normally, the following settings should not be used!!!

    # Always use remoteapi (no need to add manage.py --remote option)
    #'use_remote': True,

    # Change appid for remote connection (by default it's the same as in
    # your app.yaml)
    #'remote_id': 'otherappid',

    # Change domain (default: <remoteid>.appspot.com)
    #'remote_host': 'bla.com',
}

from ragendja.settings_post import *
