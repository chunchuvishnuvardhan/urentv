# Generated by Django 3.0.8 on 2020-08-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_auto_20200820_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='camdesc',
            field=models.TextField(default='', max_length=100),
        ),
    ]