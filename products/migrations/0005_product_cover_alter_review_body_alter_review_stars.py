# Generated by Django 4.0.2 on 2023-09-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.ImageField(blank=True, upload_to='product/product_cover', verbose_name='Product Cover'),
        ),
        migrations.AlterField(
            model_name='review',
            name='body',
            field=models.TextField(verbose_name='متن نظر'),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.CharField(choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Very Good')], max_length=10, verbose_name='امتیاز'),
        ),
    ]