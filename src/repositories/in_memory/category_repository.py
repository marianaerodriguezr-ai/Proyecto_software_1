# src/repositories/in_memory/category_repository.py
from src.models.category import Category

class CategoryRepository:
    def __init__(self):
        self.categories = []
        self._next_id = 1

    def get_all(self):
        return self.categories

    def get_by_name(self, name):
        return next((c for c in self.categories if c.name == name), None)

    def get_by_id(self, id):
        return next((c for c in self.categories if c.id == id), None)

    def create(self, category: Category):
        category.id = self._next_id
        self._next_id += 1
        self.categories.append(category)
        return category
