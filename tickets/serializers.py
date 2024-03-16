from rest_framework import serializers
from .models import Concert , Ticket, Purchase

class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ['id', 'name', 'date']  # Add more fields as needed

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'concert', 'ticket_id', 'is_sold', 'seat_number']  # Add more fields as needed

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ['id', 'concert', 'name', 'email', 'phone_number', 'date_of_purchase', 'number_of_tickets', 'tickets', 'seat_number']  # Add more fields as needed