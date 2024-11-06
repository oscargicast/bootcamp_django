from django.db import models

from model_utils.models import StatusModel
from model_utils import Choices

from apps.base.models import BaseModel


class Service(BaseModel, StatusModel):
    STATUS = Choices(
        ('to_quote', 'Por cotizar'),  # Pendiente de una cotización.
        ('quoted', 'Cotizado'),  # La cotización ha sido realizada.
        ('in_progress', 'En progreso'),  # El trabajo o servicio está en curso.
        ('done', 'Listo para recoger'),  # El pedido está listo para ser recogido por el cliente.
    )

    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='services',
    )
    # Service features
    file = models.FileField(
        upload_to='services/',
    )
    thickness = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='mm',
    )
    fold_number = models.PositiveIntegerField(
        default=0,
        blank=True,
        help_text='Number of folds',
    )
    material = models.ForeignKey(
        'products.Material',
        on_delete=models.SET_NULL,
        related_name='services',
        null=True,
        blank=True,
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
        filename = self.file.name.split('/')[-1]
        return f'{filename} - Thickness: {self.thickness}mm - Folds: {self.fold_number}'

    def save(self, *args, **kwargs):
        if self.unit_price:
            self.total_price = self.unit_price * self.units - self.discount
        super().save(*args, **kwargs)
