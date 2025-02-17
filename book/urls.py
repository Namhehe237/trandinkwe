from django.urls import path
from .views import ecom_page

urlpatterns = [
    path('', ecom_page, name='ecom_page'),
]
