from django.test import TestCase, Client
from web_app.models import Transaction
# Create your tests here.
class HomePage(TestCase) :
    def test_home_page_loads(self):
        response = Client().get('/')
        html = response.content.decode('utf8')
        self.assertIn("Anna-Livia", html)

    def test_given_amount_is_added_to_db(self):
        response = self.client.post(
            "/", data={"amount": "33.6"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<li>33.6</li>", response.content)
        self.assertEqual(Transaction.objects.count(), 1)

class SpendingModel(TestCase):
    def test_spending_model_exists(self):
        Transaction.objects.create(amount=4)
        self.assertEqual(Transaction.objects.count(), 1)



