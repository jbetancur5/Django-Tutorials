from django.urls import path
from .views import *
from .utils import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('products/', ProductIndex.as_view(), name='index'),
    path('products/create/', ProductCreate.as_view(), name='form'),
    path('producs/success/', Success.as_view(), name='success'),
    path('products/<str:id>', ProductShow.as_view(), name='show'),
    path('cart/', Cart.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', Cart.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAll.as_view(), name='cart_removeAll'),
    path('image/',
         ImageFactory(ImageLocalStorage()).as_view(),
         name='image_index'),
    path('image/save',
         ImageFactory(ImageLocalStorage()).as_view(),
         name='image_save'),
]
