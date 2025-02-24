from django.test import TestCase
from restaurant.models import MenuItem
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        self.menu1 = MenuItem.objects.create(title="Pasta", price=10.99, inventory=20)
        self.menu2 = MenuItem.objects.create(title="Burger", price=5.99, inventory=50)
        self.menu3 = MenuItem.objects.create(title="Salad", price=7.99, inventory=30)

    def test_getall(self):
        url = reverse('menu') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = [
            {"id": self.menu1.id, "title": "Pasta", "price": "10.99", "inventory": 20},
            {"id": self.menu2.id, "title": "Burger", "price": "5.99", "inventory": 50},
            {"id": self.menu3.id, "title": "Salad", "price": "7.99", "inventory": 30},
        ]
        self.assertEqual(response.json(), expected_data)
