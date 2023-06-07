from django.db import models

from core import BaseModel
from .employee import Employee
from .exhibit import Exhibit


class Tour(BaseModel):
    code = models.TextField()
    title = models.TextField()
    date = models.DateTimeField()
    exhibits = models.ManyToManyField(Exhibit)
    amount_of_people = models.IntegerField(default=0)

    guide = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.title} {self.code}'
