import csv
import os

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


def talks_from_file():
    talks = {}
    with open(CSV_FILE_PATH) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            title = row[LABEL_TITLE]
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
            }
    return talks
