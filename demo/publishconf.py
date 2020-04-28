#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://flex-demo.farrel.franqois.id'
RELATIVE_URLS = False

USE_CDN = False

CC_LICENSE['distribution-type'] = 'custom'
CC_LICENSE['custom-url'] = 'https://cdn.statically.io/img/images.farrel.franqois.id/q=90,ssl=1/misc/cc'
CC_LICENSE['otherwise-noted-url'] = '{0}/ketentuan-dan-kebijakan-blog'.format(SITEURL)

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

EXTRA_FILES_NAME = [
    '_headers',
    '_redirects',
    'ads.txt',
    'keybase.txt',
    'BingSiteAuth.xml',
]

if USE_MINIFIED_SCRIPTS == True:
    CUSTOM_JS_NAME = 'custom.min.js'
    CUSTOM_CSS_NAME = 'custom.min.css'

else:
    CUSTOM_JS_NAME = 'custom.js'
    CUSTOM_CSS_NAME = 'custom.css'

# Mengatur Letak CSS yang di kustom
if USE_CDN:
    CUSTOM_CSS = 'content/extras/{0}'.format(CUSTOM_CSS_NAME)
    CUSTOM_JS = 'content/extras/{0}'.format(CUSTOM_JS_NAME)

else:
    CUSTOM_CSS = CUSTOM_CSS_NAME
    CUSTOM_JS = CUSTOM_JS_NAME

if USE_CDN or USE_MINIFIED_SCRIPTS == True:
    STATIC_PATHS.remove('extras/custom.css')
    del EXTRA_PATH_METADATA['extras/custom.css']
    STATIC_PATHS.remove('extras/custom.js')
    del EXTRA_PATH_METADATA['extras/custom.js']

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
