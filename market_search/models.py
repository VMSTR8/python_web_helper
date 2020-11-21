from django.db import models
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex


# Model of market items
class Items(models.Model):
    item_name = models.CharField(max_length=255, unique=True, verbose_name='Наименование товара')
    in_stock = models.BooleanField(default=False, verbose_name='Наличие')
    link = models.TextField(verbose_name='Ссылка')
    price = models.IntegerField(null=True, blank=True, verbose_name='Цена магазина')
    store_name = models.CharField(max_length=30, verbose_name='Наименование магазина')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, blank=True,
                                 verbose_name='Категория')
    store = models.ForeignKey('Stores', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Магазин')
    search_vector = SearchVectorField(null=True, blank=True)

    def __str__(self):
        return self.item_name

    class Meta(object):
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        indexes = [GinIndex(fields=['search_vector'])]


# Categories for items
class Categories(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


# Store details
class Stores(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Нзвание магазина')
    description = models.TextField(blank=True, verbose_name='Описание магазина')
    discount = models.TextField(blank=True, verbose_name='Скидка для команды')
    logo = models.ImageField(upload_to='store_logo/%Y/%m/%d/', blank=True, verbose_name='Логотип')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
