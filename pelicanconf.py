#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Brenhilt"
SITENAME = "チラシの裏も印刷されてる"
SITEURL = ""
THEME = "themes/gum"
THEME = "themes/voidy-bootstrap"
THEME = "themes/medius"

PATH = "content"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}{date:%d}{slug}.html"
ARTICLE_URL = "{date:%Y}/{date:%m}{date:%d}{slug}"

TIMEZONE = "Asia/Tokyo"

DELETE_OUTPUT_DIRECTORY = True
DEFAULT_LANG = "ja"
DATE_FORMATS = {"ja": "%Y/%m/%d", "en": "%d-%m-%Y"}
DRAFT_URL = "drafts/{date:%Y}{date:%m}{date:%d}{slug}"
DRAFT_SAVE_AS = "drafts/{date:%Y}{date:%m}{date:%d}{slug}.html"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://python.org/"),
    ("b13t.net", "https://b13t.net/"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/__Bren",),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

if THEME == "themes/voidy-bootstrap":
    STYLESHEET_FILES = [
        "voidybootstrap.css",
    ]
