from django.db import models
from django.urls import reverse


def get_product_url(obj,viewname):
    ct_model = obj.__class__._meta.model_name

    return reverse(viewname, kwargs={ 'slug': obj.slug})

class Product(models.Model):

    class meta:
        abstract = True
    class Meta:
        verbose_name = ('Продукт')
        verbose_name_plural = ('Продукти')

    title = models.CharField(max_length=255,verbose_name='Назва курсу')
    slug = models.SlugField(unique=True,blank=True)
    start_date = models.DateField(verbose_name='Дата початку')
    end_date = models.DateField(verbose_name='Дата закінчення')
    quantity_lections = models.IntegerField(verbose_name='Кількість лекцій')
    photo = models.ImageField(verbose_name='Зображення')
    description = models.TextField(verbose_name='Опис',blank=True)
    small_description = models.TextField(verbose_name='Коротний опис',blank=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')




