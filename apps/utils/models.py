from django.db import models

# Create your models here.
    date_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_date_modified(self):
        return self.date_modified.strftime('%Y-%m-%d')

    class Meta:
        abstract = True
