import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    
    try:
        cursor.execute('INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)', (1, 'Alice', 20, 3.8))
        conn.commit()
        print("Запись добавлена.")
    except sqlite3.IntegrityError:
        print("Ошибка: запись с таким id уже есть.")

except sqlite3.Error as e:
    print("Ошибка при работе с базой данных:", e)

finally:
    if conn:
        conn.close()
