
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .models import Product
from django.shortcuts import render
# Create your views here.


class HomePage(TemplateView):
    model = Product
    template_name = "home.html"

    def get_products(self, request):
        product_list = Product.objects.all()
        return render(request, '../template/home.html', {'product_list': product_list})

    # def get_context_data(self, **kwargs):
    #     store_id = kwargs['pk']
    #     store = Product.objects.get(pk=store_id)
    #     return{'store': store}


class OwnerPage(TemplateView):
    mode = Product
    template_name = "ownerPage.html"


class CreateItem(CreateView):
    model = Product
    template_name = "add_item.html"
    fields = ['name', 'cost', 'quantity', 'image']
    success_url = reverse_lazy('home')
