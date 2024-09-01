from classes.products import Electronics, Clothing, Householdchemicals
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
soap = Householdchemicals(name="Мыло", category="Детское", brand="Череда", price=50)

# Создаем пользователей
customer = Customer(username="Marina", email="m.perfileva@inbox.ru", address="033 Russ Bur")
admin = Admin(username="m.perfileva", email="m.perfileva@inbox.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(customer_name=customer.username, user_role=admin.username)
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(soap, 3)

# Выводим детали корзины
print(cart.get_details())
