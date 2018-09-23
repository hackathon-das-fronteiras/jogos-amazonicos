from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
# class Gamer(AbstractUser):
#     class Meta:
#         db_table = 'gamer'
#
#     score = models.IntegerField(_('Score'), default=0)
#
#
class Country(models.Model):
    class Meta:
        db_table = 'country'
        verbose_name = _('país')
        verbose_name_plural = _('países')

    def __str__(self):
        return self.country_name

    def __unicode__(self):
        return self.country_name

    country_name = models.CharField(_('País'), max_length=40, unique=True)


class Region(models.Model):
    class Meta:
        db_table = 'region'
        verbose_name = _('região')
        verbose_name_plural = _('regiões')

    def __str__(self):
        return self.region_name

    def __unicode__(self):
        return self.region_name

    region_name = models.CharField(_('Região'), max_length=40, unique=True)
    country = models.ForeignKey(Country, verbose_name=_('País'), on_delete=None)
