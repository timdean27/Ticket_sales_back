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
    ticket_id = models.CharField(max_length=32, unique=True, default=uuid.uuid4)
    is_sold = models.BooleanField(default=False)
    seat_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # Price field to store ticket price

    def save(self, *args, **kwargs):
        if self.seat_number <= 50:
            self.price = 60.00  # Default price for seats 1-50
        else:
            self.price = 40.00  # Default price for the rest
        super().save(*args, **kwargs)

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
    student_discount = models.BooleanField(default=False)  # Boolean field for student discount

    def calculate_ticket_price(self):
        if self.student_discount and self.seat_number > 50:
            return 25.00  # Price reduced to $25 for student discount
        elif self.seat_number <= 50:
            return 65.00  # Price is $65 for top 50 seats
        else:
            return 40.00  # Price is $40 for remaining seats

    def calculate_total_price(self):
        ticket_price = self.calculate_ticket_price()
        return self.number_of_tickets * ticket_price

    def __str__(self):
        return f"Purchase by {self.name} for {self.number_of_tickets} ticket(s) for {self.concert.name} (Seat {self.seat_number})"
