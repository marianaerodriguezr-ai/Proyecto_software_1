# src/repositories/category_repository.py

class CategoryRepository:
    def __init__(self):
        self.categories = []

    def get_all(self):
        return self.categories

    def create(self, name):
        if name in self.categories:
            return False
        self.categories.append(name)
        return True

    def delete(self, name):
        if name not in self.categories:
            return False
        self.categories.remove(name)
        return True
