from rest_framework.serializers import ModelSerializer
from .models import MenuItem, Booking

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'