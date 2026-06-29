from database import create_tables
from crud import *

create_tables()

create_category("Ноутбуки")
create_category("Телефоны")

print(get_categories())

update_category(2, "Смартфоны")

print(get_categories())

delete_category(1)

print(get_categories())