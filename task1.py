import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    print("Подключение успешно.")
except sqlite3.Error as error:
    print("Ошибка:", error)
finally:
    if conn:
        conn.close()


















        