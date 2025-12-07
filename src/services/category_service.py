# src/services/category_service.py
from src.models.category import Category
from src.repositories.in_memory.category_repository import CategoryRepository

class CategoryService:
    def __init__(self, repository=None):
        self.repository = repository or CategoryRepository()

    def create_category(self, name: str):
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty")

        existing = self.repository.get_by_name(name)
        if existing:
            raise ValueError("Category already exists")

        category = Category(id=None, name=name)
        return self.repository.create(category)

    def get_all_categories(self):
        return self.repository.get_all()
