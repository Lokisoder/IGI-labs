from django.contrib.auth.models import User
from django.db import models

from core import BaseModel
from .employee_position import EmployeePosition
from .hall import Hall


class Employee(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    phone_number = models.TextField()

    position = models.ForeignKey(EmployeePosition, on_delete=models.SET_NULL, null=True)
    hall = models.ForeignKey(Hall, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
