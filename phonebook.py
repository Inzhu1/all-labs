import psycopg2
import csv

def connect():
    return psycopg2.connect(
        dbname="phonebook",
        user="inzhuaitakhyn",
        password="",  
        host="localhost",
        port="5432"
    )

# Создание таблицы
def create_table():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    print("Таблица создана.")

# Вставка данных из CSV
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute("""
                INSERT INTO PhoneBook (first_name, phone) 
                VALUES (%s, %s) 
                ON CONFLICT (phone) DO NOTHING;
            """, (row['first_name'], row['phone']))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные из CSV загружены.")

# Вставка данных с консоли
def insert_from_input():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO PhoneBook (first_name, phone) 
        VALUES (%s, %s) 
        ON CONFLICT (phone) DO NOTHING;
    """, (name, phone))
    conn.commit()
    cur.close()
    conn.close()
    print("Данные добавлены.")

# Обновление данных
def update_data():
    choice = input("Что обновить? (1 - имя, 2 - номер): ")
    conn = connect()
    cur = conn.cursor()

    if choice == '1':
        phone = input("Введите номер телефона, чей владелец меняется: ")
        new_name = input("Введите новое имя: ")
        cur.execute("UPDATE PhoneBook SET first_name = %s WHERE phone = %s", (new_name, phone))
    elif choice == '2':
        name = input("Введите имя: ")
        new_phone = input("Введите новый номер: ")
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE first_name = %s", (new_phone, name))

    conn.commit()
    cur.close()
    conn.close()
    print("Данные обновлены.")

# Поиск
def search():
    filter_type = input("Фильтр по (1 - имени, 2 - номеру, 3 - все): ")
    conn = connect()
    cur = conn.cursor()

    if filter_type == '1':
        name = input("Введите имя для поиска: ")
        cur.execute("SELECT * FROM PhoneBook WHERE first_name ILIKE %s", ('%' + name + '%',))
    elif filter_type == '2':
        phone = input("Введите номер: ")
        cur.execute("SELECT * FROM PhoneBook WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM PhoneBook")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()

# Удаление
def delete_entry():
    filter_type = input("Удалить по (1 - имени, 2 - номеру): ")
    conn = connect()
    cur = conn.cursor()

    if filter_type == '1':
        name = input("Введите имя: ")
        cur.execute("DELETE FROM PhoneBook WHERE first_name = %s", (name,))
    elif filter_type == '2':
        phone = input("Введите номер: ")
        cur.execute("DELETE FROM PhoneBook WHERE phone = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()
    print("Запись удалена.")

# Главное меню
def menu():
    create_table()
    while True:
        print("\n1. Добавить из CSV")
        print("2. Добавить вручную")
        print("3. Обновить данные")
        print("4. Поиск")
        print("5. Удалить")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите путь к CSV файлу: ")
            insert_from_csv(filename)
        elif choice == '2':
            insert_from_input()
        elif choice == '3':
            update_data()
        elif choice == '4':
            search()
        elif choice == '5':
            delete_entry()
        elif choice == '0':
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    menu()
