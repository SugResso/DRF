from django.db import models
from django.contrib.auth.models import User


class Film(models.Model):

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    title = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    content = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор(ша)')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return f"{self.pk}:{self.title}"


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
