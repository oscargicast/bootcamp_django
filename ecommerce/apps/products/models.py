from django.db import models

from apps.base.models import BaseModel


class Material(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    # stock = models.PositiveIntegerField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table = 'material'
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        # ordering = ["-created_at"]


class Category(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    materials = models.ManyToManyField(Material)

    def __str__(self):
        return self.name
