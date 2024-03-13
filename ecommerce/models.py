from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(_('Name'), max_length=50, unique=True)
    description = models.TextField(_('Description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Material(models.Model):

    category = models.ForeignKey(Category,  verbose_name=_('Category'), related_name='materials', on_delete=models.CASCADE )
    name = models.CharField(_('Name'), max_length=50, unique=True)
    description = models.TextField(_('Description'), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'material'
        verbose_name = _('Material')
        verbose_name_plural = _('Materials')


class Type(models.Model):
    category = models.ManyToManyField(Category,  verbose_name=_('Category'), related_name='types')
    name = models.CharField(_('Name'), max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type'
        verbose_name = _('Type')
        verbose_name_plural = _('Types')
