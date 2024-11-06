from django.db import models

from model_utils.models import StatusModel
from model_utils import Choices

from apps.base.models import BaseModel


class Order(BaseModel, StatusModel):
    STATUS = Choices(
        ('draft', 'Borrador'),
        ('to_quote', 'Por cotizar'),
        ('paid', 'Pagado'),
        ('in_progress', 'En progreso'),
        ('done', 'Listo para recoger'),
        ('delivered', 'Entregado'),
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        related_name='services',
        null=True,
        blank=True,
    )
    total_discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text='Total discount',
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Total price',
    )

    def __str__(self):
        return f'Order {self.id}'


class OrderLine(BaseModel):
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
    discount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text='Total discount',
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Total price',
    )

    def __str__(self):
        return f'OrderLine {self.id}'

    def save(self, *args, **kwargs):
        if self._state.adding:
            if self.unit_price is None and self.product:
                self.unit_price = self.product.price
            self.total_price = self.unit_price * self.units - self.discount
        super().save(*args, **kwargs)
