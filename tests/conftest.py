import sys
import os

# Añades el root para que Python encuentre src/
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# === FIXTURES PARA LAS PRUEBAS ===

import pytest
from src.repositories.in_memory.category_repository import CategoryRepository
from src.repositories.in_memory.product_repository import ProductRepository
from src.services.category_service import CategoryService
from src.services.product_service import ProductService


@pytest.fixture
def category_service():
    repo = CategoryRepository()
    return CategoryService(repo)


@pytest.fixture
def product_service(category_service):
    repo = ProductRepository()
    return ProductService(repo, category_service.repository)
