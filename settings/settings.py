# Django settings for pysis project.

import os.path
import posixpath

SETTINGS_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.split(SETTINGS_DIR)[0]
PROJECT_PARENT = os.path.split(PROJECT_ROOT)[0]
PROJECT_NAME = os.path.split(PROJECT_ROOT)[1]

DEBUG = True
TEMPLATE_DEBUG = DEBUG

APPLICATION_NAME = 'Student Information System'
APPLICATION_SHORT_NAME = 'PySIS'
ORGANIZATION = 'Ramakrishna Mission Vidyalaya'
TITLE = '%s | %s' % (APPLICATION_NAME, ORGANIZATION)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
    ('Ramakrishna Mission Vidyalaya', 'info@rmv.ac.in'),
)

DEFAULT_ADMIN_EMAIL = '%s <%s>' % ADMINS[0]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT,'sqlite.db'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
#MEDIA_ROOT = PROJECT_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'jm_z@@6q3$6=ybua9y7e@ql=n8-21xb56l^auar$%+3y06@gm&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'announcements.context_processors.site_wide_announcements',
    PROJECT_NAME + '.misc.context_processors.settings',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'fullhistory.fullhistory.FullHistoryMiddleware',
)

ROOT_URLCONF = PROJECT_NAME + '.urls.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'admin_tools.dashboard',
    'grappelli',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.databrowse',
    'debug_toolbar',
    'south',
    'fullhistory',
    'announcements',
    'avatar',
    'compressor',
    'endless_pagination',

    # My apps
    'profile',
)

FIXTURE_DIRS = (
    os.path.join(PROJECT_ROOT, "fixtures"),
)

# Django-debug-toolbar settings
INTERNAL_IPS = ('127.0.0.1', '127.0.1.1')
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Grappelli
GRAPPELLI_ADMIN_HEADLINE = APPLICATION_NAME
GRAPPELLI_ADMIN_TITLE = APPLICATION_NAME
ADMIN_TOOLS_INDEX_DASHBOARD = PROJECT_NAME + '.misc.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = PROJECT_NAME + '.misc.dashboard.CustomAppIndexDashboard'

from django.contrib import messages
MESSAGE_TAGS = {
    messages.DEBUG : 'info',
    messages.INFO : 'info',
    messages.SUCCESS : 'done',
    messages.WARNING : 'warning',
    messages.ERROR : 'error',
}

MAIN_MENU = [

    # (Name, URL)
    ('Profile', '/profile/'),
    ('Attendance', '/attendance/'),
    ('Marks', '/marks/'),
    ('Library', '/library/'),
    ('Knowledge Base', 'http://kb.rmv.ac.in'),
    ('Institutional Repository', 'http://ir.rmv.ac.in'),
]

PROFILE_MENU = [

    # (Name, URL)
    ('General Details', '/profile/general/'),
    ('Personal Details', '/profile/personal/'),
    ('Family Details', '/profile/family/'),
    ('Contact Details', '/profile/contact/'),
    ('Education Details', '/profile/education/'),
    ('Misc Details', '/profile/misc/'),

]

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/profile'

# Avatar
AUTO_GENERATE_AVATAR_SIZES = (80, 100, 200)
AVATAR_GRAVATAR_BACKUP = False
AVATAR_DEFAULT_URL = posixpath.join(MEDIA_URL, 'images', 'user.png')

# Django-Compressor
COMPRESS = True

# Pagination
ENDLESS_PAGINATION_PER_PAGE = 5
ENDLESS_PAGINATION_LOADING = '<img src="/media/images/loader.gif" alt="loading" />'


# All production settings like sensitive passwords go here.
# Don't forget to exclude this file from version control
try:
    from production_settings import *
except ImportError:
    pass
