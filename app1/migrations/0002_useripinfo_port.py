# Generated by Django 2.2.4 on 2019-09-01 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useripinfo',
            name='port',
            field=models.CharField(default='', max_length=10000, null=True, verbose_name='端口信息'),
        ),
    ]
