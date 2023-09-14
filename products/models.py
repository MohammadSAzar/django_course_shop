from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.utils.translation import gettext as _
from django.urls import reverse
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = RichTextField()
    price = models.PositiveIntegerField(default=0)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(verbose_name=_('Product Image'), upload_to='products/image_and_cover/', blank=True)
    slug = models.SlugField(max_length=250, null=True, blank=True, unique=True, allow_unicode=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-datetime_created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])


class CommentActiveManager(models.Manager):
    def get_queryset(self):
        return super(CommentActiveManager, self).get_queryset().filter(active=True)


class Review(models.Model):
    STARS = [
        ('1', 'Very Bad'),
        ('2', 'Bad'),
        ('3', 'Normal'),
        ('4', 'Good'),
        ('5', 'Very Good'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = RichTextField(verbose_name='متن نظر')
    stars = models.CharField(max_length=10, choices=STARS, verbose_name='امتیاز')
    active = models.BooleanField(default=True)
    datetime = models.DateTimeField(default=timezone.now)

    # Manager
    objects = models.Manager()
    comment_active_manager = CommentActiveManager()

    def __str__(self):
        return f'{self.author}: {self.body}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.slug])

