import sqlite3

conn = sqlite3.connect("parsing.prj")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
list = []
for row in cursor.execute("SELECT * FROM 'tiktok_users_view'"):
    username = row[2]
    list.append(username)

with open('parsing.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(list))