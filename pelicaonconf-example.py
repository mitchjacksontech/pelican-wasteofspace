#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mitch'
SITENAME = 'A Pelican Waste of Space'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

THEME = 'themes/pelican-wasteofspace'

SITESUBTITLE = 'Custom-made, luxury planet building.'
HEADER_IMAGE = '/theme/images/header-image.png'

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_TAGS_ON_HEADER = True

SOCIAL = (('phone','tel:5558675309'),
          ('envelope-open','mailto:adams@magrathea.co'),
          ('facebook','https://facebook.com/mitchjacksontech'),
          ('github','https://github.com/mitchjacksontech'),
          ('linkedin','https://linkedin.com/in/mitchjacksontech'))

LINKS_TITLE = 'powered by:'
LINKS = (('Pelican','https://github.com/getpelican/pelican'),
         ('pelican-wasteofspace theme','#'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('Boostrap', 'https://getbootstrap.com'),
         ('Linode', 'https://linode.com'))
COPYRIGHT_SLUG = '2017 Jackson Runs Some Servers'


# JINJA Filter sort_by_article_count
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
