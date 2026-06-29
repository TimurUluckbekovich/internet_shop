from database import create_tables
from crud import *

# ---------------- ADMIN ----------------

def admin_menu():
    while True:
        print("\n=== АДМИНИСТРАТОР ===")
        print("1. Создать товар")
        print("2. Изменить товар")
        print("3. Удалить товар")
        print("4. Статистика продаж (пока нет)")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            title = input("Название: ")
            price = float(input("Цена: "))
            category_id = int(input("ID категории: "))
            create_product(title, price, category_id)

        elif choice == "2":
            pid = int(input("ID товара: "))
            title = input("Новое название: ")
            price = float(input("Новая цена: "))
            category_id = int(input("Новая категория: "))
            update_product(pid, title, price, category_id)

        elif choice == "3":
            pid = int(input("ID товара: "))
            delete_product(pid)

        elif choice == "4":
            print("Статистика будет реализована позже (SQL этап)")

        elif choice == "0":
            break


# ---------------- CUSTOMER ----------------

def customer_menu():
    while True:
        print("\n=== ПОКУПАТЕЛЬ ===")
        print("1. Просмотр товаров")
        print("2. Поиск товаров (пока как просмотр)")
        print("3. Создание заказа (пока заглушка)")
        print("4. Мои заказы (пока заглушка)")
        print("0. Выход")

        choice = input("Выбор: ")

        if choice == "1":
            print(get_products())

        elif choice == "2":
            print(get_products())  # позже заменим на SELECT LIKE

        elif choice == "3":
            print("Создание заказа будет позже (orders + order_items)")

        elif choice == "4":
            print("Заказы будут позже")

        elif choice == "0":
            break


# ---------------- ENTRY ----------------

create_tables()

print("=== ВХОД ===")
print("1. Администратор")
print("2. Покупатель")

role = input("Выбор: ")

if role == "1":
    admin_menu()

elif role == "2":
    customer_menu()

else:
    print("Неверная роль")