# -*- coding: utf-8 -*-

BOT_NAME = 'markus_uk'

SPIDER_MODULES = ['markus_uk.spiders']
NEWSPIDER_MODULE = 'markus_uk.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'

ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS = ['Date', 'Match Time', 'Home Team', 'Away Team', 'Home Team Half-Time Score', 'Home Team Full-Time Score', 'Away Team Half-Time Score', 'Away Team Full-Time Score']
