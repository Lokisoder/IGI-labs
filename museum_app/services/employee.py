from django.http import Http404

from ..models import Employee


class EmployeeService:
    @staticmethod
    def find_by_user(user):
        employee = Employee.objects.filter(user=user).first()

        if not employee:
            raise Http404()

        return
