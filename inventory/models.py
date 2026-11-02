
from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)

    length = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])

    width = models.DecimalField(max_digits=8, decimal_places=2, validators= [ MinValueValidator(0.01)])
    height = models.DecimalField(max_digits=8, decimal_places=2, validators=[ MinValueValidator(0.01)])

    weight = models.DecimalField( max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Box(models.Model):
    name = models.CharField(max_length=100, unique=True)
    internal_length = models.DecimalField( max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])

    internal_width = models.DecimalField( max_digits=8, decimal_places=2, validators=[ MinValueValidator(0.01)])

    internal_height = models.DecimalField(max_digits=8, decimal_places=2, validators=[ MinValueValidator(0.01)])

    max_weight = models.DecimalField(max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    
    cost = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
