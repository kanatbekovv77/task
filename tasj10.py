import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    try:
        
        conn.execute('BEGIN TRANSACTION')

        
        cursor.execute('UPDATE students SET grade = 4.0 WHERE age > 20')
        conn.commit()
        print("Оценки обновлены.")

    except sqlite3.Error as e:
        # Если ошибка, откатываем транзакцию
        conn.rollback()
        print("Ошибка. Изменения отменены:", e)

finally:
    if conn:
        conn.close()
