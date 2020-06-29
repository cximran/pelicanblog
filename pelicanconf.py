#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
PLUGINS=['pelican-plugins.assets']
AUTHOR = 'Imran Malek'
SITENAME = 'Imran Malek'
SITEURL = 'http://imranmalek.com'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS=['images','pdfs']
BOOTSTRAP_STYLESHEET ="slate_bootstrap.css"
SUMMARY_MAX_LENGTH = 150
GOOGLE_ANALYTICS = "UA-36952440-1"
TWITTER_USERNAME = "Imran_Malek"
# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
THEME = "pelican-themes/voidy-bootstrap-master"
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

SKIP_DEFAULT_NAVIGATION = True
