# Generated by Django 3.0.8 on 2020-08-21 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_product_camdesc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='camdesc',
        ),
    ]