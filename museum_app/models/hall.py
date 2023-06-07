from django.db import models

from core import BaseModel


class Hall(BaseModel):
    number = models.IntegerField()
    title = models.TextField()
    floor = models.IntegerField()
    area = models.FloatField()

    def __str__(self):
        return f'{self.title} {self.number}'
