import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    
    cursor.execute('ALTER TABLE students ADD COLUMN email TEXT')
    conn.commit()
    print("Добавлен столбец email.")

    
    cursor.execute('PRAGMA table_info(students)')
    columns = cursor.fetchall()
    print("Структура таблицы students:")
    for column in columns:
        print(column)

except sqlite3.Error as e:
    print("Ошибка при изменении таблицы:", e)

finally:
    if conn:
        conn.close()
