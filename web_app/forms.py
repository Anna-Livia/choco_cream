from django.forms import ModelForm
from web_app.models import Transaction

class SpendingForm(ModelForm):
     class Meta:
        model = Transaction
        fields = ['amount']
