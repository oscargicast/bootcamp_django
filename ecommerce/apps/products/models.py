from django.db import models

from apps.base.models import BaseModel


class Material(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta(BaseModel.Meta):
        db_table = 'material'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Thickness(BaseModel):
    material = models.ForeignKey(
        Material,
        on_delete=models.CASCADE,
        related_name='thicknesses',
    )

    value_mm = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    value_inch = models.CharField(
        max_length=10,
        blank=True,
    )

    class Meta(BaseModel.Meta):
        db_table = 'thickness'
        ordering = ['-created']

    @property
    def value(self) -> str:
        if self.value_inch:
            return f"{self.value_mm} mm ({self.value_inch})''"
        return f'{self.value_mm} mm'

    def __str__(self):
        return f'{self.material.name} - {self.value}'


class Category(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'
        ordering = ['-created']

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
    )
    material = models.ForeignKey(
        Material,
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        db_table = 'product'
        ordering = ['-created']

    def __str__(self):
        return self.name


class ProductLine(BaseModel):
    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='lines',
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.PROTECT,
        related_name='order_lines',
    )

    units = models.PositiveIntegerField(
        default=1,
        help_text='Quantity of units',
    )
    # Pricing
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Price per unit',
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Total price',
    )

    class Meta:
        db_table = 'order_line'
        ordering = ['-created']

    def __str__(self):
        return f'OrderLine {self.id}'

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.unit_price = self.product.price
            self.total_price = self.unit_price * self.units
        super().save(*args, **kwargs)
