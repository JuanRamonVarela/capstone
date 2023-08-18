from django.test import TestCase
from restaurant.views import MenuItemViewn
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Pasta', price=5, inventory=10)
        Menu.objects.create(title='Pasta2', price=5, inventory=10)

    def getAll(self):
        Menu.objects.all()