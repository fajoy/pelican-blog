#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


#ref http://docs.getpelican.com/en/3.3.0/settings.html
AUTHOR = u'fajoy'
SITENAME = u'Fajoy的筆記'
SITEURL = ''

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
DEFAULT_CATEGORY = "筆記"

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

