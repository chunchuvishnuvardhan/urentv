# Generated by Django 3.0.8 on 2020-08-28 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newapp', '0021_auto_20200826_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='whatsappno2',
            field=models.CharField(default=models.CharField(max_length=15), max_length=15),
        ),
    ]
