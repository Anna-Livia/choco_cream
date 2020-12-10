from django.test import TestCase, Client

# Create your tests here.
class HomePage(TestCase) :
    def test_home_page_loads(self):
        response = Client().get('/')
        html = response.content.decode('utf8')
        self.assertIn("Anna-Livia", html)

class SpendingModel(TestCase):
    def test_spending_model_exists(self):
        from web_app.models import Spending
        new_spending = Spending.objects.create()
        self.assertEqual(Spending.objects.count(), 1)



