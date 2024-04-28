from rest_framework import serializers
from .models import Concert, Ticket, Purchase

class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ['id', 'name', 'date']  # Add more fields as needed

class TicketSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=5, decimal_places=2)  # Include price field

    class Meta:
        model = Ticket
        fields = ['id', 'concert', 'ticket_id', 'is_sold', 'seat_number', 'price', 'price_type']  # Include price field in fields list


class PurchaseSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=7, decimal_places=2)  # Add total_price field

    class Meta:
        model = Purchase
        fields = ['id', 'concert', 'purchase_id','name', 'email', 'phone_number', 'date_of_purchase', 'tickets', 'total_price']
        read_only_fields = ['total_price']  # Mark total_price as read-only
