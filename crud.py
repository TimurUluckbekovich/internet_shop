from database import connect_db

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