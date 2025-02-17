from django.shortcuts import render
from customer.models import Customer
from cart.models import Cart
from book.models import Book

def ecom_page(request):
    books = Book.objects.all()
    customers = Customer.objects.all()
    cart = Cart.objects.first()  # Example: Fetch the first cart
    
    context = {
        'books': books,
        'customers': customers,
        'cart': cart
    }
    return render(request, 'ecom_page.html', context)
