# Generated by Django 4.0.2 on 2023-09-04 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cover',
        ),
    ]
