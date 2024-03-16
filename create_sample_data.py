# create_sample_data.py

from django.utils import timezone
from my_concert_ticket_project.tickets.models import Concert, Ticket, Purchase

# Your sample data creation code here

concert = Concert.objects.get_or_create(name="Concert Name", date=timezone.now())[0]
ticket1 = Ticket.objects.create(concert=concert, ticket_id="ABC123", is_sold=False, seat_number=1)
ticket2 = Ticket.objects.create(concert=concert, ticket_id="DEF456", is_sold=False, seat_number=2)
purchase = Purchase.objects.create(
    concert=concert,
    name="John Doe",
    email="john@example.com",
    phone_number="123456789",
    date_of_purchase=timezone.now(),
    number_of_tickets=2,
    seat_number=1
)
purchase.tickets.add(ticket1, ticket2)