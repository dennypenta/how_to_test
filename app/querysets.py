from django.db.models import QuerySet


class ProductQuerySet(QuerySet):
    def in_stock(self):
        return self.all().filter(quantity__gte=1)
