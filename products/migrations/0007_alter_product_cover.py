# Generated by Django 4.0.2 on 2023-09-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_datetime_created_alter_review_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, upload_to='static/product_covers', verbose_name='Product Cover'),
        ),
    ]
