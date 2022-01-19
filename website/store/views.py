
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Store
# Create your views here.

#this is a test
#sdbsbhhsbs

class HomePage(TemplateView):
    model = Store
    template_name = "home.html"


class OwnerPage(TemplateView):
    mode = Store
    template_name = "ownerPage.html"


class CreateItem(CreateView):
    model = Store
    template_name = "add_item.html"
    fields = ['name', 'cost', 'quantity', 'image']
    success_url = reverse_lazy('home')
