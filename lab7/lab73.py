import sqlite3
import csv

conn = sqlite3.connect('example3.db')
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

cursor.execute("SELECT id, name, email FROM users")
all_users = cursor.fetchall()

with open('export_test.csv', 'w', newline='', encoding='utf-8') as f:
  writer = csv.writer(f)
  writer.writerow(['ID', 'Имя', 'Email'])
  writer.writerows(all_users)

print("Данные успешно экспортированы в export_test.csv")

conn.close()