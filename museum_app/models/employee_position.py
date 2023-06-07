from django.db import models

from core import BaseModel


class EmployeePosition(BaseModel):
    title = models.TextField()

    def __str__(self):
        return self.title
