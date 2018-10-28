from django.db import models
from django.utils.translation import ugettext as _

from app.querysets import ProductQuerySet


class Product(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    price = models.PositiveIntegerField(verbose_name=_('price'))
    quantity = models.PositiveIntegerField(default=0, verbose_name=_('quantity'))

    objects = ProductQuerySet.as_manager()

    @property
    def in_stock(self):
        return self.quantity >= 1

    def __str__(self):
        return f'#{self.id} {self.title}'

    class Meta:
        verbose_name = _('Product')
