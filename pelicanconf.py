#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Super Blogger'
SITENAME = 'Super Site'
PATH = 'content'
TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = 'en'
LOCALE = 'C'

META_DESCRIPTION = '''Blog, Superman, Spiderman '''

META_KEYWORDS = ['blog']

###############################
SITEURL = ''
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing

FEED_ALL_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

###############################

OUTPUT_PATH = 'output'
PATH = 'content'
PAGE_PATHS = ['pages']

# Themes, Jija and Plugins
THEME = './pelican-themes/pelican-bootstrap3'
PLUGINS = ['i18n_subsites', 'extended_sitemap']
PLUGIN_PATHS = ['./plugins']
JINJA_ENVIRONMENT = {
    'trim_blocks': True,
    'lstrip_blocks': True,
    'extensions': ['jinja2.ext.i18n']
}

# Take this value from http://bootswatch.com/
# Good alternatives: flatly, cosmo, readable, sandstone, united
BOOTSTRAP_THEME = 'formally'

# Presentation parameters
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (('About','/pages/about/'),
			('Archives','/archives.html'),)


STATIC_PATHS = [
    'images',
    'docs',
    'extra/robots.txt',
    'extra/CNAME',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
READERS = {'html': None}
OUTPUT_RETENTION = [".hg", ".git", ".bzr"]
SHOW_DATE_MODIFIED = False
TYPOGRIFY = True
DEFAULT_DATE_FORMAT = '%d %b %Y'
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False


USE_PAGER = True
DEFAULT_PAGINATION = 3
DEFAULT_ORPHANS = 1


AUTHOR_SUBSTITUTIONS = ()
SUMMARY_MAX_LENGTH = 50

BOOTSTRAP_FLUID = False

# SITELOGO = 'images/logo.png'
# SITELOGO_SIZE = '35'
BOOTSTRAP_NAVBAR_INVERSE = False
DISPLAY_BREADCRUMBS = False
DISPLAY_ARTICLE_INFO_ON_INDEX = False
#BANNER = '/path/to/banner.png'
#BANNER_SUBTITLE = 'This is my subtitle'
#BANNER_ALL_PAGES = True
#CC_LICENSE = 'CC-BY'
CC_LICENSE = ''

# URL setttings
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

#CUSTOM_CSS = 'static/custom.css'
# friendly, tango,
PYGMENTS_STYLE = 'tango'
# Configurations taken from sample
# https://raw.githubusercontent.com/getpelican/pelican/master/samples/pelican.conf.py
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
#PYGMENTS_RST_OPTIONS = {'linenos': 'nowrap'}

# MENUITEMS = ()

# Social widget
# SOCIAL = (('GitHub', 'https://github.com/abenkhadra'),
#           ('Linkedin', 'https://www.linkedin.com/in/benkhadraa'),)

LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

HIDE_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False

DOCUTILS_SETTINGS = { 'generator': 0, 'footnote_backlinks': 0 }
# custom page generated with a jinja2 template
# TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
