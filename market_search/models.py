from django.db import models

# Create your models here.


# class Users(models.Model):
#     username = models.CharField(max_length=25)
#     full_name = models.CharField(blank=True)
#     password = models.CharField()
#     join_date = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.full_name
#
#     class Meta:
#         verbose_name = "В единственном числе"
#         verbose_name_plural = 'В множественном'
#         ordering = ['join_date', 'username']

class Items(models.Model):
    item_name = models.CharField(max_length=255)
    in_stock = models.BooleanField(default=False)
    link = models.TextField()
    store_name = models.CharField(max_length=30)
