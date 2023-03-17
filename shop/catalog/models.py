from django.db import models

class ProductCategory(models.Model):
    class Meta:
        pass
    name = models.CharField(
        verbose_name='название',
        max_length=100
    )
    description = models.TextField(
        verbose_name='описание',
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        verbose_name='название продукта',
        max_length=200,
        help_text='краткое название продукта'
        )
    image = models.ImageField(
            verbose_name='фото продукта',
            upload_to='products'
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    short_description = models.CharField(
        verbose_name='краткое описание',
        max_length=64,
        help_text='отображается в карточке'
    )
    price = models.DecimalField(
        verbose_name='цена',
        max_digits=6,
        decimal_places=2
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0
    )
    category = models.ForeignKey(
        ProductCategory,
        verbose_name='категория',
        on_delete=models.PROTECT
    )
    
    def __str__(self):
        return self.name