from database import create_tables
from models import Customer, Admin
from crud import create_user, get_user

create_tables()

print("========== ИНТЕРНЕТ-МАГАЗИН ==========")
print("Для проверки администратора используйте имя: Admin")
print()

print("1. Вход")
print("2. Регистрация")

choice = input("Выберите действие: ")

if choice == "2":
    name = input("Введите имя: ")
    create_user(name, "customer")
    print("Регистрация успешно завершена!\n")

name = input("Введите имя: ")

user = get_user(name)

if not user:
    print("Пользователь не найден.")
    exit()

if user[2] == "admin":
    current_user = Admin(user[0], user[1], user[2])
else:
    current_user = Customer(user[0], user[1], user[2])

current_user.show_info()

while True:

    if isinstance(current_user, Customer):

        print("\n===== ПОКУПАТЕЛЬ =====")
        print("1. Просмотр товаров")
        print("2. Поиск товара")
        print("3. Создать заказ")
        print("4. Мои заказы")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":

            products = current_user.show_products()

            print("\n===== СПИСОК ТОВАРОВ =====")

            for product in products:
                print(f"""
                            ID: {product[0]}
                            Название: {product[1]}
                            Цена: {product[2]} сом
                            Категория: {product[3]}
                            ----------------------------
                        """)

        elif choice == "2":

            title = input("Введите название: ")

            products = current_user.search_products(title)

            print("\n===== РЕЗУЛЬТАТ ПОИСКА =====")

            if not products:
                print("Ничего не найдено.")

            else:
                for product in products:
                    print(f"""
                                ID: {product[0]}
                                Название: {product[1]}
                                Цена: {product[2]} сом
                                Категория: {product[3]}
                                ----------------------------
                            """)

        elif choice == "3":
            product_id = int(input("ID товара: "))
            quantity = int(input("Количество: "))
            current_user.create_order(product_id, quantity)
            print("Заказ успешно создан.")

        elif choice == "4":
            print("\n===== МОИ ЗАКАЗЫ =====")
            current_user.show_orders()

        elif choice == "0":
            break


    elif isinstance(current_user, Admin):
        print("\n===== АДМИНИСТРАТОР =====")
        print("1. Создать товар")
        print("2. Изменить товар")
        print("3. Удалить товар")
        print("4. Просмотр статистики")
        print("5. Создать категорию")
        print("6. Просмотр категорий")
        print("7. Изменить категорию")
        print("8. Удалить категорию")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Название: ")
            price = float(input("Цена: "))
            category = int(input("ID категории: "))

            current_user.create_product(title, price, category)
            print("Товар успешно добавлен.")

        elif choice == "2":
            product_id = int(input("ID товара: "))
            title = input("Новое название: ")
            price = float(input("Новая цена: "))
            category = int(input("Новая категория: "))
            current_user.update_product(product_id, title, price, category)
            print("Товар обновлен.")

        elif choice == "3":
            product_id = int(input("ID товара: "))
            current_user.delete_product(product_id)
            print("Товар удален.")

        elif choice == "4":
            current_user.show_statistics()

        elif choice == "5":
            title = input("Название категории: ")
            current_user.create_category(title)
            print("Категория добавлена.")

        elif choice == "6":
            current_user.show_categories()

        elif choice == "7":
            category_id = int(input("ID категории: "))
            title = input("Новое название: ")
            current_user.update_category(category_id, title)
            print("Категория изменена.")

        elif choice == "8":
            category_id = int(input("ID категории: "))
            current_user.delete_category(category_id)
            print("Категория удалена.")

        elif choice == "0":
            break