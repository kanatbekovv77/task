import sqlite3

try:
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade REAL
    )
    ''')
    
    conn.commit()
    print("Таблица students создана, если не существовала.")
    
except sqlite3.Error as e:
    print("Ошибка:", e)

finally:
    if conn:
        conn.close()


  
        






