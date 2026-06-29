import random
from crud import *

class User:
    def __init__(self, id, name, role):
        self.__id = id
        self.name = name
        self._role = role

    def show_info(self):
        print(f"Пользователь: {self.name}")

    def get_id(self):
        return self.__id


class Customer(User):
    def show_info(self):
        print(f"Покупатель: {self.name}")

    def show_products(self):
        return get_products()

    def search_products(self, title):
        products = get_products()

        result = []

        for product in products:
            if title.lower() in product[1].lower():
                result.append(product)

        return result

    def create_order(self, product_id, quantity):
        order_id = create_order(self.get_id())
        add_order_item(order_id, product_id, quantity)

    def show_orders(self):
        orders = get_user_orders(self.get_id())
        for order in orders:
            order_id = order[0]
            created_at = order[2]

            print(f"\nЗаказ №{order_id}")
            print(f"Дата: {created_at}")
            print("Товары:")

            items = get_order_items(order_id)

            for item in items:
                title = item[0]
                price = item[1]
                qty = item[2]

                print(f"- {title} | {price} сом | x{qty}")


class Admin(User):
    def show_info(self):
        print(f"Администратор: {self.name}")

    def create_product(self, title, price, category_id):
        create_product(title, price, category_id)

    def update_product(self, product_id, title, price, category_id):
        update_product(product_id, title, price, category_id)

    def delete_product(self, product_id):
        delete_product(product_id)

    def create_category(self, title):
        create_category(title)

    def show_categories(self):
        categories = get_categories()

        print("\n===== КАТЕГОРИИ =====")

        for category in categories:
            print(f"ID: {category[0]} | {category[1]}")

    def update_category(self, category_id, title):
        update_category(category_id, title )

    def delete_category(self, category_id):
        delete_category(category_id)

    # ---------- СТАТИСТИКА ----------

    def show_statistics(self):

        print("\n========== СТАТИСТИКА ==========")

        print(f"Количество товаров: {count_products()[0]}")
        print(f"Средняя цена: {average_price()[0]}")
        print(f"Максимальная цена: {max_price()[0]}")
        print(f"Минимальная цена: {min_price()[0]}")
        print(f"Общая сумма продаж: {total_sales()[0]}")

        print("\nПродажи по категориям:")

        for row in products_by_category():
            print(f"{row[0]} - {row[1]}")

        print("\nТовары дороже средней цены:")

        for row in products_above_average():
            print(f"{row[1]} - {row[2]} сом")

from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, id, title, price, category_id):
        self.id = id
        self.title = title
        self.price = price
        self.category_id = category_id

    @abstractmethod
    def show_info(self):
        pass

class DiscountMixin:
    def get_discount_price(self):
        return self.price * 0.9

class ShopProduct(Product, DiscountMixin):
    def __init__(self, id, title, price, category_id):
        super().__init__(id, title, price, category_id)

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["title"],
            data["price"],
            data["category_id"]
        )

    @classmethod
    def from_db(cls, data):
        return cls(
            data[0],
            data[1],
            data[2],
            data[3]
        )

    def show_info(self):
        print(
            f"Товар: {self.title}\n"
            f"Цена: {self.price}\n"
            f"Категория: {self.category_id}"
        )

    def __str__(self):
        return f"{self.title} ({self.price} сом)"

    def __eq__(self, other):
        if isinstance(other, ShopProduct):
            return self.id == other.id
        return False

    def __len__(self):
        return len(self.title)

    def __add__(self, other):
        if isinstance(other, ShopProduct):
            return self.price + other.price
        return NotImplemented

    @staticmethod
    def validate_price(price):
        return price > 0

    @staticmethod
    def generate_article():
        return random.randint(100000, 999999)

class Category:
    def __init__(self, id, title):
        self.id = id
        self.title = title

class Order:
    def __init__(self, id, user_id, created_at):
        self.id = id
        self.user_id = user_id
        self.created_at = created_at
