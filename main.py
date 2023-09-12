class Product:
    def __init__(self, id, name, upc, manufacturer, price, shelf_life, quantity):
        self.id = id
        self.name = name
        self.upc = upc
        self.manufacturer = manufacturer
        self.price = price
        self.shelf_life = shelf_life
        self.quantity = quantity

    def __getattr__(self, name):
        return self.name

    def __setattr__(self, name, value):
        if name == 'name':
            self.__dict__[name] = value
        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"ID: {self.id}, Наименование: {self.name}, UPC: {self.upc}, Производитель: {self.manufacturer}, Цена: {self.price}, Срок хранения: {self.shelf_life}, Количество: {self.quantity}"

    def __hash__(self):
        return hash(self.name)


products = [
    Product(1, "Товар1", "123456", "Производитель1", 10.99, 365, 100),
    Product(2, "Товар2", "789012", "Производитель2", 15.49, 180, 50),
    Product(3, "Товар3", "345678", "Производитель1", 5.99, 90, 200),
    Product(4, "Товар4", "901234", "Производитель3", 8.99, 270, 75),
    Product(5, "Товар5", "723492", "Производитель2", 11.49, 250, 125)]


def find_products_by_name(products, name):
    return [product for product in products if product.__getattr__('name') == name]


name = "Товар1"  # Замените на нужное наименование
matching_products = find_products_by_name(products, name)

for product in matching_products:
    print(product, '\n')


def find_products_by_name_and_price(products, name, max_price):
    return [product for product in products if
            product.__getattr__('name') == name and product.price <= max_price]


name = "Товар2"
max_price = 21.0
matching_products = find_products_by_name_and_price(products, name, max_price)

for product in matching_products:
    print(product, '\n')


def find_products_by_shelf_life(products, min_shelf_life):
    return [product for product in products if product.shelf_life > min_shelf_life]


min_shelf_life = 200
matching_products = find_products_by_shelf_life(products, min_shelf_life)

for product in matching_products:
    print(product)
