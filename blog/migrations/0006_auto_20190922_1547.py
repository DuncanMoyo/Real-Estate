# Generated by Django 2.1.2 on 2019-09-22 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190915_2137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]