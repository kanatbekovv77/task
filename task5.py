import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    
    cursor.execute('UPDATE students SET grade = ? WHERE id = ?', (3.7, 2))
    conn.commit()
    print("Оценка для студента с id = 2 обновлена.")

    
    cursor.execute('SELECT * FROM students WHERE id = 2')
    record = cursor.fetchone()
    print("Вот обновлённая запись:")
    print(f"ID: {record[0]}, Имя: {record[1]}, Возраст: {record[2]}, Оценка: {record[3]}")

except sqlite3.Error as e:
    print("Ошибка при обновлении:", e)

finally:
    if conn:
        conn.close()
