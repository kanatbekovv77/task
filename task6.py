import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

   
    cursor.execute('DELETE FROM students WHERE id = ?', (3,))
    conn.commit()
    print("Студент с id = 3 удалён.")

 
    cursor.execute('SELECT * FROM students WHERE id = 3')
    record = cursor.fetchone()
    if record:
        print("Ошибка: запись всё ещё есть.")
    else:
        print("Запись с id = 3 удалена.")

except sqlite3.Error as e:
    print("Ошибка:", e)

finally:
    if conn:
        conn.close()
