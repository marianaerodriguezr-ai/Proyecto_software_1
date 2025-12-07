from src.repositories.in_memory.category_repository import CategoryRepository
from src.repositories.in_memory.product_repository import ProductRepository

from src.services.category_service import CategoryService
from src.services.product_service import ProductService

# Crear repositorios en memoria
category_repository = CategoryRepository()
product_repository = ProductRepository()

# Inyectar repositorios en los servicios
category_service = CategoryService(repository=category_repository)
product_service = ProductService(
    repository=product_repository,
    category_repository=category_repository
)

# Funciones que los tests de integración esperan
def create_category(name: str):
    category = category_service.create_category(name)
    return {
        "id": category.id,
        "name": category.name
    }

def create_product(name: str, price: float, category_id: int):
    product = product_service.create_product(name, price, category_id)
    return {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "category_id": product.category_id
    }

def list_products():
    return [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "category_id": p.category_id
        }
        for p in product_service.get_products()
    ]

