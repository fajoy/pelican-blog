#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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
                                    'pelican-themes', 'pelican-bootstrap3')

DEFAULT_DATE = "fs"
DEFAULT_DATE_FORMAT ="%Y年%m月%d日"
LOCALE = ("zh_TW.UTF8")
