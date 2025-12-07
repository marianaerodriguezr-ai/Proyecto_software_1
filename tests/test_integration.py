# tests/test_integration.py

import pytest
from app import create_category, create_product, list_products

def test_create_product_with_existing_category():
    # 1. Crear categoría
    category = create_category(name="Electrónica")
    
    # 2. Crear producto asociado a esa categoría
    product = create_product(
        name="Celular",
        price=1500,
        category_id=category["id"]
    )
    
    # 3. Listar productos y verificar asociación
    products = list_products()
    
    assert any(p["id"] == product["id"] for p in products)
    assert product["category_id"] == category["id"]
