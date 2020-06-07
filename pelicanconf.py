#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Callum Rollo'
SITENAME = 'Callum Rollo'
SITETITLE = AUTHOR
SITESUBTITLE = 'Oceanographer'
SITEDESCRIPTION = "Science should be open. Software should be free. Borders are kind of rubbish "
SITEURL = ''
SITELOGO = SITEURL + '/images/mug.jpg'
FAVICON = SITEURL + '/images/favicon.ico'

ROBOTS = 'index, follow'

# Creative Commons Licensing
CC_LICENSE = {
        'name': 'Creative Commons Attribution-ShareAlike',
        'version': '4.0',
        'slug': 'by-sa'
}
COPYRIGHT_YEAR = 2020


THEME = '/media/callum/storage/Documents/foo/Flex'
PATH = 'content'
STATIC_PATHS = ['images', 'figures']
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']
TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None





# Social widget
SOCIAL = (
	('twitter', 	'https://twitter.com/callum_rollo'),
	 ('github', 	'https://github.com/callumrollo'),
	)



DEFAULT_PAGINATION = 10



