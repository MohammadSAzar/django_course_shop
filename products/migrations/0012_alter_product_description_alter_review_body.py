# Generated by Django 4.0.2 on 2023-09-06 15:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='متن نظر'),
        ),
    ]
