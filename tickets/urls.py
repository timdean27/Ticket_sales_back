from django.urls import path
from . import views

urlpatterns = [
    # Concerts URLs
    path('concerts/', views.ConcertListCreateAPIView.as_view(), name='concert-list'),
    path('concerts/<int:pk>/', views.ConcertRetrieveUpdateDestroyAPIView.as_view(), name='concert-detail'),

    # Tickets URLs
    path('tickets/', views.TicketListCreateAPIView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', views.TicketRetrieveUpdateDestroyAPIView.as_view(), name='ticket-detail'),

    # Purchases URLs
    path('purchases/', views.PurchaseListCreateAPIView.as_view(), name='purchase-list'),
    path('purchases/<int:pk>/', views.PurchaseRetrieveUpdateDestroyAPIView.as_view(), name='purchase-detail'),
]
