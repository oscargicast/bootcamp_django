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
        ('delivered', 'Entregado'),
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.SET_NULL,
        related_name='services',
        null=True,
        blank=True,
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

    class Meta:
        db_table = 'order'
        ordering = ['-created']

    def __str__(self):
        return f'Order {self.id}'
