# Generated by Django 4.0.2 on 2023-08-16 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
