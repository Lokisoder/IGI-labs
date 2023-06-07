from django.db import models

from core import BaseModel


class Art(BaseModel):
    title = models.TextField()

    def __str__(self):
        return self.title
