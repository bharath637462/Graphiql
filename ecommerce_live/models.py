from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils.models import ModelMixin
from phonenumber_field.modelfields import PhoneNumberField

class Customer(ModelMixin):

    first_name = models.CharField(_('First Name'), max_length=255, db_index=True)
    middle_name = models.CharField(_('Middle Name'), max_length=255, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=255, blank=True, null=True)
    email = models.EmailField(_('Email'), unique=True, db_index=True)
    phone = PhoneNumberField(_('Phone'), db_index=True, blank=True, null=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'customer'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

class Color(ModelMixin):
    name = models.CharField(_('Name'), max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'color'
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

class Category(ModelMixin):
    name = models.CharField(_('Name'), max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

class SubCategory(ModelMixin):
    name = models.CharField(_('Name'), max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'subCategory'
        verbose_name = _('SubCategory')
        verbose_name_plural = _('SubCategories')

class Product(ModelMixin):
    category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='products',
                                on_delete=models.SET_NULL, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, verbose_name=_('Sub Category'), related_name='products',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(_('Name'), max_length=255, db_index=True)
    price = models.DecimalField(_('Price'))


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class Order(ModelMixin):
    category = models.ForeignKey(Category, verbose_name=_('Category'), related_name='products',
                                on_delete=models.SET_NULL, blank=True, null=True)
    sub_category = models.ForeignKey(SubCategory, verbose_name=_('Sub Category'), related_name='products',
                                 on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(_('Name'), max_length=255, db_index=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class TransactionType(ModelMixin):
    name = models.CharField(_('Name'), max_length=255, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'transaction_type'
        verbose_name = _('Transaction Type')
        verbose_name_plural = _('Transaction Types')


class Rating(ModelMixin):
    rating = models.IntegerField(_('Rating'))
    customer = models.ForeignKey(Category, verbose_name=_('Category'), related_name='products',
                                 on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'transaction_type'
        verbose_name = _('Transaction Type')
        verbose_name_plural = _('Transaction Types')

