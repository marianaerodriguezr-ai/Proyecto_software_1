# tests/test_products.py

import pytest
from unittest.mock import MagicMock
from src.services.product_service import ProductService
from src.models.product import Product

def test_create_product_success():
    mock_repo = MagicMock()

    product = Product(id=1, name="Laptop", price=2500)

    mock_repo.create.return_value = product

    service = ProductService(repository=mock_repo)

    result = service.create_product("Laptop", 2500)

    assert result.price == 2500
    mock_repo.create.assert_called_once()


def test_create_product_invalid_price():
    mock_repo = MagicMock()
    service = ProductService(repository=mock_repo)

    with pytest.raises(ValueError):
        service.create_product("Laptop", -100)


def test_get_all_products():
    mock_repo = MagicMock()
    mock_repo.get_all.return_value = [
        Product(id=1, name="Laptop", price=2500),
        Product(id=2, name="Mouse", price=50)
    ]

    service = ProductService(repository=mock_repo)

    products = service.get_products()

    assert len(products) == 2
    mock_repo.get_all.assert_called_once()
