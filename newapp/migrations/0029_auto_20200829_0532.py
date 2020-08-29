# Generated by Django 3.0.8 on 2020-08-29 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0028_auto_20200828_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='itemcolour',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='itemname',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='product',
            name='whatsappno2',
            field=models.CharField(max_length=15),
        ),
    ]
