
from django.shortcuts import render
from django.views.generic import TemplateView, DeleteView
from .models import Store
from django.urls import reverse_lazy
# Create your views here.


class HomePage(TemplateView):
    model = Store
    template_name = "home.html"


class AdminPage(TemplateView):
    mode = Store
    template_name = "adminpage.html"

class DeletePage(TemplateView):
    model = Store
    template_name = "delete_item.html"
    success_url = reverse_lazy('home')
