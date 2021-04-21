# Generated by Django 3.1.7 on 2021-04-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_productvariant_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='collection-backgrounds'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products'),
        ),
    ]
