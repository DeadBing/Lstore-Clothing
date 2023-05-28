from django.db import models
from django.urls import reverse



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    materials = models.CharField(max_length=100)
    price = models.IntegerField( null=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    photo3 = models.ImageField(upload_to="photos/%Y/%m/%d", null=True)
    time_create = models.TimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'did': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cid': self.pk})

