from django.db import models
from django.conf import settings


class Table(models.Model):
    TABLE_CATEGORIES = (
        ('TWO', 'TWO'),
        ('THREE', 'THREE'),
        ('FOUR', 'FOUR'),
        ('FIVE', 'FIVE'),
        ('GROUP', 'GROUP')
    )
    table_number = models.IntegerField() 
    categotie = models.CharField(max_length=20, choices=TABLE_CATEGORIES)
    guests = models.IntegerField()
    def __str__(self):
        return f'table {self.table_number}. For {self.guests} people'


class Booking(models.Model):
    user = models.ForeignKey(settings. AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, blank=False,)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.TimeField()

    def __str__(self):
        return f'{self.user} has booked {self.table} on {self.arrival_time}'

