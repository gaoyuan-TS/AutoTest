# Generated by Django 3.0.5 on 2020-05-08 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_case', '0002_auto_20200508_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='is_delete',
            field=models.IntegerField(default=0, verbose_name='是否删除'),
        ),
    ]