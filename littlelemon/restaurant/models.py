from django.db import models
from django.core.validators import MaxValueValidator

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])

    def __str__(self):
        return f'{self.title} : {str(self.price)}'