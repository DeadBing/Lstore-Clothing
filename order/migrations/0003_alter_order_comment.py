# Generated by Django 4.1.6 on 2023-04-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
