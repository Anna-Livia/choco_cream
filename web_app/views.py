from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from web_app.forms import SpendingForm
from web_app.models import Transaction
import logging
log = logging.getLogger()

# Create your views here.
class home_page(CreateView):
    model = Transaction
    fields = ["amount"]
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super(home_page, self).get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.all()
        return context



