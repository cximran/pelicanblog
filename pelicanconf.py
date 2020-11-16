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
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
STATIC_PATHS=['images','pdfs','extra','pdf']
BOOTSTRAP_STYLESHEET ="slate_bootstrap.css"
SUMMARY_MAX_LENGTH = 150
GOOGLE_ANALYTICS = "UA-36952440-1"
TWITTER_USERNAME = "Imran_Malek"
CUSTOM_SIDEBAR_TOP = "Hello, Custom Sidebar Top"
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
RELATIVE_URLS = True
SIDEBAR = "sidebar.html"
CUSTOM_SIDEBAR_TOP = "sidebar_top.html"
FONT_AWESOME_CDN_LINK = {
    'href': 'https://use.fontawesome.com/releases/v5.0.13/css/all.css',
    'integrity': 'sha384-DNOHZ68U8hZfKXOrtjWvjxusGo9WQnrNx2sqG0tfsghAvtVlRW3tvkXWZh58N9jp',
    'crossorigin': 'anonymous'
}
SKIP_DEFAULT_NAVIGATION = False
SOCIAL = (
        ('Twitter', 'https://twitter.com/imran_malek',
        'fab fa-twitter-square fa-fw fa-lg'),
        ('LinkedIn', 'https://linkedin.com/in/imranmalek/',
        'fab fa-linkedin fa-fw fa-lg'),
        ('GitHub', 'https://github.com/cximran',
        'fab fa-github-square fa-fw fa-lg'),
        )
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
    'extra/CNAME': {'path': 'CNAME'},
    'extra/LICENSE': {'path': 'LICENSE'},
    'extra/README': {'path': 'README'},
}
