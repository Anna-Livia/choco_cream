from django.forms import ModelForm
from web_app.models import Spending

class SpendingForm(ModelForm):
     class Meta:
        model = Spending
        fields = ['amount']
