from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid


class Concert(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.tickets.exists():
            Ticket.objects.bulk_create([
                Ticket(concert=self, seat_number=i)
                for i in range(1, 401)
            ])

class Ticket(models.Model):
    concert = models.ForeignKey(Concert, related_name='tickets', on_delete=models.CASCADE)
    ticket_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    is_sold = models.BooleanField(default=False)
    seat_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(400)])
    price = models.DecimalField(max_digits=5, decimal_places=2, default=40)  # Set default value to 40

    PREMIUM = 'premium'
    STANDARD = 'standard'
    STUDENT = 'student'
    PRICE_CHOICES = [
        (PREMIUM, 'Premium'),
        (STANDARD, 'Standard'),
        (STUDENT, 'Student'),
    ]
    price_type = models.CharField(default='standard', max_length=20, choices=PRICE_CHOICES)

    def __str__(self):
        return f"Ticket {self.ticket_id} for {self.concert.name} (Seat {self.seat_number})"

class Purchase(models.Model):
    purchase_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    concert = models.CharField(max_length=100)  
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    date_of_purchase = models.DateField()
    tickets = models.JSONField(default=dict)  # Set default to an empty dictionary
    total_price = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f"Purchase ID: {self.purchase_id}"