from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid

class Concert(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    concert = models.ForeignKey(Concert, related_name='tickets', on_delete=models.CASCADE)
    ticket_id = models.CharField(max_length=10, unique=True, default=uuid.uuid4)
    is_sold = models.BooleanField(default=False)
    seat_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"Ticket {self.ticket_id} for {self.concert.name} (Seat {self.seat_number})"

class Purchase(models.Model):
    concert = models.ForeignKey(Concert, related_name='purchases', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_purchase = models.DateField()
    number_of_tickets = models.PositiveIntegerField()
    tickets = models.ManyToManyField(Ticket)
    seat_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"Purchase by {self.name} for {self.number_of_tickets} ticket(s) for {self.concert.name} (Seat {self.seat_number})"
