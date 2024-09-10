import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    
    cursor.executemany('INSERT INTO students (id, name, age, grade) VALUES (?, ?, ?, ?)', [
        (1, 'Erkin', 20, 3.8),
        (2, 'Amina', 21, 3.5),
        (3, 'Nurda', 22, 3.9)
    ])
    
    conn.commit()
    print("Три записи добавлены в таблицу students.")
    
except sqlite3.Error as e:
    print("Что-то пошло не так:", e)

finally:
    if conn:
        conn.close()