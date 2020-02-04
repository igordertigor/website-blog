#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ingo Fruend'
SITENAME = 'Ingo Fruend'
SITEURL = 'https://ingofruend.net'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

THEME = 'mypelican'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Github', 'https://github.com/igordertigor'),
    ('LinkedIn', 'https://www.linkedin.com/in/ingofruend/'),
 )

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/Ingo__Starr'),
)

DEFAULT_PAGINATION = 10
DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# AUTHOR_SAVE_AS = ''  # Do not generate author pages
