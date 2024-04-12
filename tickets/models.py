from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class Concert(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    concert = models.ForeignKey(Concert, related_name='tickets', on_delete=models.CASCADE)
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_sold = models.BooleanField(default=False)
    seat_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Ticket {self.ticket_id} for {self.concert.name} (Seat {self.seat_number})"
    
@receiver(post_save, sender=Concert)
def create_tickets(sender, instance, created, **kwargs):
    if created:
        for seat_number in range(1, 101):
            price = 60.00 if seat_number <= 50 else 40.00
            Ticket.objects.create(concert=instance, seat_number=seat_number, price=price)

class Purchase(models.Model):
    concert = models.ForeignKey(Concert, related_name='purchases', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_purchase = models.DateField()
    number_of_tickets = models.PositiveIntegerField()
    tickets = models.ManyToManyField(Ticket)
    seat_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    student_discount = models.BooleanField(default=False)

    def calculate_ticket_price(self):
        if self.student_discount and self.seat_number > 50:
            return 25.00
        elif self.seat_number <= 50:
            return 65.00
        else:
            return 40.00

    def calculate_total_price(self):
        ticket_price = self.calculate_ticket_price()
        return self.number_of_tickets * ticket_price

    def __str__(self):
        return f"Purchase by {self.name} for {self.number_of_tickets} ticket(s) for {self.concert.name} (Seat {self.seat_number})"
