# Generated by Django 3.0.8 on 2020-08-23 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_auto_20200823_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='itemname',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(max_length=30),
        ),
    ]
