import csv
import os
from datetime import datetime

from django.conf import settings
from django.utils.text import slugify

CSV_FILE_NAME = 'talks.csv'

CSV_FILE_PATH = os.path.join(settings.BASE_DIR, CSV_FILE_NAME)

LABEL_TITLE = 'title'
LABEL_NAME = 'name'
LABEL_AVATAR = 'avatar'
LABEL_BIO = 'bio'
LABEL_TWITTER = 'twitter'
LABEL_URL = 'url'
LABEL_ABSTRACT = 'abstract'
LABEL_DESCRIPTION = 'description'
LABEL_NOTES = 'notes'
LABEL_AUDIENCE_LEVEL = 'audience_level'
LABEL_TAGS = 'tags'
LABEL_CATEGORY = 'category'
LABEL_LANG = 'lang'
LABEL_TRACK = 'track'
LABEL_DAY = 'day'
LABEL_START = 'start'
LABEL_END = 'end'


def talks_from_file():
    talks = {}
    with open(CSV_FILE_PATH, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = row[LABEL_TITLE]
            try:
                day = datetime.strptime(row[LABEL_DAY], '%d/%m/%Y')
            except ValueError:
                day = None
            names = row["name"].replace(' & ', ',').replace(' y ', ',').split(',')
            speakers = ", ".join(names) if len(names) > 2 else "\n".join(names)

            talks[slugify(title)] = {
                'title': title,
                'name': row[LABEL_NAME],
                'avatar': row[LABEL_AVATAR],
                'bio': row[LABEL_BIO],
                'twitter': row[LABEL_TWITTER],
                'url': row[LABEL_URL],
                'abstract': row[LABEL_ABSTRACT],
                'description': row[LABEL_DESCRIPTION],
                'notes': row[LABEL_NOTES],
                'level': row[LABEL_AUDIENCE_LEVEL],
                'tags': row[LABEL_TAGS],
                'category': row[LABEL_CATEGORY],
                'lang': row[LABEL_LANG],
                'track': row[LABEL_TRACK],
                'day': day,
                'start': row[LABEL_START],
                'end': row[LABEL_END],
                'speakers': speakers,
            }
    return talks
