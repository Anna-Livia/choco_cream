from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import HttpResponse
from web_app.forms import SpendingForm
# from web_app.models import Spending


# Create your views here.
class home_page(FormView):
    template_name = 'home_page.html'
    form_class = SpendingForm


