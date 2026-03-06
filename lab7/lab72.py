import sqlite3

conn = sqlite3.connect('example2.db')
cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
  )
''')
conn.commit()

cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (?, ?, ?)", (1, "Настя", "nastyaaa@example.com"))
cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (?, ?, ?)", (2, "Иван", "ivan@example.com"))
cursor.execute("INSERT OR IGNORE INTO users (id, name, email) VALUES (?, ?, ?)", (3, "Артём", "artem@example.com"))
conn.commit()

delete_id = 2

cursor.execute("DELETE FROM users WHERE id = ?", (delete_id,))
conn.commit()

cursor.execute("SELECT * FROM users")
remaining_users = cursor.fetchall()

print("Оставшиеся пользователи после удаления id=2:")
for user in remaining_users:
  print(f"ID={user[0]}, Имя={user[1]}, Почта={user[2]}")

conn.close()