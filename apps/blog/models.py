from utils.models import TimeStampedModel
from django.db import models


# Create your models here.
class Article(TimeStampedModel):
    title = models.CharField(default='', max_length=100)
    url_slug = models.CharField(default='', max_length=50, db_index=True)
    short_description = models.CharField(default='', max_length=255)
    template_name = models.CharField(default='', max_length=100)

    def __unicode__(self):
        return self.title
