# Generated by Django 3.0.8 on 2020-08-23 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_product_itemcolour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='itemsize',
            field=models.CharField(default='', max_length=10),
        ),
    ]
