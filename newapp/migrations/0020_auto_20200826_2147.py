# Generated by Django 3.0.8 on 2020-08-26 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0019_auto_20200826_0813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('comment', models.TextField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(default='', max_length=200),
        ),
    ]