#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


#ref http://docs.getpelican.com/en/3.3.0/settings.html
AUTHOR = u'fajoy'
AUTHOR_URL = u'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
AUTHORS_URL = 'authors.html'
AUTHORS_SAVE_AS = 'authors.html' 
SITENAME = u'Fajoy的資訊筆記'
SITEURL = ''

STATIC_PATHS = ('img','js','css','html')
PAGE_DIR = 'pages'
PAGE_EXCLUDES = ()
ARTICLE_DIR = ''
ARTICLE_EXCLUDES = (PAGE_DIR,) + STATIC_PATHS





DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives')

MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']


TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh-TW'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)


DEFAULT_PAGINATION = False

RELATIVE_URLS = True

import os
THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    'pelican-themes', 'fajoy-bootstrap2')

DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT ="%Y年%m月%d日"
LOCALE = ("zh_TW.UTF-8")

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = u"筆記"

DISQUS_SITENAME = "fajoy"
GOOGLE_ANALYTICS = "UA-11470637"


PLUGIN_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    'pelican-plugins')
PLUGINS = ['pdf',]

PDF_PROCESSOR = True
PDF_GENERATOR = True
PDF_STYLE = 'chinese.style'
PDF_STYLE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    'win_fonts')

