from typing import Any
from django.shortcuts import render, redirect #here by default
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.views import View
from django import forms

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page...",
            "author": "Developed by: Martin",
        })
        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "subtitle": "Contact us",
            "email": "Email: user@onlinestore.com",
            "address": "EAFIT UNIVERSITY - Medellín, Colombia",
            "phone": "+57 300 000 0000"
        })
        return context
    

class Product:
    products = [
        {"id":"1","name":"TV","description":"Best TV","price":"$250.00"},
        {"id":"2","name":"iPhone","description":"Best iPhone","price":"$800.00"},
        {"id":"3","name":"Chromecast","description":"Best Chromecast","price":"$300.00"},
        {"id":"4","name":"Glasses","description":"Best Glasses","price":"$150.00"}
    ]


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)
    

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product = Product.products[int(id)-1]
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse('home'))
        
        product_price = float(product["price"].replace("$", "").replace(",", ""))
        viewData = {
            "title": product["name"] + " - Online Store",
            "subtitle": product["name"] + " - Product information",
            "product": product,
            "is_expensive": product_price > 100  # Add this flag
        }
        return render(request, self.template_name, viewData)
    

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError('The price must be greater than zero.')
        return price


class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {"title": "Create product", "form": form}
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('show', args=[product.id]))
        else:
            viewData = {"title": "Create product", "form": form}
            return render(request, self.template_name, viewData)