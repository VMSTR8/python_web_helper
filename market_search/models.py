from django.db import models

# Create your models here.


# TODO добавить колонку цены в модель
# TODO Нужно ли делать сколько % скидка команды?
# TODO Продумать модель, что еще добавить
# TODO Добавить колонку с логотипами магазинов

# Model of market items
class Items(models.Model):
    item_name = models.CharField(max_length=255, verbose_name='Наименование товара')
    in_stock = models.BooleanField(default=False, verbose_name='Наличие')
    link = models.TextField(verbose_name='Ссылка')
    store_name = models.CharField(max_length=30, verbose_name='Наименование магазина')

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
