from rest_framework import serializers
from .models import Concert, Ticket, Purchase

class ConcertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = ['id', 'name', 'date']  # Add more fields as needed

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'concert', 'ticket_id', 'is_sold', 'seat_number']
        read_only_fields = ['ticket_id', 'is_sold', 'seat_number']  # Mark read-only fields

class PurchaseSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()  # Add a serializer method field for the calculated total_price

    class Meta:
        model = Purchase
        fields = ['id', 'concert', 'name', 'email', 'phone_number', 'date_of_purchase', 'number_of_tickets', 'total_price', 'seat_number', 'student_discount']
        read_only_fields = ['total_price']  # Mark total_price as read-only

    def get_total_price(self, obj):
        return obj.calculate_total_price()  # Calculate total price using the method from the model
