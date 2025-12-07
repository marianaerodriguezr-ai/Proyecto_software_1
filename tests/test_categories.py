# tests/test_categories.py

import pytest
from unittest.mock import MagicMock
from src.services.category_service import CategoryService
from src.models.category import Category

def test_create_category_success():
    mock_repo = MagicMock()

    mock_repo.get_by_name.return_value = None  # No existe aún

    mock_repo.create.return_value = Category(id=1, name="Ropa")

    service = CategoryService(repository=mock_repo)

    new_category = service.create_category("Ropa")

    assert new_category.name == "Ropa"
    mock_repo.create.assert_called_once()


def test_create_category_duplicate():
    mock_repo = MagicMock()

    # Simula categoría existente
    mock_repo.get_by_name.return_value = Category(id=1, name="Ropa")

    service = CategoryService(repository=mock_repo)

    with pytest.raises(ValueError):
        service.create_category("Ropa")


def test_list_categories():
    mock_repo = MagicMock()

    mock_repo.get_all.return_value = [
        Category(id=1, name="Ropa"),
        Category(id=2, name="Electrónica")
    ]

    service = CategoryService(repository=mock_repo)

    categories = service.get_all_categories()

    assert len(categories) == 2
    mock_repo.get_all.assert_called_once()
