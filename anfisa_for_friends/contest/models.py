from django.db import models

# Create your models here.
from django.db import models

from django.core.validators import MinValueValidator, MaxValueValidator

# Опишите модель Contest здесь!
class Contest(models.Model):
    title = models.CharField(verbose_name='Название', max_length=20)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена',
        help_text='Рекомендованная розничная цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)]
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True
    )