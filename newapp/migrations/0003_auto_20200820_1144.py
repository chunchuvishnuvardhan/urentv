# Generated by Django 3.0.8 on 2020-08-20 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20200820_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='cam_model',
            new_name='cammodel',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cam_name',
            new_name='camname',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cam_owner',
            new_name='camowner',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cam_pic',
            new_name='campic',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cam_rentperday',
            new_name='camrentperday',
        ),
    ]