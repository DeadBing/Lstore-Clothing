# Generated by Django 4.1.6 on 2023-05-30 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0004_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=20, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(max_length=200, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=20, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='house',
            field=models.CharField(max_length=20, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='order',
            name='index',
            field=models.CharField(max_length=12, verbose_name='Индекс'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='order',
            name='region',
            field=models.CharField(max_length=20, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(max_length=20, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказы'),
        ),
    ]
