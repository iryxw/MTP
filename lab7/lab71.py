import sqlite3

conn = sqlite3.connect('example1.db')
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

cursor.execute("SELECT * FROM users WHERE id > 1")
selected_users = cursor.fetchall()

print("Выбранные пользователи (id > 1):")
for user in selected_users:
  print(f"ID={user[0]}, Имя={user[1]}, Почта={user[2]}")

conn.close()