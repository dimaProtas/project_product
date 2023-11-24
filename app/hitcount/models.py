from django.db import models


class HitCount(models.Model):
    path = models.CharField(max_length=255, primary_key=True)
    hits = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.path} ({self.hits})'