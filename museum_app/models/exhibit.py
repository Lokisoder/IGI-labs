from django.db import models

from core import BaseModel
from .art import Art
from .employee import Employee


class Exhibit(BaseModel):
    title = models.TextField()

    art = models.ForeignKey(Art, on_delete=models.SET_NULL, null=True)
    assigned_employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
