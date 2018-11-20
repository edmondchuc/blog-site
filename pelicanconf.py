#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Edmond Chuc'
SITENAME = 'Edmond Chuc\'s Blog'
SITEURL = 'https://www.edmondchuc.com/blog'

PATH = 'content'

TIMEZONE = 'Australia/Brisbane'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme path
THEME = 'Flex'

# Flex theme settings
# https://github.com/alexandrevicenzi/Flex/wiki/Configuration-example
SITETITLE = 'Edmond Chuc'
SITESUBTITLE = 'Software Developer'
SITEDESCRIPTION = 'Edmond Chuc\'s, a software developer\'s portfolio and blogging website.'
SITELOGO = 'https://www.edmondchuc.com/static/img/me-pic.jpg'
FAVICON = 'https://www.edmondchuc.com/static/img/favicon.ico'
BROWSER_COLOR = '#333'
ROBOTS = 'index, follow'
COPYRIGHT_YEAR = '2018 by Edmond Chuc'