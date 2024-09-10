import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    
    cursor.execute('SELECT * FROM students WHERE age > 20')
    records = cursor.fetchall()

    
    print("Студенты старше 20 лет:")
    for row in records:
        print(f"ID: {row[0]}, Имя: {row[1]}, Возраст: {row[2]}, Оценка: {row[3]}")

except sqlite3.Error as e:
    print("Ошибка при запросе данных:", e)

finally:
    if conn:
        conn.close()
