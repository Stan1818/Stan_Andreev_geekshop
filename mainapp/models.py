from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=150, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):
        return f'#{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='product', blank=True, verbose_name='Изображение')
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
