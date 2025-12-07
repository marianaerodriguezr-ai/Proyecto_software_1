# src/repositories/in_memory/product_repository.py
from src.models.product import Product

class ProductRepository:
    def __init__(self):
        self.products = []
        self._next_id = 1

    def get_all(self):
        return self.products

    def get_by_id(self, product_id):
        return next((p for p in self.products if p.id == product_id), None)

    def create(self, product: Product):
        product.id = self._next_id
        self._next_id += 1
        self.products.append(product)
        return product

