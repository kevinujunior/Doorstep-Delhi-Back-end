# Generated by Django 3.2.4 on 2021-06-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210627_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='is_promotional',
            field=models.BooleanField(default=False),
        ),
    ]