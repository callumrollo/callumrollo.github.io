#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import json
from pathlib import Path
if Path("secrets.json").exists():
    with open("secrets.json") as json_file:
        secrets = json.load(json_file)
    SITEURL = secrets['url']
else:
    SITEURL = "https://callumrollo.github.io"

AUTHOR = 'Callum Rollo'
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
SITENAME = 'Callum Rollo'
SITETITLE = 'Callum Rollo'
SITESUBTITLE = 'Recovering oceanographer'
SITEDESCRIPTION = "Science should be open. Software should be free. No one is illegal"
SITELOGO = SITEURL + '/images/mug.jpg'
FAVICON = SITEURL + '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
ARTICLE_ORDER_BY = 'reversed-modified'

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
HOME_HIDE_TAGS = False

GITHUB_URL = 'http://github.com/callumrollo/'

LINKS = (('blog', '/'),
        )

SOCIAL = (
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
DEFAULT_PAGINATION = 50



STATIC_PATHS = ['images']



