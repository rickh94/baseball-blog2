#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

STAGE = os.environ.get("STAGE", "dev")

AUTHOR = "Rick Henry"
SITENAME = "Baseball Blog"
SITESUBTITLE = "A companion blog to a non-existent baseball team"
SITEURL = os.environ.get("SITEURL", "")
THEME = "themes/future-imperfect"

FEATURED_CATEGORY = "Weird Rules"

PATH = "content"

TIMEZONE = "America/New_York"
DEFAULT_DATE_FORMAT = "%B %d, %Y"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (("You can add links in your config file", "#"), ("Another social link", "#"))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = STAGE == "dev"

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["sitemap", "assets"]
SITEMAP = {"format": "xml"}

sass_style = "expanded" if STAGE == "dev" else "compressed"

ASSET_CONFIG = (
    ("SASS_STYLE", sass_style),
    ("SASS_LINE_COMMENTS", ""),
    ("SASS_BIN", "/usr/bin/sass"),
)
