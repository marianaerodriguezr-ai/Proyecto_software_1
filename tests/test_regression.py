def test_create_category_regression(category_service):
    category = category_service.create_category("Electronics")
    assert category.id == 1
    assert category.name == "Electronics"

def test_create_product_regression(product_service, category_service):
    category = category_service.create_category("Fruits")
    product = product_service.create_product("Apple", 1.99, category.id)

    assert product.name == "Apple"
    assert product.price == 1.99
    assert product.category_id == category.id
