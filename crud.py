from database import connect_db
from datetime import datetime

def create_user(name, role):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO users (name, role)
            VALUES (?, ?)
        """, (name, role))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()


def get_user(name):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM users
            WHERE name = ?
        """, (name,))

        return cursor.fetchone()

    except Exception as e:
        print(f"Ошибка: {e}")
        return None

    finally:
        connection.close()


def get_users():
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM users
        """)

        return cursor.fetchall()

    except Exception as e:
        print(f"Ошибка: {e}")
        return []

    finally:
        connection.close()

def create_category(title):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO categories (title)
            VALUES (?)
        """, (title,))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()


def get_categories():
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM categories
        """)

        return cursor.fetchall()

    except Exception as e:
        print(f"Ошибка: {e}")
        return []

    finally:
        connection.close()


def update_category(category_id, new_title):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE categories
            SET title = ?
            WHERE id = ?
        """, (new_title, category_id))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()


def delete_category(category_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM categories
            WHERE id = ?
        """, (category_id,))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()


def create_product(title, price, category_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO products (title, price, category_id)
            VALUES (?, ?, ?)
        """, (title, price, category_id))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()


def get_products():
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM products
        """)

        return cursor.fetchall()

    except Exception as e:
        print(f"Ошибка: {e}")
        return []

    finally:
        connection.close()


def update_product(product_id, title, price, category_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE products
            SET title = ?, price = ?, category_id = ?
            WHERE id = ?
        """, (title, price, category_id, product_id))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()


def delete_product(product_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM products
            WHERE id = ?
        """, (product_id,))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()



def create_order(user_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cursor.execute("""
            INSERT INTO orders (user_id, created_at)
            VALUES (?, ?)
        """, (user_id, created_at))

        order_id = cursor.lastrowid

        connection.commit()
        return order_id

    except Exception as e:
        print(f"Ошибка: {e}")
        return None

    finally:
        connection.close()


def add_order_item(order_id, product_id, quantity):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity)
            VALUES (?, ?, ?)
        """, (order_id, product_id, quantity))

        connection.commit()

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        connection.close()


def get_user_orders(user_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT * FROM orders
            WHERE user_id = ?
        """, (user_id,))

        return cursor.fetchall()

    except Exception as e:
        print(f"Ошибка: {e}")
        return []

    finally:
        connection.close()


def get_order_items(order_id):
    connection = connect_db()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT products.title, products.price, order_items.quantity
            FROM order_items
            JOIN products ON order_items.product_id = products.id
            WHERE order_items.order_id = ?
        """, (order_id,))

        return cursor.fetchall()

    except Exception as e:
        print(f"Ошибка: {e}")
        return []

    finally:
        connection.close()

def get_products_with_categories():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT products.title,
               products.price,
               categories.title
        FROM products
        JOIN categories
        ON products.category_id = categories.id
    """)

    result = cursor.fetchall()

    connection.close()

    return result


def count_products():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM products
    """)

    result = cursor.fetchone()

    connection.close()

    return result

def average_price():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT AVG(price)
        FROM products
    """)

    result = cursor.fetchone()

    connection.close()

    return result

def max_price():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT MAX(price)
        FROM products
    """)

    result = cursor.fetchone()

    connection.close()

    return result

def min_price():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT MIN(price)
        FROM products
    """)

    result = cursor.fetchone()

    connection.close()

    return result

def total_sales():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT SUM(products.price * order_items.quantity)
        FROM order_items
        JOIN products
        ON order_items.product_id = products.id
    """)

    result = cursor.fetchone()

    connection.close()

    return result

def products_by_category():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT categories.title,
               COUNT(order_items.id)
        FROM order_items
        JOIN products
            ON order_items.product_id = products.id
        JOIN categories
            ON products.category_id = categories.id
        GROUP BY categories.title
    """)

    result = cursor.fetchall()

    connection.close()

    return result

def products_above_average():
    connection = connect_db()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM products
        WHERE price >
        (
            SELECT AVG(price)
            FROM products
        )
    """)

    result = cursor.fetchall()

    connection.close()

    return result