# Generated by Django 2.1.2 on 2019-09-15 16:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0018_auto_20190915_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 15, 18, 2, 4, 236271)),
        ),
    ]
