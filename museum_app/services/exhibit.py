import datetime

from ..models import Exhibit


class ExhibitService:
    @staticmethod
    def _get_exhibits_created_after(created_at):
        return Exhibit.objects.filter(created_at__gt=created_at)

    @classmethod
    def get_recent_exhibits(cls):
        date_half_year_ago = datetime.datetime.now() - datetime.timedelta(days=183)
        return cls._get_exhibits_created_after(date_half_year_ago)
