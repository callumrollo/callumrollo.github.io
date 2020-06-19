#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'Callum Rollo'
SITEURL = 'https://callumrollo.github.io'
SITENAME = 'Callum Rollo'
SITETITLE = 'Callum Rollo'
SITESUBTITLE = 'Oceanographer'
SITEDESCRIPTION = "Science should be open. Software should be free. Borders are kind of rubbish "
SITELOGO = SITEURL + '/images/mug.jpg'
FAVICON = SITEURL + '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = '../Flex'
PATH = 'content'
OUTPUT_PATH = 'blog/'
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
	('twitter', 	'https://twitter.com/callum_rollo'),
	 ('github', 	'https://github.com/callumrollo'),
	)

MENUITEMS = (('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10



STATIC_PATHS = ['images', 'figures']
RELATIVE_URLS = True

Port = 8888



