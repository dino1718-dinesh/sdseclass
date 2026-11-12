class Product:
   def __init__(self, name, price):
       if price < 0:
           raise ValueError("Price cannot be negative")
       self.name = name
       self.price = price

class CartItem:
   def __init__(self, product, quantity):
       if quantity <= 0:
           raise ValueError("Quantity must be positive")
       self.product = product
       self.quantity = quantity

   def subtotal(self):
       return self.product.price * self.quantity

class ShoppingCart:
   def __init__(self):
       self.items = []
       self.discount = 0

   def add_product(self, product, quantity):
       self.items.append(CartItem(product, quantity))

   def remove_product(self, product_name):
       self.items = [item for item in self.items
                     if item.product.name != product_name]

   def apply_discount(self, percentage):
       if not 0 <= percentage <= 100:
           raise ValueError("Discount must be between 0 and 100")
       self.discount = percentage

   def calculate_total(self):
       subtotal = sum(item.subtotal() for item in self.items)
       return subtotal * (1 - self.discount / 100)
laptop = Product("Laptop", 50000)
mouse = Product("Mouse", 500)
cart = ShoppingCart()
cart.add_product(laptop, 1)
cart.add_product(mouse, 2)
print("Before discount:", cart.calculate_total())
cart.apply_discount(10)
print("After 10% discount:", cart.calculate_total())
cart.remove_product("Mouse")
print("After removing Mouse:", cart.calculate_total())
import unittest

class TestShoppingCart(unittest.TestCase):
   def setUp(self):
       self.cart = ShoppingCart()
       self.laptop = Product("Laptop", 50000)
       self.mouse = Product("Mouse", 500)

   def test_add_product(self):
       self.cart.add_product(self.laptop, 1)
       self.assertEqual(self.cart.calculate_total(), 50000)

   def test_remove_product(self):
       self.cart.add_product(self.mouse, 1)
       self.cart.remove_product("Mouse")
       self.assertEqual(self.cart.calculate_total(), 0)

   def test_discount(self):
       self.cart.add_product(self.laptop, 1)
       self.cart.apply_discount(10)
       self.assertEqual(self.cart.calculate_total(), 45000)

   def test_empty_cart(self):
       self.assertEqual(self.cart.calculate_total(), 0)

   def test_invalid_discount(self):
       with self.assertRaises(ValueError):
           self.cart.apply_discount(110)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestShoppingCart)
result = unittest.TextTestRunner(verbosity=2).run(suite)
print("All tests passed:", result.wasSuccessful())
