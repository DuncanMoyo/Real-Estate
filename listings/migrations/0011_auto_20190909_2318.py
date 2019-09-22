# Generated by Django 2.1.2 on 2019-09-09 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_auto_20190909_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='amenities',
        ),
        migrations.AddField(
            model_name='listing',
            name='amenities',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Amenity'),
        ),
    ]
