python manage.py shell

from book.models import Book
Book.objects.create(title="Django for Beginners", author="William S. Vincent", price=25.99, stock=10)
Book.objects.create(title="Python Crash Course", author="Eric Matthes", price=30.99, stock=5)
Book.objects.create(title="Clean Code", author="Robert C. Martin", price=40.00, stock=8)

from customer.models import Customer
Customer.objects.create(name="John Doe", email="johndoe@example.com", phone="1234567890")
Customer.objects.create(name="Jane Smith", email="janesmith@example.com", phone="0987654321")


from book.models import Book
Book.objects.create(title="Django for Beginners", author="William S. Vincent", price=25.99, stock=10)
Book.objects.create(title="Python Crash Course", author="Eric Matthes", price=30.99, stock=5)
Book.objects.create(title="Clean Code", author="Robert C. Martin", price=40.00, stock=8)


from cart.models import Cart
from customer.models import Customer
from book.models import Book

customer = Customer.objects.first()  # Get the first customer
cart = Cart.objects.create(customer=customer)
cart.book.set(Book.objects.all())  # Add all books to the cart

exit()
