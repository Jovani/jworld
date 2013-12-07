from utils.models import TimeStampedModel
from django.db import models


# Create your models here.
class Article(TimeStampedModel):
    title = models.CharField(default='', max_length=100)
