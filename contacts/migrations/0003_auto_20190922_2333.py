# Generated by Django 2.1.2 on 2019-09-22 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190922_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='message',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
    ]
