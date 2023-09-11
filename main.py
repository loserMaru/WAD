class Product:
    def __init__(self, id, name, upc, manufacturer, price, shelf_life, quantity):
        self.id = id
        self.name = name
        self.upc = upc
        self.manufacturer = manufacturer
        self.price = price
        self.shelf_life = shelf_life
        self.quantity = quantity

    # Геттеры и сеттеры для Tun (наименование товара)
    def getTun(self):
        return self.name

    def setTun(self, name):
        self.name = name

    def toString(self):
        return f"ID: {self.id}, Наименование: {self.name}, UPC: {self.upc}, Производитель: {self.manufacturer}, Цена: {self.price}, Срок хранения: {self.shelf_life}, Количество: {self.quantity}"

    def hashCode(self):
        return hash(self.id)


# Создаем массив объектов Product
products = [
    Product(1, "Товар1", "123456", "Производитель1", 10.99, 365, 100),
    Product(2, "Товар2", "789012", "Производитель2", 15.49, 180, 50),
    Product(3, "Товар3", "345678", "Производитель1", 5.99, 90, 200),
    Product(4, "Товар4", "901234", "Производитель3", 8.99, 270, 75),
]


# a) Список товаров для заданного наименования
def find_products_by_name(products, name):
    return [product for product in products if product.getTun() == name]


# b) Список товаров для заданного наименования, цена которых не превосходит заданную
def find_products_by_name_and_price(products, name, max_price):
    return [product for product in products if product.getTun() == name and product.price <= max_price]


# c) Список товаров, срок хранения которых больше заданного
def find_products_by_shelf_life(products, min_shelf_life):
    return [product for product in products if product.shelf_life > min_shelf_life]


# Примеры использования
name_to_find = "Товар1"
max_price_to_find = 11.0
min_shelf_life_to_find = 200

print("a) Список товаров для заданного наименования:")
for product in find_products_by_name(products, name_to_find):
    print(product.toString())

print("\nb) Список товаров для заданного наименования, цена которых не превосходит заданную:")
for product in find_products_by_name_and_price(products, name_to_find, max_price_to_find):
    print(product.toString())

print("\nc) Список товаров, срок хранения которых больше заданного:")
for product in find_products_by_shelf_life(products, min_shelf_life_to_find):
    print(product.toString())
