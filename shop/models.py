from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Category(models.Model):
    category_name = models.CharField('название категории', max_length=50)

    def __str__(self):
        return 'Категория: ' + self.category_name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    subcategory_name = models.CharField('название подкатегории', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Item(models.Model):
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField('название товара', max_length=50)
    image = models.ImageField()
    price = models.FloatField()

    rating = models.FloatField('rating', validators=[
        MaxValueValidator(5),
        MinValueValidator(0)
    ], blank=True)

    MEN = 'men'
    WOMEN = 'women'

    sex_list = [
        (MEN, 'Men'),
        (WOMEN, 'Women'),
    ]
    sex = models.CharField(
        max_length=30,
        choices=sex_list,
        default=MEN,
    )

    XXS = 'XXS'
    XS = 'XS'
    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'

    size_list = [
        (XXS, 'XXS'),
        (XS, 'XS'),
        (S, 'S'),
        (M, 'M'),
        (L, 'L'),
        (XL, 'XL'),
        (XXL, 'XXL'),
    ]
    size = models.CharField(
        max_length=30,
        choices=size_list,
        default=S,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Comment(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    author_name = models.CharField('имя автора', max_length=50)
    comment_text = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
